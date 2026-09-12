import streamlit as st
from utils.document_processor import parse_document
from utils.embeddings import create_vector_store

st.title("📄 Document Intelligence & RAG")

uploaded_file = st.file_uploader("Upload PDF, DOCX, XLSX, or CSV", type=["pdf", "docx", "xlsx", "csv"])

if uploaded_file:
    with st.spinner("Processing document & building vector store..."):
        text, file_type = parse_document(uploaded_file)
        vectorstore = create_vector_store(text)
        st.session_state["vectorstore"] = vectorstore
        st.session_state["doc_text"] = text
        st.success(f"Successfully processed `{uploaded_file.name}`!")

if "doc_text" in st.session_state:
    st.subheader("Document Preview")
    st.text_area("Content", st.session_state["doc_text"][:2000] + "...", height=200)
