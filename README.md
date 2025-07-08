# 🧠 Smart Assistant for Research Summarization
🔗 Live App: https://github.com/rimi-majumdar/-Smart-Assistant-for-Research-Summarization

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

## 🌐 Deployment (Render)

1. Push this repo to GitHub
2. Go to [https://render.com](https://render.com)
3. Click "New → Web Service"
4. Use:

   * Build Command: pip install -r requirements.txt
   * Start Command: streamlit run main.py --server.port 10000 --server.address 0.0.0.0
5. Wait for deployment and open your URL

---

🧠 Architecture Flow
📌 Interface Layer — Streamlit
→ Handles document upload, user input, output rendering.

📌 Processing Layer — backend/

processor.py — Extracts text from uploaded documents.

summarizer.py — Sends content to LLM for summarization.

qna_engine.py — Processes free-form Q&A.

challenge_generator.py — Creates and evaluates logic questions.

utils.py — Handles API calls to LLM.

📌 Model Layer — Together AI API
→ Uses LLaMA 3/8B for summarization, Q&A, and challenge evaluation.

🎯 Reasoning Flow
A. Ask Anything
User uploads → processor.py → user asks → qna_engine.py → LLM response with reference → Output

B. Challenge Me
User uploads → summarizer.py → challenge_generator.py → user answers → evaluate_answers() → feedback

C. Auto Summary
Document → summarizer.py → summary → Display

📂 Folder Structure
Smart-Assistant-for-Research-Summarization/
├── backend/
│   ├── challenge_generator.py
│   ├── processor.py
│   ├── qna_engine.py
│   ├── summarizer.py
│   └── utils.py
├── frontend/
│   ├── index.html
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   └── src/
│       ├── app.js
│       ├── index.cs
│       └── index.js
├── README.md
├── rmain.py 
├── requirements.txt


📽️ Demo
🎥 Click here to watch the demo


https://github.com/user-attachments/assets/5f4b7168-4a1c-4aa8-bb22-fc49ee3f73d8


## 🧾Contact
Developed by Rimi Majumdar as part of the Data Science Internship Task.

