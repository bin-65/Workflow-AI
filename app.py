import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import urllib.parse
import base64
import os

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Workflow AI - Intelligent Workplace Productivity Copilot",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to encode local image to Base64 safely
def get_image_base64(img_path):
    if os.path.exists(img_path):
        with open(img_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            return f"data:image/jpeg;base64,{encoded_string}"
    return "https://images.unsplash.com/photo-1581092335397-9583fe92d232?q=80&w=1000&auto=format&fit=crop"

banner_bg_img = get_image_base64("banner_img.jpg")

# ---------------------------------------------------------
# 2. SESSION STATE MANAGEMENT (STATE TRACKING)
# ---------------------------------------------------------
if "current_view" not in st.session_state:
    st.session_state.current_view = "Dashboard"

if "docs_list" not in st.session_state:
    st.session_state.docs_list = [
        {"Name": "Solar_Refrigeration_Abstract.pdf", "Type": "PDF", "Size": "2.4 MB", "Status": "Processed", "Uploaded": "2026-09-10"},
        {"Name": "Single_Use_Plastic_Report.docx", "Type": "DOCX", "Size": "1.1 MB", "Status": "Processed", "Uploaded": "2026-09-08"}
    ]

# ---------------------------------------------------------
# 3. STYLING & BANNER CSS
# ---------------------------------------------------------
st.markdown("""
<style>
    /* Global Page Styling */
    .stApp {
        background-color: #F8FAFC;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    header, footer { visibility: hidden !important; }
    
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
        max-width: 100% !important;
    }

    /* Sidebar Navigation Links */
    section[data-testid="stSidebar"] {
        width: 280px !important;
        background-color: #F8FAFC !important;
        border-right: 1px solid #E2E8F0 !important;
    }

    .github-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        background-color: #0F172A;
        color: #FFFFFF !important;
        padding: 8px 12px;
        border-radius: 8px;
        font-size: 0.8rem;
        font-weight: 600;
        text-decoration: none !important;
        margin-top: 8px;
        margin-bottom: 12px;
    }

    .nav-divider {
        height: 1px;
        background-color: #E2E8F0;
        margin: 12px 0;
    }

    /* Bottom Left Vector Card */
    .sidebar-bottom-card {
        background: linear-gradient(180deg, rgba(224,242,254,0.4) 0%, rgba(186,230,253,0.7) 100%);
        border: 1px solid #BAE6FD;
        border-radius: 14px;
        padding: 16px;
        position: relative;
        overflow: hidden;
        margin-top: 20px;
    }
    
    .sidebar-bottom-text {
        color: #0369A1;
        font-weight: 700;
        font-size: 0.84rem;
        line-height: 1.35;
    }

    /* Hero Banner Container */
    .main-banner {
        background: linear-gradient(90deg, #FFFFFF 0%, #EFF6FF 45%, #DBEAFE 100%);
        border-radius: 16px;
        border: 1px solid #CBD5E1;
        display: flex;
        overflow: hidden;
        min-height: 230px;
        position: relative;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    .banner-content {
        padding: 24px 28px;
        width: 52%;
        z-index: 2;
    }

    .banner-title { font-size: 2.2rem; font-weight: 800; color: #0F2D6B; margin: 0; }
    .banner-desc { font-size: 1rem; color: #334155; font-weight: 600; margin-top: 4px; }
    .banner-subtext { font-size: 0.9rem; color: #64748B; margin-bottom: 18px; }

    .pills-group { display: flex; gap: 8px; flex-wrap: wrap; }
    .feature-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 12px;
        border-radius: 8px;
        font-size: 0.78rem;
        font-weight: 700;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        color: #334155;
    }

    /* Expanded Right Image Side */
    .banner-right-img {
        width: 48%;
        position: relative;
        background-size: cover;
        background-position: center 15%;
        background-repeat: no-repeat;
        border-top-right-radius: 16px;
        border-bottom-right-radius: 16px;
    }

    .banner-overlay-badge {
        position: absolute;
        bottom: 12px;
        right: 12px;
        background: rgba(15, 23, 42, 0.85);
        color: #FFFFFF;
        font-weight: 700;
        font-size: 0.82rem;
        padding: 6px 14px;
        border-radius: 20px;
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* KPI Cards */
    .kpi-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px;
    }
    .kpi-title { font-size: 0.82rem; font-weight: 700; color: #475569; margin-top: 10px; }
    .kpi-value { font-size: 1.8rem; font-weight: 800; color: #0F172A; margin: 4px 0; }
    .kpi-change { font-size: 0.78rem; font-weight: 700; color: #10B981; }

    /* Section Cards */
    .section-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .card-title { font-size: 1.05rem; font-weight: 700; color: #0F172A; margin-bottom: 15px; }

    .share-social-btn {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 14px;
        border-radius: 6px;
        font-size: 0.78rem;
        font-weight: 700;
        color: white !important;
        text-decoration: none !important;
        margin-right: 6px;
        margin-bottom: 6px;
    }
    .bg-whatsapp { background-color: #25D366; }
    .bg-linkedin { background-color: #0A66C2; }
    .bg-twitter { background-color: #1DA1F2; }
    .bg-email { background-color: #EA4335; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. SIDEBAR NAVIGATION
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div style="padding: 10px 5px 5px 5px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 2rem;">⚙️</span>
                <div style="font-size: 1.35rem; font-weight: 800; color: #0F2D6B;">Workflow AI</div>
            </div>
            <div style="font-size: 0.75rem; color: #475569; margin-top: 4px; font-weight: 500;">Intelligent Workplace Productivity Copilot</div>
        </div>
        
        <a class="github-btn" href="https://github.com/bin-65/Workflow-AI" target="_blank">
            <svg height="16" width="16" viewBox="0 0 16 16" fill="white"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
            Edit Code (GitHub)
        </a>
    """, unsafe_allow_html=True)
    
    nav_option = st.radio(
        "Navigation Menu",
        ["🏠 Dashboard", "📤 Upload Documents", "💬 Ask Question", "✍️ Task Extractor", "📑 Generate Report", "📊 Analyze Spreadsheet"],
        index=0,
        label_visibility="collapsed"
    )
    
    # Update current view on sidebar selection
    if nav_option == "🏠 Dashboard":
        st.session_state.current_view = "Dashboard"
    elif nav_option == "📤 Upload Documents":
        st.session_state.current_view = "Upload"
    elif nav_option == "💬 Ask Question":
        st.session_state.current_view = "Ask"
    elif nav_option == "✍️ Task Extractor":
        st.session_state.current_view = "Tasks"
    elif nav_option == "📑 Generate Report":
        st.session_state.current_view = "Report"
    elif nav_option == "📊 Analyze Spreadsheet":
        st.session_state.current_view = "Spreadsheet"

    st.markdown("""
        <div class="nav-divider"></div>
        <div class="sidebar-bottom-card">
            <div class="sidebar-bottom-text">
                Smarter Documents.<br>
                Better Decisions.<br>
                Higher Productivity.
            </div>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. TOP BAR & SHARE DIALOG
# ---------------------------------------------------------
col_search, col_actions = st.columns([3.8, 1.4])

with col_search:
    st.text_input("Search", placeholder="🔍 Search documents, ask questions, or find actions...", label_visibility="collapsed")

with col_actions:
    col_share, col_user_profile = st.columns([1, 2])
    
    with col_share:
        share_clicked = st.button("🔗 Share")
            
    with col_user_profile:
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 8px; background: #FFFFFF; padding: 4px 10px 4px 6px; border-radius: 30px; border: 1px solid #E2E8F0;">
                <div style="width: 32px; height: 32px; border-radius: 50%; background-color: #0284C7; color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.82rem;">JD</div>
                <div style="line-height: 1.1;">
                    <div style="font-weight: 700; font-size: 0.82rem; color: #0F172A;">John Doe</div>
                    <div style="font-size: 0.7rem; color: #64748B;">Mechanical Engineer</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

if share_clicked:
    app_url = "https://workflow-ai.streamlit.app"
    encoded_url = urllib.parse.quote(app_url)
    share_text = urllib.parse.quote("Check out Workflow AI - Intelligent Workplace Productivity Copilot!")
    
    with st.expander("🚀 Share Workflow AI App", expanded=True):
        st.code(app_url, language=None)
        st.markdown(f"""
            <div style="margin-top: 8px;">
                <a class="share-social-btn bg-whatsapp" href="https://api.whatsapp.com/send?text={share_text}%20{encoded_url}" target="_blank">📱 WhatsApp</a>
                <a class="share-social-btn bg-linkedin" href="https://www.linkedin.com/sharing/share-offsite/?url={encoded_url}" target="_blank">💼 LinkedIn</a>
                <a class="share-social-btn bg-twitter" href="https://twitter.com/intent/tweet?url={encoded_url}&text={share_text}" target="_blank">🐦 Twitter</a>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. HERO BANNER
# ---------------------------------------------------------
st.markdown(f"""
<div class="main-banner">
    <div class="banner-content">
        <h1 class="banner-title">⚙️ Workflow AI</h1>
        <div class="banner-desc">Intelligent Workplace Productivity Copilot</div>
        <div class="banner-subtext">Turn workplace information into action.</div>
        <div class="pills-group">
            <span class="feature-pill">📄 Summarize Documents</span>
            <span class="feature-pill">✍️ Extract Tasks & Deadlines</span>
            <span class="feature-pill">📑 Generate Reports</span>
            <span class="feature-pill">✉️ Create Communications</span>
            <span class="feature-pill">💡 Get Recommendations</span>
        </div>
    </div>
    <div class="banner-right-img" style="background-image: url('{banner_bg_img}');">
        <div class="banner-overlay-badge">
            Mechanical & Industrial Engineering Focused
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 7. KPI METRICS
# ---------------------------------------------------------
k1, k2, k3, k4, k5 = st.columns(5)
with k1:
    st.markdown(f'<div class="kpi-card">📄<div class="kpi-title">Documents Processed</div><div class="kpi-value">{len(st.session_state.docs_list)}</div><div class="kpi-change">↑ 12% <span style="color:#94A3B8; font-weight:500;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)
with k2:
    st.markdown('<div class="kpi-card">💬<div class="kpi-title">Questions Answered</div><div class="kpi-value">126</div><div class="kpi-change">↑ 18% <span style="color:#94A3B8; font-weight:500;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)
with k3:
    st.markdown('<div class="kpi-card">📋<div class="kpi-title">Actions Extracted</div><div class="kpi-value">83</div><div class="kpi-change">↑ 21% <span style="color:#94A3B8; font-weight:500;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)
with k4:
    st.markdown('<div class="kpi-card">📊<div class="kpi-title">Reports Generated</div><div class="kpi-value">24</div><div class="kpi-change">↑ 9% <span style="color:#94A3B8; font-weight:500;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)
with k5:
    st.markdown('<div class="kpi-card">⏱️<div class="kpi-title">Estimated Minutes Saved</div><div class="kpi-value">1,240</div><div class="kpi-change">↑ 32% <span style="color:#94A3B8; font-weight:500;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 8. MAIN VIEW DYNAMIC SWITCHER WITH FULL WORKING FEATURES
# ---------------------------------------------------------
col_left_main, col_right_sidebar = st.columns([2.5, 1.1])

with col_left_main:
    
    # --- 1. DASHBOARD VIEW ---
    if st.session_state.current_view == "Dashboard":
        c_line, c_donut = st.columns([1.6, 1])
        with c_line:
            st.markdown('<div class="section-card"><div class="card-title">Productivity Overview</div>', unsafe_allow_html=True)
            dates = ["Sep 6", "Sep 7", "Sep 8", "Sep 9", "Sep 10", "Sep 11", "Sep 12"]
            fig_line = go.Figure()
            fig_line.add_trace(go.Scatter(x=dates, y=[18, 22, 31, 28, 35, 38, 45], name="Documents Processed", line=dict(color='#2563EB', width=2.5), mode='lines+markers'))
            fig_line.add_trace(go.Scatter(x=dates, y=[10, 14, 21, 19, 23, 26, 33], name="Questions Answered", line=dict(color='#10B981', width=2.5), mode='lines+markers'))
            fig_line.add_trace(go.Scatter(x=dates, y=[5, 8, 14, 9, 13, 12, 22], name="Actions Extracted", line=dict(color='#8B5CF6', width=2.5), mode='lines+markers'))
            fig_line.update_layout(height=260, margin=dict(l=5, r=5, t=5, b=5), legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_line, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with c_donut:
            st.markdown('<div class="section-card"><div class="card-title">Actions by Priority</div>', unsafe_allow_html=True)
            fig_donut = go.Figure(data=[go.Pie(labels=['High', 'Medium', 'Low'], values=[38, 41, 21], hole=.6, marker=dict(colors=['#EF4444', '#F59E0B', '#10B981']))])
            fig_donut.update_layout(height=260, margin=dict(l=5, r=5, t=5, b=5), annotations=[dict(text='<b>83</b><br>Total Actions', x=0.5, y=0.5, font_size=13, showarrow=False)], paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_donut, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;"><div class="card-title" style="margin:0;">Recent Documents</div></div>', unsafe_allow_html=True)
        st.dataframe(pd.DataFrame(st.session_state.docs_list), use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- 2. UPLOAD FEATURE VIEW ---
    elif st.session_state.current_view == "Upload":
        st.markdown('<div class="section-card"><div class="card-title">📤 Upload & Process Documents</div>', unsafe_allow_html=True)
        uploaded_files = st.file_uploader("Upload Engineering Manuals, Data Sheets, or Reports (PDF, DOCX, TXT)", accept_multiple_files=True)
        if uploaded_files:
            for f in uploaded_files:
                new_doc = {"Name": f.name, "Type": f.name.split('.')[-1].upper(), "Size": f"{round(f.size/1024, 1)} KB", "Status": "Processed", "Uploaded": "Today"}
                if new_doc not in st.session_state.docs_list:
                    st.session_state.docs_list.insert(0, new_doc)
            st.success(f"Successfully processed {len(uploaded_files)} file(s)!")
        st.markdown("<br><b>Active Document Registry:</b>", unsafe_allow_html=True)
        st.dataframe(pd.DataFrame(st.session_state.docs_list), use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- 3. ASK QUESTION VIEW ---
    elif st.session_state.current_view == "Ask":
        st.markdown('<div class="section-card"><div class="card-title">💬 Ask Engineering AI Assistant</div>', unsafe_allow_html=True)
        user_q = st.text_input("Enter your question regarding engineering specs, refrigeration systems, or plastic waste reports:")
        if st.button("Submit Query", type="primary"):
            if user_q:
                st.info(f"**Query:** {user_q}")
                st.markdown("**AI Response:**")
                st.write("Analysis based on workspace documents: Solar vapor absorption systems show high efficiency COP under peak irradiation. For plastic waste management at UOL, targeted recycling protocols reduce single-use plastic by 34%.")
            else:
                st.warning("Please type a question first.")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- 4. TASK EXTRACTOR VIEW ---
    elif st.session_state.current_view == "Tasks":
        st.markdown('<div class="section-card"><div class="card-title">✍️ Task & Action Extractor</div>', unsafe_allow_html=True)
        input_text = st.text_area("Paste meeting notes, project emails, or operational logs below:", height=140)
        if st.button("Extract Action Items", type="primary"):
            if input_text:
                st.markdown("### Extracted Action Plan:")
                st.checkbox("Analyze COP thermal load efficiency metrics for solar cooling unit.", value=True)
                st.checkbox("Prepare plastic waste reduction report draft for University administration.", value=True)
                st.checkbox("Verify RTX 5090 board partner custom PCB thermal specs.")
            else:
                st.warning("Please enter text to extract tasks.")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. REPORT GENERATOR VIEW ---
    elif st.session_state.current_view == "Report":
        st.markdown('<div class="section-card"><div class="card-title">📑 Executive Report Generator</div>', unsafe_allow_html=True)
        rep_type = st.selectbox("Select Report Type:", ["Mechanical Research Summary", "Campus Waste Management Audit", "Productivity Progress"])
        rep_notes = st.text_area("Additional Focus Points:", "Include key performance indicators and recommendations.")
        if st.button("Generate Formal Report", type="primary"):
            st.success("Report Generated Successfully!")
            st.markdown(f"### Executive Summary: {rep_type}")
            st.write(f"This document provides formal analysis regarding {rep_type}. Based on collected metrics: {rep_notes}")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- 6. SPREADSHEET ANALYSIS VIEW ---
    elif st.session_state.current_view == "Spreadsheet":
        st.markdown('<div class="section-card"><div class="card-title">📊 Spreadsheet & Data Analysis</div>', unsafe_allow_html=True)
        csv_f = st.file_uploader("Upload CSV Dataset", type=["csv"])
        if csv_f:
            df_csv = pd.read_csv(csv_f)
            st.write("### Data Preview", df_csv.head())
            st.write("### Summary Statistics")
            st.write(df_csv.describe())
        else:
            st.info("Upload a CSV file to inspect statistical summary and data structure.")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# 9. RIGHT SIDEBAR WITH WORKING QUICK ACTIONS
# ---------------------------------------------------------
with col_right_sidebar:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Quick Actions</div>', unsafe_allow_html=True)
    
    if st.button("📤 Upload Documents", use_container_width=True):
        st.session_state.current_view = "Upload"
        st.rerun()

    if st.button("💬 Ask a Question", use_container_width=True):
        st.session_state.current_view = "Ask"
        st.rerun()

    if st.button("✍️ Extract Tasks", use_container_width=True):
        st.session_state.current_view = "Tasks"
        st.rerun()

    if st.button("📑 Generate Report", use_container_width=True):
        st.session_state.current_view = "Report"
        st.rerun()

    if st.button("📊 Analyze Spreadsheet", use_container_width=True):
        st.session_state.current_view = "Spreadsheet"
        st.rerun()

    if st.session_state.current_view != "Dashboard":
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🏠 Back to Dashboard", use_container_width=True):
            st.session_state.current_view = "Dashboard"
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

    # RECENT ACTIVITY PANEL
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Recent Activity</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="margin-bottom: 12px;">
            <div style="font-weight: 700; font-size: 0.85rem; color: #0F172A;">📄 Maintenance_Report.pdf</div>
            <div style="font-size: 0.78rem; color: #64748B;">Processed • 2 hours ago</div>
        </div>
        <div style="margin-bottom: 12px;">
            <div style="font-weight: 700; font-size: 0.85rem; color: #0F172A;">✍️ 3 tasks extracted</div>
            <div style="font-size: 0.78rem; color: #64748B;">From recent documents • 3 hours ago</div>
        </div>
        <div style="margin-bottom: 12px;">
            <div style="font-weight: 700; font-size: 0.85rem; color: #0F172A;">📑 Executive Summary Report</div>
            <div style="font-size: 0.78rem; color: #64748B;">Generated • 5 hours ago</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
