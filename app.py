import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="Workflow AI - Intelligent Workplace Productivity Copilot",
    page_icon="⚙️",
    layout="wide"
)

# 2. Strict CSS Injection
st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    header, footer { visibility: hidden; }

    .block-container {
        padding-top: 1rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }

    /* Outer Wrapper Card */
    .banner-container {
        width: 100%;
        background-color: #FFFFFF;
        border-radius: 12px;
        border: 1px solid #CBD5E1;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        display: flex;
        overflow: hidden;
        min-height: 220px;
        margin-bottom: 25px;
    }

    /* Left Side Content */
    .banner-left-side {
        width: 52%;
        padding: 24px 28px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        background: #FFFFFF;
    }

    .banner-logo-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F2D6B;
        margin: 0;
        line-height: 1.1;
    }

    .banner-subtitle-text {
        font-size: 1.05rem;
        font-weight: 600;
        color: #2563EB;
        margin-top: 4px;
        margin-bottom: 4px;
    }

    .banner-tagline-text {
        font-size: 0.95rem;
        color: #475569;
        font-weight: 500;
        margin-bottom: 16px;
    }

    /* Bottom Feature Pills */
    .pills-container {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        align-items: center;
    }

    .pill {
        padding: 5px 12px;
        border-radius: 8px;
        font-size: 0.78rem;
        font-weight: 700;
        display: inline-block;
    }

    .pill-blue { background: #EFF6FF; color: #1D4ED8; }
    .pill-green { background: #ECFDF5; color: #047857; }
    .pill-purple { background: #F5F3FF; color: #6D28D9; }
    .pill-orange { background: #FFF7ED; color: #C2410C; }
    .pill-teal { background: #F0FDFA; color: #0F766E; }

    /* Right Side Banner Image Overlay */
    .banner-right-side {
        width: 48%;
        position: relative;
        background-size: cover;
        background-position: center;
        background-image: url('https://images.unsplash.com/photo-1581092335397-9583fe92d232?q=80&w=1200&auto=format&fit=crop');
    }

    .right-blue-overlay {
        position: absolute;
        right: 0;
        top: 0;
        bottom: 0;
        width: 55%;
        background: linear-gradient(135deg, rgba(2, 132, 199, 0.85) 0%, rgba(3, 105, 161, 0.95) 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #FFFFFF;
        font-weight: 700;
        font-size: 0.95rem;
        text-align: center;
        padding: 15px;
        clip-path: ellipse(120% 100% at 100% 50%);
    }

    .kpi-card-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }

    div.stButton > button {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        color: #0F172A;
        font-weight: 600;
        padding: 10px 14px;
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

# 3. Top Search Input
st.text_input("Search", label_visibility="collapsed", placeholder="🔍 Search documents, ask questions, or find actions...")
st.markdown("<br>", unsafe_allow_html=True)

# 4. Clean Single-Block Banner HTML Execution
html_banner = """
<div class="banner-container">
    <div class="banner-left-side">
        <h1 class="banner-logo-title">⚙️ Workflow AI</h1>
        <div class="banner-subtitle-text">Intelligent Workplace Productivity Copilot</div>
        <div class="banner-tagline-text">Turn workplace information into action.</div>
        <div class="pills-container">
            <span class="pill pill-blue">📄 Summarize Documents</span>
            <span class="pill pill-green">✍️ Extract Tasks & Deadlines</span>
            <span class="pill pill-purple">📄 Generate Reports</span>
            <span class="pill pill-orange">⌛ Create Communications</span>
            <span class="pill pill-teal">📑 Get Recommendations</span>
        </div>
    </div>
    <div class="banner-right-side">
        <div class="right-blue-overlay">
            Mechanical & Industrial<br>Engineering Focused
        </div>
    </div>
</div>
"""
st.markdown(html_banner, unsafe_allow_html=True)

# 5. Dashboard KPIs & Grid
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

left_body, right_body = st.columns([2.3, 1])

with left_body:
    st.subheader("Productivity Overview")
    chart_data = pd.DataFrame({
        "Date": ["Sep 6", "Sep 7", "Sep 8", "Sep 9", "Sep 10", "Sep 11", "Sep 12"],
        "Documents Processed": [18, 22, 31, 28, 35, 38, 45],
        "Questions Answered": [10, 14, 21, 19, 23, 26, 33],
        "Actions Extracted": [5, 8, 14, 9, 13, 12, 22]
    })
    
    fig = px.line(chart_data, x="Date", y=["Documents Processed", "Questions Answered", "Actions Extracted"], markers=True, color_discrete_sequence=["#0284C7", "#10B981", "#8B5CF6"])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='white', margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Recent Documents")
    docs_data = [
        {"Name": "Maintenance_Report.pdf", "Type": "PDF", "Size": "2.4 MB", "Status": "Ready", "Uploaded": "2 hours ago"},
        {"Name": "Production_Data.xlsx", "Type": "XLSX", "Size": "1.8 MB", "Status": "Ready", "Uploaded": "4 hours ago"},
        {"Name": "Meeting_Notes.docx", "Type": "DOCX", "Size": "1.2 MB", "Status": "Ready", "Uploaded": "6 hours ago"},
    ]
    st.dataframe(pd.DataFrame(docs_data), use_container_width=True)

with right_body:
    st.subheader("Quick Actions")
    st.button("📤 Upload Documents", use_container_width=True)
    st.button("💬 Ask a Question", use_container_width=True)
    st.button("🧩 Extract Tasks", use_container_width=True)
    st.button("📄 Generate Report", use_container_width=True)
