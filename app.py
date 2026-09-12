import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Config
st.set_page_config(
    page_title="Workflow AI - Mechanical & Industrial Engineering Focused",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inject CSS matching UI design
st.markdown("""
    <style>
    /* Global App Background */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Hide Streamlit default headers & footers */
    header, footer {visibility: hidden;}
    
    /* Top Banner Styling */
    .banner-container {
        background: linear-gradient(135deg, #E0F2FE 0%, #EFF6FF 50%, #DBEAFE 100%);
        border: 1px solid #BFDBFE;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .banner-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 4px;
    }
    
    .banner-subtitle {
        font-size: 1.05rem;
        color: #3B82F6;
        font-weight: 500;
        margin-bottom: 8px;
    }
    
    .banner-tagline {
        font-size: 0.95rem;
        color: #475569;
    }
    
    .engineering-badge {
        background-color: #1E40AF;
        color: #FFFFFF;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }

    /* Metric Cards Styling */
    .metric-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.05);
        text-align: left;
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #0F172A;
    }
    
    .metric-delta {
        font-size: 0.85rem;
        font-weight: 600;
        color: #10B981;
    }
    
    /* Quick Action Button Styling */
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        background-color: #FFFFFF;
        color: #1E293B;
        font-weight: 600;
        padding: 10px;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        border-color: #2563EB;
        background-color: #EFF6FF;
        color: #2563EB;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Search Header Bar & User Profile Top Navigation
top_col1, top_col2 = st.columns([4, 1])
with top_col1:
    st.text_input("🔍 Search documents, ask questions, or find actions...", label_visibility="collapsed")
with top_col2:
    st.markdown("<div style='text-align: right; font-weight: 600; color: #1E293B;'>⚙️ Mechanical Engineer</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 4. Custom Hero Banner (Matching Engineering Focused Graphic)
st.markdown("""
    <div class="banner-container">
        <div>
            <div class="banner-title">⚙️ Workflow AI</div>
            <div class="banner-subtitle">Intelligent Workplace Productivity Copilot</div>
            <div class="banner-tagline">Turn workplace information into action.</div>
        </div>
        <div class="engineering-badge">
            Mechanical & Industrial Engineering Focused
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. Top Metric Cards Row
m1, m2, m3, m4, m5 = st.columns(5)

with m1:
    st.markdown('<div class="metric-card"><div style="color:#2563EB;">📄 Documents Processed</div><div class="metric-value">47</div><div class="metric-delta">↑ 12% vs last 7 days</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="metric-card"><div style="color:#059669;">💬 Questions Answered</div><div class="metric-value">126</div><div class="metric-delta">↑ 18% vs last 7 days</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="metric-card"><div style="color:#7C3AED;">📋 Actions Extracted</div><div class="metric-value">83</div><div class="metric-delta">↑ 21% vs last 7 days</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="metric-card"><div style="color:#D97706;">📊 Reports Generated</div><div class="metric-value">24</div><div class="metric-delta">↑ 9% vs last 7 days</div></div>', unsafe_allow_html=True)
with m5:
    st.markdown('<div class="metric-card"><div style="color:#0891B2;">⏱️ Estimated Minutes Saved</div><div class="metric-value">1,240</div><div class="metric-delta">↑ 32% vs last 7 days</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Main Visual Grid
col_left, col_right = st.columns([2.3, 1])

with col_left:
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
        color_discrete_sequence=["#2563EB", "#10B981", "#8B5CF6"]
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='white',
        margin=dict(l=10, r=10, t=10, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig, use_container_width=True)

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
    st.subheader("Quick Actions")
    if st.button("📤  Upload Documents", use_container_width=True):
        st.switch_page("pages/1_Document_Intelligence.py")
        
    if st.button("💬  Ask a Question", use_container_width=True):
        st.switch_page("pages/2_AI_Assistant.py")
        
    if st.button("🧩  Extract Tasks", use_container_width=True):
        st.switch_page("pages/3_Task_Extractor.py")
        
    if st.button("📄  Generate Report", use_container_width=True):
        st.switch_page("pages/5_Report_Generator.py")
        
    if st.button("📊  Analyze Spreadsheet", use_container_width=True):
        st.switch_page("pages/1_Document_Intelligence.py")

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Actions by Priority")
    pie_df = pd.DataFrame({
        "Priority": ["High", "Medium", "Low"],
        "Count": [38, 41, 21]
    })
    fig_pie = px.pie(
        pie_df, 
        values="Count", 
        names="Priority", 
        hole=0.55,
        color_discrete_sequence=["#EF4444", "#F59E0B", "#10B981"]
    )
    fig_pie.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=10, b=10)
    )
    st.plotly_chart(fig_pie, use_container_width=True)
