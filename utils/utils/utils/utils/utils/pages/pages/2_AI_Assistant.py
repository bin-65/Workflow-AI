import streamlit as st
from utils.rag import ask_rag_question

st.title("💬 AI Workplace Assistant")

if "vectorstore" not in st.session_state:
    st.warning("Please upload a document under Document Intelligence first!")
else:
    query = st.text_input("Ask a question about your uploaded document:")
    if query:
        with st.spinner("Searching and generating response..."):
            answer, docs = ask_rag_question(st.session_state["vectorstore"], query)
            st.markdown("### Answer")
            st.write(answer)
            
            with st.expander("Retrieved Context & Sources"):
                for i, doc in enumerate(docs):
                    st.markdown(f"**Chunk {i+1}:**")
                    st.write(doc.page_content)
