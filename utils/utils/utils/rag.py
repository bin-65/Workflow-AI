from langchain.chains import RetrievalQA
from utils.groq_client import get_groq_llm

def ask_rag_question(vectorstore, query):
    llm = get_groq_llm()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    
    docs = retriever.get_relevant_documents(query)
    context = "\n\n".join([d.page_content for d in docs])
    
    prompt = f"Answer the following question based ONLY on the context below. Include relevant quotes/sources.\n\nContext:\n{context}\n\nQuestion: {query}"
    response = llm.invoke(prompt)
    
    return response.content, docs
