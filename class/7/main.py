import streamlit as st
from groq import generate_response
import re

def looks_incomplete(text: str) -> bool:
    if not text or len(text.strip()) < 10:
        return True
    t = text.strip()    
    if t.endswith(("**", "*", "-", "—", ":", ",", "(", "[", "{")):
        return True
    if re.search(r"\d+\.\s*\*\*$", t):
        return True
    if not re.search(r"[.!?]\s*$", t):  
        return True
    return False

def complete_answer(question: str, max_rounds: int = 2) -> str:
    base_prompt = (
        f"Answer clearly in bullet points with sub topics",
        f"Do not cut sentences fully, finish them with a correct complete point",
        f"Question {question}"
    )
    
    ans = generate_response(base_prompt, temperature=0.3, max_tokens=200)
    
    rounds = 0
    
    while rounds < max_rounds and looks_incomplete(ans):
        cont_prompt = (
            "Continue EXACTLY from where you stopped. "
            "Do NOT repeat earlier text. "
            "Finish the incomplete point and complete the answer.\n\n"
            f"Question: {question}\n\n"
            f"Answer so far:\n{ans}\n\nContinue:"
        )
        
        more = generate_response(cont_prompt, temperature=0.3, max_tokens=200)
        if not more or more.strip() in ans:
            break
        ans = (ans.rstrip() + "\n" + more.lstrip()).strip()
        rounds += 1
        
    return ans

def main():
    st.title("AI Teaching Assistant")
    st.write("Welcome! You can ask me anything about various subjects, and I'll provide an answer.")

    user_input = st.text_input("Enter your question here:")

    if user_input:
        st.write(f"**Your question:** {user_input}")
        response = complete_answer(user_input)
        st.write("**AI's answer:**")
        st.markdown(response)  
        st.info("Please enter a question to ask.")

if __name__ == "__main__":
    main()