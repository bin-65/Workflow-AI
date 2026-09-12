import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Workflow AI", page_icon="⚙️", layout="wide")

# Custom CSS matching the blue/teal theme from your interface image
st.markdown("""
    <style>
    .main-header { font-size:2.2rem; font-weight:700; color:#1E3A8A; }
    .sub-header { font-size:1.1rem; color:#475569; }
    .metric-card { background-color:#F8FAFC; padding:18px; border-radius:10px; border:1px solid #E2E8F0; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-header'>⚙️ Workflow AI</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Intelligent Workplace Productivity Copilot — Turn workplace information into action.</div><br>", unsafe_allow_html=True)

# Top KPI Metrics (Matching Mockup)
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Documents Processed", "47", "↑ 12%")
col2.metric("Questions Answered", "126", "↑ 18%")
col3.metric("Actions Extracted", "83", "↑ 21%")
col4.metric("Reports Generated", "24", "↑ 9%")
col5.metric("Minutes Saved", "1,240", "↑ 32%")

st.divider()

col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("Productivity Overview")
    chart_data = pd.DataFrame({
        "Date": ["Sep 6", "Sep 7", "Sep 8", "Sep 9", "Sep 10", "Sep 11", "Sep 12"],
        "Documents Processed": [18, 22, 31, 28, 35, 38, 45],
        "Questions Answered": [10, 14, 21, 19, 23, 26, 33],
        "Actions Extracted": [5, 8, 14, 9, 13, 12, 22]
    })
    fig = px.line(chart_data, x="Date", y=["Documents Processed", "Questions Answered", "Actions Extracted"], markers=True)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Recent Documents")
    docs_df = pd.DataFrame([
        {"Name": "Maintenance_Report.pdf", "Type": "PDF", "Size": "2.4 MB", "Status": "Ready", "Uploaded": "2 hours ago"},
        {"Name": "Production_Data.xlsx", "Type": "XLSX", "Size": "1.8 MB", "Status": "Ready", "Uploaded": "4 hours ago"},
        {"Name": "Meeting_Notes.docx", "Type": "DOCX", "Size": "1.2 MB", "Status": "Ready", "Uploaded": "6 hours ago"},
    ])
    st.dataframe(docs_df, use_container_width=True)

with col_right:
    st.subheader("Quick Actions")
    if st.button("📤 Upload Documents", use_container_width=True):
        st.switch_page("pages/1_Document_Intelligence.py")
    if st.button("❓ Ask a Question", use_container_width=True):
        st.switch_page("pages/2_AI_Assistant.py")
    if st.button("🧩 Extract Tasks", use_container_width=True):
        st.switch_page("pages/3_Task_Extractor.py")
    if st.button("📄 Generate Report", use_container_width=True):
        st.switch_page("pages/5_Report_Generator.py")

    st.subheader("Actions by Priority")
    pie_df = pd.DataFrame({"Priority": ["High", "Medium", "Low"], "Count": [38, 41, 21]})
    fig_pie = px.pie(pie_df, values="Count", names="Priority", hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)
