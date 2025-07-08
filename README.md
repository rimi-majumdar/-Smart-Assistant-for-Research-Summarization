# 🧠 Smart Assistant for Research Summarization

## 📌 Objective

This project aims to simulate a document-aware **AI assistant** that can:
- Answer comprehension and inference-based questions from user-uploaded documents.
- Generate logic-based questions and evaluate user responses.
- Justify every answer with a direct reference from the document.

---

## 🧩 Problem Statement

Traditional tools fail to deeply understand complex documents like research papers or technical manuals. This assistant is designed to go beyond keyword searches and provide **contextual understanding**, **reasoning**, and **justified responses**.

The assistant can:
- Read and understand long PDF/TXT documents.
- Support free-form Q&A and logic-based questions.
- Provide contextual references from the uploaded content.

---

## 🚀 Features

### ✅ 1. Document Upload
- Supports `.pdf` and `.txt` formats.
- Accepts structured English documents such as reports and research papers.

### ✅ 2. Interaction Modes

#### 🔹 a. Ask Anything
- Users can ask **free-form questions** based on the uploaded document.
- The assistant answers with **contextual understanding** and direct references.

#### 🔹 b. Challenge Me
- Automatically generates **3 logic/comprehension-based questions**.
- Users attempt to answer them.
- The assistant evaluates the responses and provides **feedback with justification**.

### ✅ 3. Contextual Understanding
- All responses are **grounded in actual document content**.
- Each answer includes a snippet reference, e.g., “*Paragraph 3 of Section 1*”.
- Avoids hallucinations or fabrications.

### ✅ 4. Auto Summary
- Instantly generates a **≤150-word summary** of the uploaded document.

### ✅ 5. Application Architecture
- **Frontend**: Built using [Streamlit](https://streamlit.io/) for a simple, interactive web interface.
- **Backend**: Powered by Python (Flask-based logic modules).

---

## 🌟 Bonus Features (Implemented)

- ✅ **Memory Handling**: Handles follow-up questions using prior context.
- ✅ **Answer Highlighting**: Highlights **document snippets** that justify each answer.

---

## 🏗️ Architecture / Reasoning Flow

```mermaid
graph TD
    A[User Uploads PDF/TXT] --> B[Document Preprocessing & Summarization]
    B --> C{Choose Mode}
    C --> D[Ask Anything: User types a question]
    C --> E[Challenge Me: System generates logic-based questions]
    D --> F[LLM processes user question + context]
    E --> G[LLM generates 3 questions]
    G --> H[User submits answers]
    H --> I[Assistant evaluates and gives feedback with justification]
    F --> J[Answer with snippet + justification]



## 🏗 Setup Instructions

1. Clone the repo:

bash
git clone https://github.com/rimi-majumdar/-Smart-Assistant-for-Research-Summarization.git
cd -Smart-Assistant-for-Research-Summarization


2. Install dependencies:

bash
pip install -r requirements.txt


3. Run the app locally:

bash
streamlit run main.py --server.port 10000 --server.address 0.0.0.0


---

## 🚀 Deployment on Render

1. Push this repo to GitHub
2. Go to [https://render.com](https://render.com)
3. Click "New → Web Service"
4. Use:

   * Build Command: pip install -r requirements.txt
   * Start Command: streamlit run main.py --server.port 10000 --server.address 0.0.0.0
5. Wait for deployment and open your URL

---


📂 Folder Structure
bash
Copy
Edit
Smart-Assistant-for-Research-Summarization/
│
├── app.py                    # Streamlit main entry point
├── backend/                  # Core logic
│   ├── qa_engine.py          # Handles Q&A and challenge logic
│   ├── summarizer.py         # Summarization module
│   └── memory_handler.py     # Memory support for follow-ups
│
├── utils/
│   └── pdf_reader.py         # Extract text from PDF/TXT
│
├── requirements.txt
└── README.md
📽️ Demo
🎥 Click here to watch the demo
(Add link when available)

🙌 Author
Rimi Majumdar
🔗 GitHub Profile

