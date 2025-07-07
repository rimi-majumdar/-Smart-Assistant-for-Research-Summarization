from backend.utils import query_llama_together
import re

def generate_challenges(content, api_key):
    prompt = f"""Create exactly 3 open-ended comprehension questions based on the document.
Do NOT add any introductory statements. Each question must be complete and have a question mark.

DOCUMENT:
{content[:3000]}
"""
    raw = query_llama_together(prompt, api_key)
    lines = [l.strip() for l in raw.split("\n") if l.strip()]
    cleaned = []
    for line in lines:
        line = re.sub(r'^[0-9]+[).\-]\s*', '', line).strip()
        if "?" in line and not line.lower().startswith(("here are", "below are", "following are")):
            cleaned.append(line)
        if len(cleaned) == 3:
            break
    return cleaned

def evaluate_answers(content, questions, answers, api_key):
    results = []
    for q, a in zip(questions, answers):
        if not a.strip():
            results.append("❗ This question is not answered. Please submit an answer to receive feedback.")
            continue
        prompt = f"""DOCUMENT:
{content[:3000]}

QUESTION: {q}
USER ANSWER: {a}

Evaluate the answer with reference to the document. Be honest and clear.
Then quote the most relevant sentence from the document that supports or refutes the answer.

Response format:
Feedback: <correct/incorrect + explanation>
Supporting Evidence: "<quote from the document>" (↪ Referencing sentence or paragraph)
"""
        results.append(query_llama_together(prompt, api_key))
    return results