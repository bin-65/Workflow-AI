import streamlit as st
from utils.groq_client import get_groq_llm

st.title("🧩 Action Center & Task Extractor")

if "doc_text" in st.session_state:
    if st.button("Extract Actionable Tasks"):
        llm = get_groq_llm()
        prompt = f"Extract all key tasks, assigned persons, priority, and deadlines from this text into a clean markdown table:\n\n{st.session_state['doc_text']}"
        res = llm.invoke(prompt)
        st.markdown(res.content)
else:
    st.info("Upload a document first to extract action items.")
