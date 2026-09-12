import streamlit as st
import pandas as pd
import plotly.express as px
import base64
import os

# Page Config
st.set_page_config(
    page_title="Workflow AI - Mechanical & Industrial Engineering Focused",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to convert image to base64 for direct CSS injection
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    return ""

banner_b64 = get_image_base64("assets/hero_banner.png")
logo_b64 = get_image_base64("assets/logo.png")

# CSS Styling matching the blue enterprise design layout
st.markdown(f"""
    <style>
    /* Background Page Styling */
    .stApp {{
        background-color: #F0F4F9;
    }}
    
    header, footer {{visibility: hidden;}}
    
    /* Dynamic Banner Background matching Industrial Graphic */
    .custom-hero-banner {{
        background: url('data:image/png;base64,{banner_b64}') no-repeat center center;
        background-size: cover;
        border-radius: 14px;
        padding: 40px 30px;
        color: white;
        min-height: 180px;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }}
    
    /* Fallback linear gradient if local image is loading */
    .hero-fallback {{
        background: linear-gradient(90deg, #1E3A8A 0%, #3B82F6 60%, #93C5FD 100%);
    }}

    .hero-title {{
        font-size: 2.6rem;
        font-weight: 800;
        margin: 0;
        color: #0F172A;
    }}
    
    .hero-subtitle {{
        font-size: 1.2rem;
        font-weight: 600;
        color: #2563EB;
        margin-top: 5px;
    }}

    .hero-tagline {{
        font-size: 1rem;
        color: #475569;
        margin-top: 4px;
    }}
    
    /* Floating Right Engineering Badge */
    .badge-tag {{
        position: absolute;
        right: 25px;
        bottom: 25px;
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(5px);
        color: #FFFFFF;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}

    /* Metric Cards Custom Styling */
    .kpi-card {{
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }}
    .kpi-title {{ font-size: 0.85rem; font-weight: 600; color: #64748B; }}
    .kpi-value {{ font-size: 1.8rem; font-weight: 800; color: #0F172A; margin: 6px 0; }}
    .kpi-delta {{ font-size: 0.8rem; font-weight: 600; color: #10B981; }}
    
    /* Quick Actions Button Styling */
    div.stButton > button {{
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        color: #1E293B;
        font-weight: 600;
        padding: 12px;
        text-align: left;
    }}
    div.stButton > button:hover {{
        border-color: #2563EB;
        background-color: #EFF6FF;
        color: #2563EB;
    }}
    </style>
""", unsafe_allow_html=True)

# Top Bar Header
top_c1, top_c2 = st.columns([4, 1])
with top_c1:
    st.text_input("Search documents, ask questions, or find actions...", label_visibility="collapsed", placeholder="🔍 Search documents, ask questions, or find actions...")
with top_c2:
    st.markdown("<div style='text-align: right; padding-top: 5px;'><b>JD</b> John Doe<br><small>Mechanical Engineer</small></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Main Visual Hero Banner (Industrial Engineering Graphic)
banner_class = "custom-hero-banner" if banner_b64 else "custom-hero-banner hero-fallback"
st.markdown(f"""
    <div class="{banner_class}">
        <div class="hero-title">⚙️ Workflow AI</div>
        <div class="hero-subtitle">Intelligent Workplace Productivity Copilot</div>
        <div class="hero-tagline">Turn workplace information into action.</div>
        <div class="badge-tag">Mechanical & Industrial Engineering Focused</div>
    </div>
""", unsafe_allow_html=True)

# Top 5 Metric Cards Row
m1, m2, m3, m4, m5 = st.columns(5)
with m1:
    st.markdown('<div class="kpi-card"><div class="kpi-title" style="color:#2563EB;">📄 Documents Processed</div><div class="kpi-value">47</div><div class="kpi-delta">↑ 12% vs last 7 days</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="kpi-card"><div class="kpi-title" style="color:#10B981;">💬 Questions Answered</div><div class="kpi-value">126</div><div class="kpi-delta">↑ 18% vs last 7 days</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="kpi-card"><div class="kpi-title" style="color:#8B5CF6;">📋 Actions Extracted</div><div class="kpi-value">83</div><div class="kpi-delta">↑ 21% vs last 7 days</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="kpi-card"><div class="kpi-title" style="color:#F59E0B;">📊 Reports Generated</div><div class="kpi-value">24</div><div class="kpi-delta">↑ 9% vs last 7 days</div></div>', unsafe_allow_html=True)
with m5:
    st.markdown('<div class="kpi-card"><div class="kpi-title" style="color:#06B6D4;">⏱️ Estimated Minutes Saved</div><div class="kpi-value">1,240</div><div class="kpi-delta">↑ 32% vs last 7 days</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Charts & Main Content Section
left_body, right_body = st.columns([2.3, 1])

with left_body:
    st.subheader("Productivity Overview")
    chart_data = pd.DataFrame({
        "Date": ["Sep 6", "Sep 7", "Sep 8", "Sep 9", "Sep 10", "Sep 11", "Sep 12"],
        "Documents Processed": [18, 22, 31, 28, 35, 38, 45],
        "Questions Answered": [10, 14, 21, 19, 23, 26, 33],
        "Actions Extracted": [5, 8, 14, 9, 13, 12, 22]
    })
    
    fig = px.line(chart_data, x="Date", y=["Documents Processed", "Questions Answered", "Actions Extracted"], markers=True, color_discrete_sequence=["#2563EB", "#10B981", "#8B5CF6"])
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
    if st.button("📤  Upload Documents", use_container_width=True): st.switch_page("pages/1_Document_Intelligence.py")
    if st.button("💬  Ask a Question", use_container_width=True): st.switch_page("pages/2_AI_Assistant.py")
    if st.button("🧩  Extract Tasks", use_container_width=True): st.switch_page("pages/3_Task_Extractor.py")
    if st.button("📄  Generate Report", use_container_width=True): st.switch_page("pages/5_Report_Generator.py")
    if st.button("📊  Analyze Spreadsheet", use_container_width=True): st.switch_page("pages/1_Document_Intelligence.py")

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Actions by Priority")
    pie_df = pd.DataFrame({"Priority": ["High", "Medium", "Low"], "Count": [38, 41, 21]})
    fig_pie = px.pie(pie_df, values="Count", names="Priority", hole=0.55, color_discrete_sequence=["#EF4444", "#F59E0B", "#10B981"])
    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_pie, use_container_width=True)
