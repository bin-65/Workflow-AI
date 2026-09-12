import streamlit as st
import pandas as pd
import plotly.express as px
import base64
import os

# 1. Page Configuration
st.set_page_config(
    page_title="Workflow AI - Intelligent Workplace Productivity Copilot",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Helper function to convert local image to Base64 (Guarantees render in Streamlit)
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

banner_b64 = get_image_base64("assets/hero_banner.jpg")

# 2. Custom Styling Matched to the New Image Theme
st.markdown("""
    <style>
    /* Global Background */
    .stApp {
        background-color: #F8FAFC;
    }
    
    header, footer { visibility: hidden; }

    /* Remove Top Spacing to push banner up */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
    }

    /* Hero Banner Container matching Image Colors */
    .hero-banner-box {
        width: 100%;
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid #BAE6FD;
        background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 45%, #7DD3FC 100%);
        position: relative;
        min-height: 240px;
        display: flex;
        align-items: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.08);
    }

    .hero-banner-content {
        padding: 35px 40px;
        width: 52%;
        z-index: 2;
    }

    /* Clear & Bold Typography */
    .hero-banner-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #0C4A6E;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 12px;
        letter-spacing: -0.5px;
    }

    .hero-banner-title span {
        color: #0284C7;
    }

    .hero-banner-subtitle {
        color: #0369A1;
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 8px;
    }

    .hero-banner-desc {
        color: #334155;
        font-size: 1rem;
        font-weight: 500;
        margin-top: 6px;
    }

    /* Big Image Fitting on Right Side */
    .hero-banner-img {
        position: absolute;
        right: 0;
        top: 0;
        bottom: 0;
        height: 100%;
        width: 50%;
        object-fit: cover;
        z-index: 1;
        mask-image: linear-gradient(to left, rgba(0,0,0,1) 80%, rgba(0,0,0,0) 100%);
        -webkit-mask-image: linear-gradient(to left, rgba(0,0,0,1) 80%, rgba(0,0,0,0) 100%);
    }

    .badge-tag {
        display: inline-block;
        background: #0284C7;
        color: #FFFFFF;
        font-weight: 700;
        font-size: 0.8rem;
        padding: 5px 14px;
        border-radius: 20px;
        margin-top: 12px;
        box-shadow: 0 2px 6px rgba(2, 132, 199, 0.25);
    }

    /* KPI Cards Styling */
    .kpi-card-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }
    
    /* Quick Action Buttons Styling */
    div.stButton > button {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        color: #0F172A;
        font-weight: 600;
        padding: 11px 16px;
        text-align: left;
        width: 100%;
    }
    div.stButton > button:hover {
        border-color: #0284C7;
        background-color: #F0F9FF;
        color: #0284C7;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Search Bar (Full Width Top)
st.text_input("Search", label_visibility="collapsed", placeholder="🔍 Search documents, ask questions, or find actions...")
st.markdown("<br>", unsafe_allow_html=True)

# 4. Hero Banner Section with Color Matching & Logo Integration
if banner_b64:
    st.markdown(f"""
        <div class="hero-banner-box">
            <div class="hero-banner-content">
                <div class="hero-banner-title">
                    ⚙️ Workflow <span>AI</span>
                </div>
                <div class="hero-banner-subtitle">Intelligent Workplace Productivity Copilot</div>
                <div class="hero-banner-desc">Turn workplace information into action.</div>
                <div class="badge-tag">⏱️ AI WORKFORCE READINESS</div>
            </div>
            <img src="data:image/jpeg;base64,{banner_b64}" class="hero-banner-img" alt="Engineer AI Workforce">
        </div>
    """, unsafe_allow_html=True)
else:
    # Online Fallback Image matching exact uploaded visual
    st.markdown("""
        <div class="hero-banner-box">
            <div class="hero-banner-content">
                <div class="hero-banner-title">
                    ⚙️ Workflow <span>AI</span>
                </div>
                <div class="hero-banner-subtitle">Intelligent Workplace Productivity Copilot</div>
                <div class="hero-banner-desc">Turn workplace information into action.</div>
                <div class="badge-tag">⏱️ AI WORKFORCE READINESS</div>
            </div>
            <img src="https://images.unsplash.com/photo-1581092335397-9583fe92d232?q=80&w=1400&auto=format&fit=crop" class="hero-banner-img" alt="Engineer AI Workforce">
        </div>
    """, unsafe_allow_html=True)

# 5. Top Metric KPI Cards Row
m1, m2, m3, m4, m5 = st.columns(5)
with m1:
    st.markdown('<div class="kpi-card-box"><div style="color:#0284C7; font-weight:700; font-size:0.85rem;">📄 Documents Processed</div><div style="font-size:1.8rem; font-weight:800; color:#0F172A; margin:4px 0;">47</div><div style="color:#10B981; font-size:0.8rem; font-weight:600;">↑ 12% <span style="color:#94A3B8;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="kpi-card-box"><div style="color:#10B981; font-weight:700; font-size:0.85rem;">💬 Questions Answered</div><div style="font-size:1.8rem; font-weight:800; color:#0F172A; margin:4px 0;">126</div><div style="color:#10B981; font-size:0.8rem; font-weight:600;">↑ 18% <span style="color:#94A3B8;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="kpi-card-box"><div style="color:#8B5CF6; font-weight:700; font-size:0.85rem;">📋 Actions Extracted</div><div style="font-size:1.8rem; font-weight:800; color:#0F172A; margin:4px 0;">83</div><div style="color:#10B981; font-size:0.8rem; font-weight:600;">↑ 21% <span style="color:#94A3B8;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="kpi-card-box"><div style="color:#F59E0B; font-weight:700; font-size:0.85rem;">📊 Reports Generated</div><div style="font-size:1.8rem; font-weight:800; color:#0F172A; margin:4px 0;">24</div><div style="color:#10B981; font-size:0.8rem; font-weight:600;">↑ 9% <span style="color:#94A3B8;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)
with m5:
    st.markdown('<div class="kpi-card-box"><div style="color:#06B6D4; font-weight:700; font-size:0.85rem;">⏱️ Estimated Minutes Saved</div><div style="font-size:1.8rem; font-weight:800; color:#0F172A; margin:4px 0;">1,240</div><div style="color:#10B981; font-size:0.8rem; font-weight:600;">↑ 32% <span style="color:#94A3B8;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)

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
        color_discrete_sequence=["#0284C7", "#10B981", "#8B5CF6"]
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
    if st.button("📤  Upload Documents", use_container_width=True): pass
    if st.button("💬  Ask a Question", use_container_width=True): pass
    if st.button("🧩  Extract Tasks", use_container_width=True): pass
    if st.button("📄  Generate Report", use_container_width=True): pass
    if st.button("📊  Analyze Spreadsheet", use_container_width=True): pass

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
