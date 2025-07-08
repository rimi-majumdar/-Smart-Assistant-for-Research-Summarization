# Smart Assistant for Research Summarization 

An intelligent research assistant that helps researchers upload papers, get concise summaries, ask context-aware questions, and even test their understanding through custom-generated challenges.

🔗 Live App: [https://smart-assistant-for-research.onrender.com](https://smart-assistant-for-research.onrender.com)

---

## 🧠 Features

* 📄 Upload PDF or TXT research papers
* ✨ Automatic summary generation (max 150 words)
* 💬 Ask Anything mode:

  * Ask natural questions grounded in uploaded content
  * Uses semantic search + OpenAI to find answers

* 🎯 Challenge Me mode:

  * Automatically generates custom MCQs or open-ended questions
  * Evaluates and explains correctness of user answers

* 🧵 Memory Handling (Bonus):

 
  * Follow-up questions are answered using full conversational history

* 🔍 Answer Highlighting (Bonus):

  * Displays supporting document snippet for each answer

* ⚡ Streamlit UI with 2-mode toggle (Ask/Challenge)
* 🚀 Deployable on Render

---

## 🧱 Architecture Overview

1. 📂 Upload Document (PDF or TXT) via Streamlit
2. 📃 Document text is extracted using PyPDF2 and cleaned
3. 🧠 Summary is generated via backend/summarizer.py
4. 💬 In "Ask Anything" mode:

   * Question is routed to backend/qna\_engine.py
   * Uses embedding search + history-aware prompt to answer

5. 🎓 In "Challenge Me" mode:

   * Uses backend/challenge\_generator.py to make  questions
   * Evaluates user response and returns feedback



---

## 📁 Directory Structure

```
Smart-Assistant-for-Research-Summarization/
🔼 backend/
🔼 summarizer.py
🔼 qna_engine.py
🔼 challenge_generator.py
🔼 memory.py
🔼 memory.json
🔼 main.py
🔼 requirements.txt
🔼 .streamlit/
🔼 config.toml
🔼 README.md
```

---

## 🏗️ Setup Instructions

1. Clone the repo:

```bash
git clone https://github.com/rimi-majumdar/-Smart-Assistant-for-Research-Summarization.git
cd -Smart-Assistant-for-Research-Summarization
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app locally:

```bash
streamlit run main.py --server.port 10000 --server.address 0.0.0.0
```

---

## 🚀 Deployment on Render

1. Push this repo to GitHub
2. Go to [https://render.com](https://render.com)
3. Click "New → Web Service"
4. Use:

   * Build Command: `pip install -r requirements.txt`
   * Start Command: `streamlit run main.py --server.port 10000 --server.address 0.0.0.0`
5. Wait for deployment and open your URL

---

## ✅ Bonus Features Implemented

* 🧵 GPT-style Memory Handling
* 🧠 Follow-up questions answered using last 20 turns stored in memory.json
* 🔍 Answer Highlighting: displays document snippet supporting each answer

---

## 📽️ Optional: Demo Video (You can add later)

```
🎥 Demo: https://your-demo-link.com
```

---

## 📬 Contact

Developed by Rimi Majumdar as part of the GenAI Internship Task.
