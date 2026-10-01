# 🤖 AI Text Summarizer

An AI-based text summarization application developed as a college assignment for the **BCA program**.

This project is based on **Problem 9 – AI Text Summarizer** and implements **Feature Set B** given in the assignment.

---

## 📌 Project Details

| Details | Information |
|---|---|
| Project Title | AI Text Summarizer |
| Problem Number | Problem 9 |
| Feature Set | Feature Set B |
| Project Type | AI-Based Application |
| Course | BCA |
| Domain | Artificial Intelligence / NLP |

---

## 🎯 Objective

The objective of this project is to develop an AI-based application that can summarize lengthy text or uploaded text files into a shorter and meaningful summary.

The application allows users to provide text or a file as input, generate a summary, control the summary length, and view important key points.

---

## ✨ Features

This project implements all the requirements specified under **Feature Set B**.

### 📝 1. Text/File Input

The application allows users to provide input in two ways:

- Enter or paste text directly
- Upload a text file

The system reads the provided content and uses it as input for summarization.

---

### 🤖 2. Generate Summary

The application processes the input text and generates a concise summary.

The purpose of the summary is to reduce lengthy content while retaining the important information.

---

### 📏 3. Adjustable Summary Length

Users can adjust the desired length of the generated summary.

The application can provide different summary lengths according to the user's requirement.

For example:

- Short
- Medium
- Long

This gives users control over how much information they want in the final summary.

---

### 🔑 4. Display Key Points

The application displays the important key points from the provided content.

This helps users quickly understand the main ideas without reading the complete original text.

---

## 🔄 Project Workflow

```text
        ┌──────────────────────┐
        │      User Input      │
        │   Text / Text File   │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │   Text Processing    │
        │       / NLP          │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Select Summary Length │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │   Generate Summary   │
        └──────────┬───────────┘
                   │
              ┌────┴────┐
              ▼         ▼
       ┌──────────┐ ┌────────────┐
       │ Summary  │ │ Key Points │
       └──────────┘ └────────────┘


---

🧠 How It Works

1. The user enters text or uploads a text file.


2. The application reads the input content.


3. The input text is processed using NLP/AI techniques.


4. The user selects the required summary length.


5. The system generates the summary.


6. Important key points are identified and displayed.


7. The user can read the generated summary and key points.




---

🛠️ Technologies Used

The project can be implemented using:

Python

Natural Language Processing (NLP)

HTML

CSS

JavaScript


AI/NLP Libraries

Add the libraries that are actually used in your project, for example:

NLTK

Transformers

Scikit-learn

PyTorch



---

📂 Project Structure

AI-Text-Summarizer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── uploads/
    └── .gitkeep

> Update this structure according to the actual files in your project.




---

⚙️ Installation

1. Clone the Repository

git clone https://github.com/YOUR-USERNAME/AI-Text-Summarizer.git

2. Open the Project Folder

cd AI-Text-Summarizer

3. Create a Virtual Environment

python -m venv venv

Activate the environment.

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate

4. Install Dependencies

pip install -r requirements.txt

5. Run the Application

python app.py

Open the local URL displayed in the terminal.


---

📋 Feature Set B Requirements

Requirement	Implementation

Text/File Input	✅ Implemented
Generate Summary	✅ Implemented
Adjustable Summary Length	✅ Implemented
Display Key Points	✅ Implemented



---

💻 How to Use

Step 1 — Provide Input

Enter text into the text box or upload a text file.

Step 2 — Select Summary Length

Choose the required summary length.

Step 3 — Generate Summary

Click the Generate Summary button.

Step 4 — View Results

The application displays:

Generated summary

Important key points



---

🎓 Academic Purpose

This project is developed as an academic assignment for a BCA course.

It demonstrates the practical use of:

Artificial Intelligence

Natural Language Processing

Text Processing

Automatic Text Summarization

Web Application Development



---

🚀 Future Scope

The application can be enhanced in the future with:

PDF file input

DOCX file input

Multiple language support

Summary download

Summary history

Word count comparison

Voice input

Text-to-speech

Advanced transformer-based summarization

User login and authentication



---

👩‍💻 Developer

Sayali Chavan

BCA Student


---

📜 License

This project is created for educational and academic purposes.
