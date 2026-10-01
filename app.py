from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import PyPDF2
from docx import Document
import re

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB

# First run downloads the model. For a college project, this is simple to demonstrate.
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def clean_text(text):
    text = re.sub(r"\s+", " ", text or "").strip()
    return text

def extract_file_text(file):
    filename = (file.filename or "").lower()

    if filename.endswith(".txt"):
        return file.read().decode("utf-8", errors="ignore")

    if filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if filename.endswith(".docx"):
        doc = Document(file)
        return "\n".join(p.text for p in doc.paragraphs)

    raise ValueError("Unsupported file. Please upload TXT, PDF, or DOCX.")

def split_sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]

def extract_key_points(text, count=5):
    """Simple frequency-based extractive key-point method."""
    sentences = split_sentences(text)
    if not sentences:
        return []

    words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())
    stopwords = {
        "the","and","that","this","with","from","have","were","their","there",
        "which","would","about","into","also","because","while","where","when",
        "what","your","they","them","then","than","been","will","shall","could",
        "should","these","those","more","some","such","very","only","over","under",
        "after","before","each","other","using","used","being","through","between"
    }
    freq = {}
    for w in words:
        if w not in stopwords:
            freq[w] = freq.get(w, 0) + 1

    scored = []
    for i, sentence in enumerate(sentences):
        sw = re.findall(r"\b[a-zA-Z]{3,}\b", sentence.lower())
        score = sum(freq.get(w, 0) for w in sw)
        scored.append((score, i, sentence))

    top = sorted(scored, reverse=True)[:count]
    top = sorted(top, key=lambda x: x[1])
    return [s for _, _, s in top]

def generate_summary(text, target="medium"):
    text = clean_text(text)
    if len(text.split()) < 30:
        return text

    word_count = len(text.split())
    if target == "short":
        max_len = min(90, max(35, word_count // 4))
        min_len = min(35, max_len - 5)
    elif target == "long":
        max_len = min(220, max(80, word_count // 2))
        min_len = min(80, max_len - 10)
    else:
        max_len = min(150, max(60, word_count // 3))
        min_len = min(55, max_len - 10)

    # BART works best when input is chunked for longer documents.
    chunks = []
    words = text.split()
    chunk_size = 450
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))

    summaries = []
    for chunk in chunks[:8]:  # practical limit for a student demo
        if len(chunk.split()) < 30:
            continue
        result = summarizer(
            chunk,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )
        summaries.append(result[0]["summary_text"])

    return " ".join(summaries)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        text = clean_text(request.form.get("text", ""))
        uploaded = request.files.get("file")

        if uploaded and uploaded.filename:
            text = clean_text(extract_file_text(uploaded))

        if not text:
            return jsonify({"error": "Please enter text or upload a TXT, PDF, or DOCX file."}), 400

        length = request.form.get("length", "medium")
        summary = generate_summary(text, length)
        key_points = extract_key_points(text, 5)

        return jsonify({
            "original": text,
            "summary": summary,
            "key_points": key_points,
            "original_words": len(text.split()),
            "summary_words": len(summary.split())
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
