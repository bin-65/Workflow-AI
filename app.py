import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Workflow AI - Intelligent Workplace Productivity Copilot",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling matching the mock dashboard
st.markdown("""
    <style>
    .main-header { font-size: 2.2rem; font-weight: 700; color: #1E3A8A; margin-bottom: 0px; }
    .sub-header { font-size: 1.05rem; color: #475569; margin-bottom: 20px; }
    .card-title { font-size: 0.9rem; font-weight: 600; color: #64748B; }
    </style>
""", unsafe_allow_html=True)

# Application Header
st.markdown("<div class='main-header'>⚙️ Workflow AI</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Intelligent Workplace Productivity Copilot — Turn workplace information into action.</div>", unsafe_allow_html=True)

# Top KPI Metric Cards
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Documents Processed", "47", "↑ 12%")
col2.metric("Questions Answered", "126", "↑ 18%")
col3.metric("Actions Extracted", "83", "↑ 21%")
col4.metric("Reports Generated", "24", "↑ 9%")
col5.metric("Minutes Saved", "1,240", "↑ 32%")

st.divider()

# Main Body Grid
col_left, col_right = st.columns([2.2, 1])

with col_left:
    # Productivity Overview Analytics Chart
    st.subheader("Productivity Overview")
    chart_data = pd.DataFrame({
        "Date": ["Sep 6", "Sep 7", "Sep 8", "Sep 9", "Sep 10", "Sep 11", "Sep 12"],
        "Documents Processed": [18, 22, 31, 28, 35, 38, 45],
        "Questions Answered": [10, 14, 21, 19, 23, 26, 33],
        "Actions Extracted": [5, 8, 14, 9, 13, 12, 22]
    })
    
    fig = px.line(
        chart_data, 
        x="Date", 
        y=["Documents Processed", "Questions Answered", "Actions Extracted"],
        markers=True,
        color_discrete_sequence=["#2563EB", "#059669", "#7C3AED"]
    )
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), legend_title_text="")
    st.plotly_chart(fig, use_container_width=True)

    # Recent Documents Table
    st.subheader("Recent Documents")
    docs_data = [
        {"Name": "Maintenance_Report.pdf", "Type": "PDF", "Size": "2.4 MB", "Status": "Ready", "Uploaded": "2 hours ago"},
        {"Name": "Production_Data.xlsx", "Type": "XLSX", "Size": "1.8 MB", "Status": "Ready", "Uploaded": "4 hours ago"},
        {"Name": "Meeting_Notes.docx", "Type": "DOCX", "Size": "1.2 MB", "Status": "Ready", "Uploaded": "6 hours ago"},
        {"Name": "Inspection_Report.pdf", "Type": "PDF", "Size": "3.1 MB", "Status": "Processing", "Uploaded": "7 hours ago"},
        {"Name": "Team_Updates.csv", "Type": "CSV", "Size": "0.9 MB", "Status": "Ready", "Uploaded": "8 hours ago"},
    ]
    st.dataframe(pd.DataFrame(docs_data), use_container_width=True)

with col_right:
    # Quick Action Buttons linked directly to pages/ modules
    st.subheader("Quick Actions")
    if st.button("📤 Upload Documents", use_container_width=True):
        st.switch_page("pages/1_Document_Intelligence.py")
        
    if st.button("❓ Ask a Question", use_container_width=True):
        st.switch_page("pages/2_AI_Assistant.py")
        
    if st.button("🧩 Extract Tasks", use_container_width=True):
        st.switch_page("pages/3_Task_Extractor.py")
        
    if st.button("📄 Generate Report", use_container_width=True):
        st.switch_page("pages/5_Report_Generator.py")

    st.markdown("<br>", unsafe_allow_html=True)

    # Actions by Priority Donut Chart
    st.subheader("Actions by Priority")
    pie_df = pd.DataFrame({
        "Priority": ["High", "Medium", "Low"],
        "Count": [38, 41, 21]
    })
    fig_pie = px.pie(
        pie_df, 
        values="Count", 
        names="Priority", 
        hole=0.5,
        color_discrete_sequence=["#EF4444", "#F59E0B", "#10B981"]
    )
    fig_pie.update_layout(margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_pie, use_container_width=True)
