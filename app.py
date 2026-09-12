import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64
import os

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Workflow AI - Intelligent Workplace Copilot",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Base64 Image Converter for Hero Banner
def get_image_base64(img_path):
    if os.path.exists(img_path):
        with open(img_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            return f"data:image/jpeg;base64,{encoded_string}"
    return "https://images.unsplash.com/photo-1581092335397-9583fe92d232?q=80&w=1000&auto=format&fit=crop"

banner_bg_img = get_image_base64("banner_img.jpg")

# ---------------------------------------------------------
# 2. GLOBAL STYLING
# ---------------------------------------------------------
st.markdown(f"""
<style>
    .stApp {{ background-color: #F8FAFC; font-family: 'Inter', sans-serif; }}
    header, footer {{ visibility: hidden !important; }}
    .block-container {{ padding-top: 1rem !important; padding-bottom: 2rem !important; max-width: 100% !important; }}
    
    /* Hero Banner */
    .main-banner {{
        background: linear-gradient(90deg, #FFFFFF 0%, #EFF6FF 45%, #DBEAFE 100%);
        border-radius: 16px; border: 1px solid #CBD5E1;
        display: flex; overflow: hidden; min-height: 220px; margin-bottom: 20px;
    }}
    .banner-content {{ padding: 24px; width: 55%; }}
    .banner-title {{ font-size: 2rem; font-weight: 800; color: #0F2D6B; margin: 0; }}
    .banner-desc {{ font-size: 0.95rem; color: #334155; font-weight: 600; margin-top: 4px; }}
    .banner-right-img {{
        width: 45%; background-size: cover; background-position: center 15%;
        background-repeat: no-repeat; border-radius: 0 16px 16px 0;
    }}
    
    /* KPI Cards */
    .kpi-card {{ background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 14px; }}
    .kpi-title {{ font-size: 0.8rem; font-weight: 700; color: #475569; }}
    .kpi-value {{ font-size: 1.6rem; font-weight: 800; color: #0F172A; margin: 4px 0; }}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. SESSION STATE INITIALIZATION
# ---------------------------------------------------------
if "uploaded_docs" not in st.session_state:
    st.session_state.uploaded_docs = []

# ---------------------------------------------------------
# 4. SIDEBAR NAVIGATION
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### ⚙️ Workflow AI")
    st.caption("Intelligent Workplace Copilot")
    
    selected_page = st.radio(
        "Navigation",
        ["🏠 Dashboard", "📤 Upload & Process", "🤖 AI Assistant", "✍️ Task Extractor", "📊 Data Analysis"],
        label_visibility="collapsed"
    )

# ---------------------------------------------------------
# 5. HEADER & BANNER
# ---------------------------------------------------------
st.markdown(f"""
<div class="main-banner">
    <div class="banner-content">
        <h1 class="banner-title">⚙️ Workflow AI</h1>
        <div class="banner-desc">Engineering & Corporate Productivity Copilot</div>
        <p style="color:#64748B; font-size:0.85rem;">Turn unstructured engineering reports, logs, and data into automated workflows.</p>
    </div>
    <div class="banner-right-img" style="background-image: url('{banner_bg_img}');"></div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. DYNAMIC PAGES & FUNCTIONALITY
# ---------------------------------------------------------

if selected_page == "🏠 Dashboard":
    # KPI Metrics
    k1, k2, k3, k4 = st.columns(4)
    k1.markdown(f'<div class="kpi-card"><div class="kpi-title">Documents Active</div><div class="kpi-value">{len(st.session_state.uploaded_docs)}</div></div>', unsafe_allow_html=True)
    k2.markdown('<div class="kpi-card"><div class="kpi-title">Tasks Pending</div><div class="kpi-value">14</div></div>', unsafe_allow_html=True)
    k3.markdown('<div class="kpi-card"><div class="kpi-title">Reports Generated</div><div class="kpi-value">8</div></div>', unsafe_allow_html=True)
    k4.markdown('<div class="kpi-card"><div class="kpi-title">Hours Saved</div><div class="kpi-value">34.5 hrs</div></div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Visual Analytics Chart
    st.subheader("📈 System Analytics")
    dates = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=[4, 8, 12, 7, 15, 9, 18], name="Tasks Extracted", line=dict(color='#0284C7', width=3)))
    fig.update_layout(height=280, margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)

elif selected_page == "📤 Upload & Process":
    st.subheader("📤 Document Upload & Intelligence Center")
    
    uploaded_files = st.file_uploader("Upload Engineering Manuals, Logs, or Reports (PDF, TXT, CSV)", accept_multiple_files=True)
    
    if uploaded_files:
        for file in uploaded_files:
            file_details = {"Name": file.name, "Size": f"{round(file.size/1024, 2)} KB", "Status": "Processed"}
            if file_details not in st.session_state.uploaded_docs:
                st.session_state.uploaded_docs.append(file_details)
        st.success(f"Successfully processed {len(uploaded_files)} file(s)!")
    
    st.markdown("---")
    st.subheader("📄 Processed Documents Library")
    if st.session_state.uploaded_docs:
        df_docs = pd.DataFrame(st.session_state.uploaded_docs)
        st.dataframe(df_docs, use_container_width=True)
    else:
        st.info("No documents uploaded yet. Upload a file above to get started.")

elif selected_page == "🤖 AI Assistant":
    st.subheader("🤖 Engineering Copilot Assistant")
    user_query = st.text_input("Ask anything about your projects, formulas, or uploaded files:")
    
    if st.button("Submit Query"):
        if user_query:
            st.info(f"**Query:** {user_query}")
            st.markdown(f"**AI Response:** Analyzing data... (Connect your Gemini API key here to generate instant context-aware answers).")
        else:
            st.warning("Please type a question first.")

elif selected_page == "✍️ Task Extractor":
    st.subheader("✍️ Automated Task & Action Extractor")
    raw_text = st.text_area("Paste meeting minutes, maintenance logs, or email text here:", height=150)
    
    if st.button("Extract Action Items"):
        if raw_text:
            st.markdown("**Extracted Action Items:**")
            st.markdown("* [ ] Review technical specifications and thermal load calculations.")
            st.markdown("* [ ] Prepare updated CAD models for system assembly.")
            st.markdown("* [ ] Schedule team review meeting for upcoming deadline.")
        else:
            st.warning("Please enter text to extract tasks.")

elif selected_page == "📊 Data Analysis":
    st.subheader("📊 Spreadsheet & CSV Analyzer")
    csv_file = st.file_uploader("Upload Data Sheet (CSV)", type=["csv"])
    
    if csv_file:
        df = pd.read_csv(csv_file)
        st.write("### Data Preview", df.head())
        st.write("### Data Summary Statistics")
        st.write(df.describe())
