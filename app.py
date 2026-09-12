import streamlit as st
import pandas as pd
import plotly.express as px
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
# 2. CUSTOM CSS (STYLING EXACT MATCH)
# ---------------------------------------------------------
st.markdown("""
<style>
    /* Global Page Styling */
    .stApp {
        background-color: #F8FAFC;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Hide Default Header & Footer */
    header, footer { visibility: hidden !important; }
    
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
        max-width: 100% !important;
    }

    /* Sidebar Customization */
    section[data-testid="stSidebar"] {
        width: 280px !important;
        background-color: #F8FAFC !important;
        border-right: 1px solid #E2E8F0 !important;
    }
    
    .sidebar-logo-container {
        padding: 10px 5px 20px 5px;
    }
    
    .sidebar-brand {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .sidebar-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #0F2D6B;
        line-height: 1.1;
        margin: 0;
    }
    
    .sidebar-subtitle {
        font-size: 0.75rem;
        color: #475569;
        margin-top: 4px;
        font-weight: 500;
        line-height: 1.2;
    }

    /* Sidebar Navigation Menu Items */
    .nav-item {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 10px 14px;
        border-radius: 8px;
        font-size: 0.88rem;
        font-weight: 600;
        color: #334155;
        text-decoration: none;
        margin-bottom: 4px;
        transition: all 0.2s ease;
    }
    
    .nav-item:hover {
        background-color: #F1F5F9;
        color: #0284C7;
    }
    
    .nav-item.active {
        background-color: #E0F2FE;
        color: #0284C7;
    }

    .nav-divider {
        height: 1px;
        background-color: #E2E8F0;
        margin: 15px 0;
    }

    /* Top Navigation Bar */
    .top-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 15px;
    }

    .user-profile-chip {
        display: flex;
        align-items: center;
        gap: 10px;
        background: #FFFFFF;
        padding: 4px 12px 4px 6px;
        border-radius: 30px;
        border: 1px solid #E2E8F0;
    }

    .avatar-circle {
        width: 34px;
        height: 34px;
        border-radius: 50%;
        background-color: #0284C7;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.85rem;
    }

    /* Main Banner Card */
    .main-banner {
        background: linear-gradient(90deg, #FFFFFF 0%, #EFF6FF 50%, #DBEAFE 100%);
        border-radius: 16px;
        border: 1px solid #CBD5E1;
        padding: 0;
        display: flex;
        overflow: hidden;
        min-height: 200px;
        position: relative;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    .banner-content {
        padding: 24px 28px;
        width: 58%;
        z-index: 2;
    }

    .banner-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F2D6B;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .banner-desc {
        font-size: 1rem;
        color: #334155;
        font-weight: 600;
        margin-top: 4px;
        margin-bottom: 2px;
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
        width: 42%;
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
        width: 60%;
        background: linear-gradient(135deg, rgba(2, 132, 199, 0.85) 0%, rgba(3, 105, 161, 0.95) 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #FFFFFF;
        font-weight: 700;
        font-size: 0.92rem;
        text-align: center;
        padding: 15px;
        clip-path: ellipse(130% 100% at 100% 50%);
    }

    /* KPI Cards Styling */
    .kpi-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        height: 100%;
    }

    .kpi-title {
        font-size: 0.82rem;
        font-weight: 700;
        color: #475569;
        margin-top: 10px;
    }

    .kpi-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #0F172A;
        margin: 4px 0;
    }

    .kpi-change {
        font-size: 0.78rem;
        font-weight: 700;
        color: #10B981;
        display: flex;
        align-items: center;
        gap: 4px;
    }

    .kpi-subtext {
        font-size: 0.72rem;
        color: #94A3B8;
        font-weight: 500;
    }

    /* Container Cards */
    .section-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        margin-bottom: 20px;
    }

    .card-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 15px;
    }

    /* Quick Action Buttons */
    .action-btn {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 12px 16px;
        border-radius: 10px;
        font-size: 0.88rem;
        font-weight: 600;
        margin-bottom: 10px;
        cursor: pointer;
        border: 1px solid transparent;
    }

    .btn-blue { background-color: #EFF6FF; color: #1D4ED8; border-color: #BFDBFE; }
    .btn-purple { background-color: #F5F3FF; color: #6D28D9; border-color: #DDD6FE; }
    .btn-green { background-color: #ECFDF5; color: #047857; border-color: #A7F3D0; }
    .btn-orange { background-color: #FFF7ED; color: #C2410C; border-color: #FFEDD5; }
    .btn-teal { background-color: #F0FDFA; color: #0F766E; border-color: #99F6E4; }

    /* File Type Badges */
    .badge-pdf { background-color: #FEE2E2; color: #DC2626; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 0.75rem; }
    .badge-xlsx { background-color: #D1FAE5; color: #059669; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 0.75rem; }
    .badge-docx { background-color: #DBEAFE; color: #2563EB; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 0.75rem; }
    .badge-csv { background-color: #E0E7FF; color: #4F46E5; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 0.75rem; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. SIDEBAR NAVIGATION
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div class="sidebar-logo-container">
            <div class="sidebar-brand">
                <span style="font-size: 2rem;">⚙️</span>
                <div>
                    <div class="sidebar-title">Workflow AI</div>
                </div>
            </div>
            <div class="sidebar-subtitle">Intelligent Workplace Productivity Copilot</div>
        </div>
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
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background-color: #EFF6FF; padding: 15px; border-radius: 12px; border: 1px solid #BFDBFE;">
            <div style="color: #1D4ED8; font-weight: 700; font-size: 0.85rem; margin-bottom: 4px;">Smarter Documents.</div>
            <div style="color: #1D4ED8; font-weight: 700; font-size: 0.85rem; margin-bottom: 4px;">Better Decisions.</div>
            <div style="color: #2563EB; font-weight: 600; font-size: 0.85rem;">Higher Productivity.</div>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. TOP BAR SEARCH & USER PROFILE
# ---------------------------------------------------------
col_search, col_user = st.columns([4, 1.2])

with col_search:
    st.text_input("Search", placeholder="🔍 Search documents, ask questions, or find actions...", label_visibility="collapsed")

with col_user:
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: flex-end; gap: 15px; margin-top: 2px;">
            <span style="font-size: 1.2rem; cursor: pointer;">🔔</span>
            <div class="user-profile-chip">
                <div class="avatar-circle">JD</div>
                <div style="line-height: 1.1;">
                    <div style="font-weight: 700; font-size: 0.85rem; color: #0F172A;">John Doe</div>
                    <div style="font-size: 0.72rem; color: #64748B;">Mechanical Engineer</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. MAIN HERO BANNER
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
# 6. KPI METRICS (5 COLUMNS)
# ---------------------------------------------------------
k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.markdown("""
    <div class="kpi-card">
        <span style="background: #EFF6FF; padding: 8px; border-radius: 8px; color: #2563EB;">📄</span>
        <div class="kpi-title">Documents Processed</div>
        <div class="kpi-value">47</div>
        <div class="kpi-change">↑ 12% <span class="kpi-subtext">vs. last 7 days</span></div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown("""
    <div class="kpi-card">
        <span style="background: #ECFDF5; padding: 8px; border-radius: 8px; color: #059669;">💬</span>
        <div class="kpi-title">Questions Answered</div>
        <div class="kpi-value">126</div>
        <div class="kpi-change">↑ 18% <span class="kpi-subtext">vs. last 7 days</span></div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown("""
    <div class="kpi-card">
        <span style="background: #F5F3FF; padding: 8px; border-radius: 8px; color: #7C3AED;">📋</span>
        <div class="kpi-title">Actions Extracted</div>
        <div class="kpi-value">83</div>
        <div class="kpi-change">↑ 21% <span class="kpi-subtext">vs. last 7 days</span></div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown("""
    <div class="kpi-card">
        <span style="background: #FFF7ED; padding: 8px; border-radius: 8px; color: #EA580C;">📊</span>
        <div class="kpi-title">Reports Generated</div>
        <div class="kpi-value">24</div>
        <div class="kpi-change">↑ 9% <span class="kpi-subtext">vs. last 7 days</span></div>
    </div>
    """, unsafe_allow_html=True)

with k5:
    st.markdown("""
    <div class="kpi-card">
        <span style="background: #F0FDFA; padding: 8px; border-radius: 8px; color: #0D9488;">⏱️</span>
        <div class="kpi-title">Estimated Minutes Saved</div>
        <div class="kpi-value">1,240</div>
        <div class="kpi-change">↑ 32% <span class="kpi-subtext">vs. last 7 days</span></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 7. CHARTS SECTION
# ---------------------------------------------------------
col_line, col_donut = st.columns([2.2, 1.2])

with col_line:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Productivity Overview</div>', unsafe_allow_html=True)
    
    dates = ["Sep 6", "Sep 7", "Sep 8", "Sep 9", "Sep 10", "Sep 11", "Sep 12"]
    
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=dates, y=[18, 22, 31, 28, 35, 38, 45], name="Documents Processed", line=dict(color='#2563EB', width=2.5), mode='lines+markers'))
    fig_line.add_trace(go.Scatter(x=dates, y=[10, 14, 21, 19, 23, 26, 33], name="Questions Answered", line=dict(color='#10B981', width=2.5), mode='lines+markers'))
    fig_line.add_trace(go.Scatter(x=dates, y=[5, 8, 14, 9, 13, 12, 22], name="Actions Extracted", line=dict(color='#8B5CF6', width=2.5), mode='lines+markers'))

    fig_line.update_layout(
        height=280,
        margin=dict(l=10, r=10, t=10, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#F1F5F9')
    )
    st.plotly_chart(fig_line, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_donut:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">Actions by Priority</div>', unsafe_allow_html=True)
    
    fig_donut = go.Figure(data=[go.Pie(
        labels=['High', 'Medium', 'Low'],
        values=[38, 41, 21],
        hole=.6,
        marker=dict(colors=['#EF4444', '#F59E0B', '#10B981'])
    )])
    
    fig_donut.update_layout(
        height=280,
        margin=dict(l=10, r=10, t=10, b=10),
        showlegend=True,
        annotations=[dict(text='<b>83</b><br>Total Actions', x=0.5, y=0.5, font_size=14, showarrow=False)],
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig_donut, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# 8. BOTTOM SECTION (TABLE & SIDEBAR ACTIONS/ACTIVITY)
# ---------------------------------------------------------
col_table, col_side_actions = st.columns([2.2, 1.2])

with col_table:
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

with col_side_actions:
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
