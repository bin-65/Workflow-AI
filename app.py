import streamlit as st
import pandas as pd
import plotly.express as px
import base64
import os

# 1. Page Configuration & Theme Settings
st.set_page_config(
    page_title="Workflow AI - Intelligent Workplace Productivity Copilot",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to encode local images safely for HTML/CSS rendering
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    return ""

banner_b64 = get_image_base64("assets/hero_banner.png")
avatar_b64 = get_image_base64("assets/engineer_avatar.png")

# 2. Custom CSS Injections matching exact reference visual theme
st.markdown(f"""
    <style>
    /* Global Page Background */
    .stApp {{
        background-color: #F8FAFC;
    }}
    
    header, footer {{visibility: hidden;}}

    /* Header Profile & Badge Layout */
    .profile-badge-container {{
        display: flex;
        align-items: center;
        justify-content: flex-end;
        gap: 12px;
    }}
    
    .profile-avatar {{
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background-color: #2563EB;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.95rem;
        background-size: cover;
        background-position: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }}

    /* Main Brand & Hero Banner */
    .hero-banner-container {{
        width: 100%;
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid #BFDBFE;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        margin-bottom: 24px;
        background: linear-gradient(135deg, #E0F2FE 0%, #EFF6FF 40%, #DBEAFE 100%);
        position: relative;
    }}

    .hero-banner-img {{
        width: 100%;
        height: auto;
        display: block;
        max-height: 220px;
        object-fit: cover;
    }}

    .hero-fallback-layout {{
        padding: 30px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        min-height: 180px;
    }}

    .brand-title {{
        font-size: 2.4rem;
        font-weight: 800;
        color: #1E3A8A;
        margin: 0;
    }}
    
    .brand-title-ai {{
        color: #2563EB;
    }}

    .engineering-badge {{
        background: rgba(30, 58, 138, 0.85);
        color: #FFFFFF;
        padding: 10px 20px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
        backdrop-filter: blur(4px);
    }}

    /* Top KPI Metric Cards */
    .kpi-card-box {{
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }}
    
    /* Quick Action Button Overrides */
    div.stButton > button {{
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        color: #1E293B;
        font-weight: 600;
        padding: 10px 14px;
        text-align: left;
    }}
    div.stButton > button:hover {{
        border-color: #2563EB;
        background-color: #EFF6FF;
        color: #2563EB;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. Top Navigation Header (Search Bar + Engineer Profile Badge)
top_col1, top_col2 = st.columns([3.5, 1.2])

with top_col1:
    st.text_input("Search", label_visibility="collapsed", placeholder="🔍 Search documents, ask questions, or find actions...")

with top_col2:
    avatar_style = f"background-image: url('data:image/png;base64,{avatar_b64}');" if avatar_b64 else ""
    avatar_text = "" if avatar_b64 else "JD"
    st.markdown(f"""
        <div class="profile-badge-container">
            <span style="font-size: 1.2rem; cursor: pointer;">🔔</span>
            <div class="profile-avatar" style="{avatar_style}">{avatar_text}</div>
            <div style="line-height: 1.2;">
                <div style="font-weight: 700; color: #0F172A; font-size: 0.9rem;">John Doe</div>
                <div style="color: #64748B; font-size: 0.75rem;">Mechanical Engineer ▾</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 4. Hero Banner Graphic Rendering
if banner_b64:
    st.markdown(f"""
        <div class="hero-banner-container">
            <img src="data:image/png;base64,{banner_b64}" class="hero-banner-img" alt="Workflow AI Hero Banner">
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class="hero-banner-container">
            <div class="hero-fallback-layout">
                <div>
                    <div class="brand-title">⚙️ Workflow <span class="brand-title-ai">AI</span></div>
                    <div style="color: #2563EB; font-weight: 600; font-size: 1.1rem; margin-top: 4px;">Intelligent Workplace Productivity Copilot</div>
                    <div style="color: #475569; margin-top: 4px;">Turn workplace information into action.</div>
                </div>
                <div class="engineering-badge">
                    Mechanical & Industrial Engineering Focused
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# 5. Top Metric KPI Cards Row
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

# 6. Main Visual Grid Section (Analytics Line Chart + Table + Actions Sidebar)
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
