import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="Workflow AI - Intelligent Workplace Productivity Copilot",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Injections
st.markdown("""
    <style>
    .stApp {
        background-color: #F8FAFC;
    }
    
    header, footer { visibility: hidden; }

    /* Top Search Bar Row */
    .top-search-row {
        margin-bottom: 10px;
    }

    /* Main Light Blue Hero Banner Layout */
    .hero-banner-container {
        width: 100%;
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid #BFDBFE;
        background: linear-gradient(90deg, #EBF5FF 0%, #E0F2FE 40%, #DBEAFE 65%, #93C5FD 100%);
        position: relative;
        min-height: 230px;
        display: flex;
        align-items: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.05);
    }

    .hero-text-content {
        padding: 30px 40px;
        width: 50%;
        z-index: 2;
    }

    .hero-brand-title {
        font-size: 2.7rem;
        font-weight: 800;
        color: #1E3A8A;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .hero-brand-title span {
        color: #2563EB;
    }

    .hero-subtitle {
        color: #1D4ED8;
        font-size: 1.15rem;
        font-weight: 700;
        margin-top: 6px;
    }

    .hero-description {
        color: #475569;
        font-size: 0.95rem;
        margin-top: 4px;
    }

    /* Big Engineer Image Right Top Side */
    .hero-engineer-img {
        position: absolute;
        right: 0;
        top: 0;
        bottom: 0;
        height: 100%;
        width: 52%;
        object-fit: cover;
        z-index: 1;
        mask-image: linear-gradient(to left, rgba(0,0,0,1) 75%, rgba(0,0,0,0) 100%);
        -webkit-mask-image: linear-gradient(to left, rgba(0,0,0,1) 75%, rgba(0,0,0,0) 100%);
    }

    .engineering-badge-floating {
        position: absolute;
        right: 25px;
        bottom: 20px;
        z-index: 3;
        background: rgba(15, 23, 42, 0.70);
        color: #FFFFFF;
        padding: 8px 18px;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255,255,255,0.2);
    }

    /* Metric Cards Styling */
    .kpi-card-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }
    
    /* Quick Actions Button Styling */
    div.stButton > button {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        color: #1E293B;
        font-weight: 600;
        padding: 10px 14px;
        text-align: left;
        width: 100%;
    }
    div.stButton > button:hover {
        border-color: #2563EB;
        background-color: #EFF6FF;
        color: #2563EB;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Search Bar
st.text_input("Search", label_visibility="collapsed", placeholder="🔍 Search documents, ask questions, or find actions...")
st.markdown("<br>", unsafe_allow_html=True)

# 4. Hero Banner (Light Blue Background + Large Engineer Image on Right Side)
st.markdown("""
    <div class="hero-banner-container">
        <div class="hero-text-content">
            <div class="hero-brand-title">
                ⚙️ Workflow <span>AI</span>
            </div>
            <div class="hero-subtitle">Intelligent Workplace Productivity Copilot</div>
            <div class="hero-description">Turn workplace information into action.</div>
        </div>
        <img class="hero-engineer-img" src="https://images.unsplash.com/photo-1581092335397-9583fe92d232?q=80&w=1400&auto=format&fit=crop" alt="Industrial Engineer">
        <div class="engineering-badge-floating">
            Mechanical & Industrial Engineering Focused
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. Metric KPI Cards Row
m1, m2, m3, m4, m5 = st.columns(5)
with m1:
    st.markdown('<div class="kpi-card-box"><div style="color:#2563EB; font-weight:600; font-size:0.85rem;">📄 Documents Processed</div><div style="font-size:1.8rem; font-weight:800; color:#0F172A; margin:4px 0;">47</div><div style="color:#10B981; font-size:0.8rem; font-weight:600;">↑ 12% <span style="color:#94A3B8;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="kpi-card-box"><div style="color:#10B981; font-weight:600; font-size:0.85rem;">💬 Questions Answered</div><div style="font-size:1.8rem; font-weight:800; color:#0F172A; margin:4px 0;">126</div><div style="color:#10B981; font-size:0.8rem; font-weight:600;">↑ 18% <span style="color:#94A3B8;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="kpi-card-box"><div style="color:#8B5CF6; font-weight:600; font-size:0.85rem;">📋 Actions Extracted</div><div style="font-size:1.8rem; font-weight:800; color:#0F172A; margin:4px 0;">83</div><div style="color:#10B981; font-size:0.8rem; font-weight:600;">↑ 21% <span style="color:#94A3B8;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="kpi-card-box"><div style="color:#F59E0B; font-weight:600; font-size:0.85rem;">📊 Reports Generated</div><div style="font-size:1.8rem; font-weight:800; color:#0F172A; margin:4px 0;">24</div><div style="color:#10B981; font-size:0.8rem; font-weight:600;">↑ 9% <span style="color:#94A3B8;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)
with m5:
    st.markdown('<div class="kpi-card-box"><div style="color:#06B6D4; font-weight:600; font-size:0.85rem;">⏱️ Estimated Minutes Saved</div><div style="font-size:1.8rem; font-weight:800; color:#0F172A; margin:4px 0;">1,240</div><div style="color:#10B981; font-size:0.8rem; font-weight:600;">↑ 32% <span style="color:#94A3B8;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Main Visual Grid Section
left_body, right_body = st.columns([2.3, 1])

with left_body:
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
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='white', margin=dict(l=10, r=10, t=10, b=10))
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

with right_body:
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
    pie_df = pd.DataFrame({"Priority": ["High", "Medium", "Low"], "Count": [38, 41, 21]})
    fig_pie = px.pie(
        pie_df, 
        values="Count", 
        names="Priority", 
        hole=0.55, 
        color_discrete_sequence=["#EF4444", "#F59E0B", "#10B981"]
    )
    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_pie, use_container_width=True)
