from backend.utils import query_llama_together

def answer_question(content, question, api_key, history=None):
    history_prompt = ""
    if history:
        for q, a in history[-3:]:  # include last 3 exchanges
            history_prompt += f"Q: {q}\nA: {a}\n"

    prompt = f"""You are a research assistant. Use the document to answer the current user question.
If the user question is a follow-up, use the conversation history below to maintain context.
After answering, quote the most relevant sentence or paragraph from the document as justification.

DOCUMENT:
{content[:3000]}

{history_prompt}
USER QUESTION: {question}

Answer format:
A: <your answer>
Supporting Evidence: "<quote from the document>" (↪ Referencing sentence or paragraph)
"""

    full_response = query_llama_together(prompt, api_key)
    return full_response.strip()