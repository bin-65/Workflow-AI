import streamlit as st
from utils.groq_client import get_groq_llm

st.title("✉️ Smart Communication Drafts")

comm_type = st.selectbox("Platform", ["Email", "WhatsApp Message"])
context = st.text_area("Key points to include in message:")

if st.button("Generate Draft"):
    llm = get_groq_llm()
    prompt = f"Draft a professional {comm_type} based on these key details:\n{context}"
    res = llm.invoke(prompt)
    st.write(res.content)
