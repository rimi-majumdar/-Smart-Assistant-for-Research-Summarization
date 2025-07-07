import streamlit as st
from backend.processor import extract_text_from_file
from backend.summarizer import generate_summary
from backend.qna_engine import answer_question
from backend.challenge_generator import generate_challenges, evaluate_answers

st.set_page_config(page_title="Smart Assistant GenAI", layout="wide")
st.title("📚 Smart Assistant for Research Summarization")

API_KEY = "tgp_v1_dM6JW4D9hN47uzNNphHj9q42OjinWLtCCvOAmRKY0SU"

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
if uploaded_file:
    with st.spinner("Reading document..."):
        content = extract_text_from_file(uploaded_file)
        st.session_state.content = content

    st.subheader("📄 Auto Summary")
    st.success(generate_summary(content, API_KEY))

    mode = st.radio("Mode", ["Ask Anything", "Challenge Me"])
    if mode == "Ask Anything":
        q = st.text_input("Ask a question about this document")
        if q:
            st.write(answer_question(content, q, API_KEY))
    else:
        if st.button("Generate 3 Questions"):
            qs = generate_challenges(content, API_KEY)
            st.session_state.qs = qs
            st.session_state.resp = [""] * len(qs)

        if "qs" in st.session_state:
            qs = st.session_state.qs
            if len(st.session_state.resp) != len(qs):
                st.session_state.resp = [""] * len(qs)

            for i, q in enumerate(qs):
                st.markdown(f"**Q{i+1}: {q}**")
                st.session_state.resp[i] = st.text_area(
                    f"Your answer to Q{i+1}", 
                    value=st.session_state.resp[i],
                    key=f"ans_{i}"
                )

            if st.button("Evaluate"):
                feedback = evaluate_answers(content, qs, st.session_state.resp, API_KEY)
                for i, fb in enumerate(feedback):
                    st.markdown(f"🧠 *Feedback Q{i+1}:* {fb}")