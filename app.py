import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Workflow AI - Intelligent Workplace Productivity Copilot",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# 2. STYLING & FIXES (NO UNDERLINES, GITHUB & SHARE ADDED)
# ---------------------------------------------------------
st.markdown("""
<style>
    /* Global Page Styling */
    .stApp {
        background-color: #F8FAFC;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Hide Default Streamlit Header & Footer */
    header, footer { visibility: hidden !important; }
    
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
        max-width: 100% !important;
    }

    /* Sidebar Navigation Links - NO UNDERLINES */
    section[data-testid="stSidebar"] {
        width: 280px !important;
        background-color: #F8FAFC !important;
        border-right: 1px solid #E2E8F0 !important;
    }
    
    .nav-item {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 10px 14px;
        border-radius: 8px;
        font-size: 0.88rem;
        font-weight: 600;
        color: #334155 !important;
        text-decoration: none !important;
        margin-bottom: 4px;
        transition: all 0.2s ease;
    }
    
    .nav-item:hover {
        background-color: #F1F5F9;
        color: #0284C7 !important;
        text-decoration: none !important;
    }
    
    .nav-item.active {
        background-color: #E0F2FE;
        color: #0284C7 !important;
        font-weight: 700;
        text-decoration: none !important;
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
        margin-top: 10px;
        margin-bottom: 15px;
        transition: background 0.2s ease;
    }
    .github-btn:hover {
        background-color: #1E293B;
    }

    .nav-divider {
        height: 1px;
        background-color: #E2E8F0;
        margin: 15px 0;
    }

    /* Hero Banner Section */
    .main-banner {
        background: linear-gradient(90deg, #FFFFFF 0%, #EFF6FF 45%, #DBEAFE 100%);
        border-radius: 16px;
        border: 1px solid #CBD5E1;
        display: flex;
        overflow: hidden;
        min-height: 200px;
        position: relative;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    .banner-content {
        padding: 24px 28px;
        width: 60%;
        z-index: 2;
    }

    .banner-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F2D6B;
        margin: 0;
    }

    .banner-desc {
        font-size: 1rem;
        color: #334155;
        font-weight: 600;
        margin-top: 4px;
    }

    .banner-subtext {
        font-size: 0.9rem;
        color: #64748B;
        margin-bottom: 18px;
    }

    .pills-group {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
    }

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

    .banner-right-img {
        width: 40%;
        position: relative;
        background-image: url('https://images.unsplash.com/photo-1581092335397-9583fe92d232?q=80&w=1200&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
    }

    .banner-overlay-badge {
        position: absolute;
        right: 0;
        top: 0;
        bottom: 0;
        width: 75%;
        background: linear-gradient(135deg, rgba(2, 132, 199, 0.75) 0%, rgba(3, 105, 161, 0.9) 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #FFFFFF;
        font-weight: 700;
        font-size: 0.92rem;
        text-align: center;
        padding: 15px;
    }

    /* KPI Cards Styling */
    .kpi-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }

    .kpi-title { font-size: 0.82rem; font-weight: 700; color: #475569; margin-top: 10px; }
    .kpi-value { font-size: 1.8rem; font-weight: 800; color: #0F172A; margin: 4px 0; }
    .kpi-change { font-size: 0.78rem; font-weight: 700; color: #10B981; }

    /* Container Cards */
    .section-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        margin-bottom: 20px;
    }

    .card-title { font-size: 1.05rem; font-weight: 700; color: #0F172A; margin-bottom: 15px; }

    /* Quick Action Buttons Styling */
    .action-btn {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 12px 16px;
        border-radius: 10px;
        font-size: 0.88rem;
        font-weight: 600;
        margin-bottom: 10px;
        border: 1px solid transparent;
        cursor: pointer;
    }

    .btn-blue { background-color: #EFF6FF; color: #1D4ED8; border-color: #BFDBFE; }
    .btn-purple { background-color: #F5F3FF; color: #6D28D9; border-color: #DDD6FE; }
    .btn-green { background-color: #ECFDF5; color: #047857; border-color: #A7F3D0; }
    .btn-orange { background-color: #FFF7ED; color: #C2410C; border-color: #FFEDD5; }
    .btn-teal { background-color: #F0FDFA; color: #0F766E; border-color: #99F6E4; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. SIDEBAR NAVIGATION & GITHUB LINK
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
        
        <!-- GITHUB EDIT LINK BUTTON -->
        <a class="github-btn" href="https://github.com/bin-65/Workflow-AI" target="_blank">
            <svg height="16" width="16" viewBox="0 0 16 16" fill="white"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
            Edit Code (GitHub)
        </a>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <a class="nav-item active" href="#">🏠 Home</a>
        <a class="nav-item" href="#">📄 Document Intelligence</a>
        <a class="nav-item" href="#">🤖 AI Assistant</a>
        <a class="nav-item" href="#">✍️ Task Extractor</a>
        <a class="nav-item" href="#">✉️ Communication</a>
        <a class="nav-item" href="#">📑 Report Generator</a>
        <a class="nav-item" href="#">📊 Spreadsheet Analysis</a>
        <a class="nav-item" href="#">📈 Productivity Analytics</a>
        
        <div class="nav-divider"></div>
        
        <a class="nav-item" href="#">🕒 Recent Documents</a>
        <a class="nav-item" href="#">⚙️ Settings</a>
        <a class="nav-item" href="#">❓ Help & Support</a>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background-color: #EFF6FF; padding: 15px; border-radius: 12px; border: 1px solid #BFDBFE;">
            <div style="color: #1D4ED8; font-weight: 700; font-size: 0.85rem;">Smarter Documents.</div>
            <div style="color: #1D4ED8; font-weight: 700; font-size: 0.85rem;">Better Decisions.</div>
            <div style="color: #2563EB; font-weight: 600; font-size: 0.85rem;">Higher Productivity.</div>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. TOP BAR, SHARE OPTION & USER PROFILE
# ---------------------------------------------------------
col_search, col_actions = st.columns([3.8, 1.4])

with col_search:
    st.text_input("Search", placeholder="🔍 Search documents, ask questions, or find actions...", label_visibility="collapsed")

with col_actions:
    col_share, col_user_profile = st.columns([1, 2])
    
    with col_share:
        if st.button("🔗 Share", help="Share application link"):
            st.toast("App link copied to clipboard!", icon="✅")
            
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

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. HERO BANNER WITH ENGINEER IMAGE
# ---------------------------------------------------------
st.markdown("""
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
    <div class="banner-right-img">
        <div class="banner-overlay-badge">
            Mechanical & Industrial<br>Engineering Focused
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. KPI METRICS
# ---------------------------------------------------------
k1, k2, k3, k4, k5 = st.columns(5)
with k1:
    st.markdown('<div class="kpi-card">📄<div class="kpi-title">Documents Processed</div><div class="kpi-value">47</div><div class="kpi-change">↑ 12% <span style="color:#94A3B8; font-weight:500;">vs. last 7 days</span></div></div>', unsafe_allow_html=True)
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
# 7. MAIN CONTENT & RIGHT SIDEBAR PANELS
# ---------------------------------------------------------
col_left_main, col_right_sidebar = st.columns([2.5, 1.1])

with col_left_main:
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
    st.markdown('<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;"><div class="card-title" style="margin:0;">Recent Documents</div><a href="#" style="font-size:0.82rem; font-weight:700; color:#0284C7; text-decoration:none;">View All</a></div>', unsafe_allow_html=True)
    docs = [
        {"Name": "Maintenance_Report.pdf", "Type": "PDF", "Size": "2.4 MB", "Status": "Ready", "Uploaded": "2 hours ago"},
        {"Name": "Production_Data.xlsx", "Type": "XLSX", "Size": "1.8 MB", "Status": "Ready", "Uploaded": "4 hours ago"},
        {"Name": "Meeting_Notes.docx", "Type": "DOCX", "Size": "1.2 MB", "Status": "Ready", "Uploaded": "6 hours ago"},
        {"Name": "Inspection_Report.pdf", "Type": "PDF", "Size": "3.1 MB", "Status": "Processing", "Uploaded": "7 hours ago"},
        {"Name": "Team_Updates.csv", "Type": "CSV", "Size": "0.9 MB", "Status": "Ready", "Uploaded": "8 hours ago"}
    ]
    st.dataframe(pd.DataFrame(docs), use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right_sidebar:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Quick Actions</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="action-btn btn-blue">📤 Upload Documents</div>
        <div class="action-btn btn-purple">💬 Ask a Question</div>
        <div class="action-btn btn-green">✍️ Extract Tasks</div>
        <div class="action-btn btn-orange">📑 Generate Report</div>
        <div class="action-btn btn-teal">📊 Analyze Spreadsheet</div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;"><div class="card-title" style="margin:0;">Recent Activity</div><a href="#" style="font-size:0.82rem; font-weight:700; color:#0284C7; text-decoration:none;">View All</a></div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="margin-bottom: 14px;">
            <div style="font-weight: 700; font-size: 0.85rem; color: #0F172A;">📄 Maintenance_Report.pdf</div>
            <div style="font-size: 0.78rem; color: #64748B;">Processed • 2 hours ago</div>
        </div>
        <div style="margin-bottom: 14px;">
            <div style="font-weight: 700; font-size: 0.85rem; color: #0F172A;">✍️ 3 tasks extracted</div>
            <div style="font-size: 0.78rem; color: #64748B;">From recent documents • 3 hours ago</div>
        </div>
        <div style="margin-bottom: 14px;">
            <div style="font-weight: 700; font-size: 0.85rem; color: #0F172A;">📑 Executive Summary Report</div>
            <div style="font-size: 0.78rem; color: #64748B;">Generated • 5 hours ago</div>
        </div>
        <div style="margin-bottom: 14px;">
            <div style="font-weight: 700; font-size: 0.85rem; color: #0F172A;">📊 Production_Data.xlsx</div>
            <div style="font-size: 0.78rem; color: #64748B;">Analyzed • 6 hours ago</div>
        </div>
        <div>
            <div style="font-weight: 700; font-size: 0.85rem; color: #0F172A;">💬 Question answered</div>
            <div style="font-size: 0.78rem; color: #64748B;">"What was the issue with CNC Machine 04?" • 7 hours ago</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
