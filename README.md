# 🧠 Smart Assistant for Research Summarization



🔗 Live App:https://smart-assistant-for-research.onrender.com/


📌 Objective


This project builds a document-aware AI assistant capable of:

Answering comprehension and inference-based questions from uploaded documents.

Generating logic-based challenges and evaluating responses.

Justifying all answers using direct references from the document.

🧩 Problem Statement


Traditional tools often fall short in understanding complex documents such as research papers and technical manuals. This assistant addresses that gap with contextual reasoning and content-based responses.

Capabilities include:

Understanding long-form .pdf or .txt documents.

Handling free-form Q&A and logic-based challenges.

Citing references from the uploaded material.

🚀 Features


✅ Document Upload
Accepts .pdf and .txt formats.

Works with structured documents like reports and research papers.

✅ Interaction Modes

🔹 Ask Anything

— Free-form Q&A grounded in document content with reference-based answers.


🔹 Challenge Me

— Automatically generates 3 comprehension/logic questions.

— Evaluates user answers and provides feedback with justification.



✅ Contextual Understanding

— All answers are grounded in the actual content.

— Snippet-based referencing (e.g., “Paragraph 3 of Section 1”).

— Minimizes hallucination or irrelevant answers.



✅ Auto Summary

— Instant ≤150-word summary of the uploaded content.

✅ Architecture

Frontend: Streamlit-based interactive web interface.

Backend: Python modules (Flask-style structure).



🌟 Bonus Features (implemented)


✅ Memory Handling: Enables follow-up questions with historical context.


✅ Answer Highlighting: Justifies responses with cited snippets.





🏗 Setup Instructions



Clone the repository:


git clone https://github.com/rimi-majumdar/-Smart-Assistant-for-Research-Summarization.git



cd -Smart-Assistant-for-Research-Summarization


Install dependencies:

pip install -r requirements.txt


Run the app locally:

streamlit run main.py --server.port 10000 --server.address 0.0.0.0



🌐 Deployment (Render)


To deploy using Render:


Push the repository to GitHub.


Visit: https://render.com


Click “New → Web Service”


Configuration:

Build Command:

pip install -r requirements.txt

Start Command:

streamlit run main.py --server.port 10000 --server.address 0.0.0.0

Deploy and access your app online.




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

Smart-Assistant-for-Research-Summarization\
├── backend/ \
│   ├── challenge_generator.py\
│   ├── processor.py\
│   ├── qna_engine.py\
│   ├── summarizer.py\
│   └── utils.py\
├── frontend/\
│   ├── index.html\
│   ├── postcss.config.js\
│   ├── tailwind.config.js\
│   └── src/\
│       ├── app.js\
│       ├── index.cs\
│       └── index.js\
├── README.md\
├── rmain.py \
└── requirements.txt



📽 Demo


🎥 Click here to watch the demo






https://github.com/user-attachments/assets/bba6e86e-3141-47e5-91c0-6f6c644f9b45





🧾 Contact

Developed by Rimi Majumdar as part of the Data Science Internship Task.
