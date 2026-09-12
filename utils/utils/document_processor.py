import pandas as pd
from pypdf import PdfReader
import docx

def parse_document(uploaded_file):
    text = ""
    file_type = uploaded_file.name.split(".")[-1].lower()
    
    if file_type == "pdf":
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text() or ""
            
    elif file_type == "docx":
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"
            
    elif file_type in ["csv", "xlsx", "xls"]:
        df = pd.read_csv(uploaded_file) if file_type == "csv" else pd.read_excel(uploaded_file)
        text = df.to_string()
        
    return text, file_type
