import os
import streamlit as st
from langchain_groq import ChatGroq

def get_groq_llm(model_name="llama-3.3-70b-versatile", temperature=0.2):
    api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("GROQ API Key is missing! Set it in Streamlit Secrets or .env file.")
        st.stop()
    return ChatGroq(groq_api_key=api_key, model_name=model_name, temperature=temperature)
