import streamlit as st
import base64
import os

# Page Config
st.set_page_config(
    page_title="Workflow AI - Intelligent Workplace Productivity Copilot",
    page_icon="⚙️",
    layout="wide"
)

# Helper function to convert local image to Base64
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# Path to your saved screenshot image
banner_b64 = get_image_base64("assets/workflow_banner.jpg")

# CSS for Exact Match Banner
st.markdown("""
    <style>
    /* Remove padding to touch top */
    .block-container {
        padding-top: 1rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }

    .workflow-banner {
        width: 100%;
        background: #FFFFFF;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        display: flex;
        overflow: hidden;
        position: relative;
        min-height: 200px;
        margin-bottom: 25px;
    }

    /* Left Content Section */
    .banner-left {
        width: 50%;
        padding: 24px 30px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        background: #FFFFFF;
        z-index: 2;
    }

    .logo-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 4px;
    }

    /* Gear Icon styling using SVG/HTML */
    .gear-logo {
        width: 42px;
        height: 42px;
    }

    .banner-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F2D6B;
        line-height: 1.1;
        margin: 0;
        letter-spacing: -0.5px;
    }

    .banner-subtitle {
        font-size: 1.05rem;
        font-weight: 600;
        color: #2563EB;
        margin-top: 6px;
    }

    .banner-tagline {
        font-size: 0.95rem;
        color: #475569;
        font-weight: 500;
        margin-top: 12px;
        margin-bottom: 18px;
    }

    /* Bottom Features Row */
    .features-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        align-items: center;
    }

    .feature-pill {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 6px 12px;
        border-radius: 8px;
        font-size: 0.78rem;
        font-weight: 600;
    }

    /* Color Palette for Pills exact match */
    .pill-blue { background-color: #EFF6FF; color: #1D4ED8; }
    .pill-green { background-color: #ECFDF5; color: #047857; }
    .pill-purple { background-color: #F5F3FF; color: #6D28D9; }
    .pill-orange { background-color: #FFF7ED; color: #C2410C; }
    .pill-teal { background-color: #F0FDFA; color: #0F766E; }

    /* Right Section (Image & Masking) */
    .banner-right {
        width: 50%;
        position: relative;
        overflow: hidden;
    }

    .banner-bg-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center;
    }

    /* Exact Curved Blue Masking Overlay on Right */
    .right-overlay-text {
        position: absolute;
        right: 0;
        top: 0;
        bottom: 0;
        width: 45%;
        background: linear-gradient(135deg, rgba(2, 132, 199, 0.85) 0%, rgba(3, 105, 161, 0.95) 100%);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: #FFFFFF;
        text-align: center;
        padding: 15px;
        clip-path: ellipse(120% 100% at 100% 50%);
    }

    .overlay-title {
        font-size: 0.95rem;
        font-weight: 700;
        line-height: 1.3;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- BANNER HTML OUTPUT -----------------

# If image file exists in assets, use local base64. Otherwise fallback to direct screenshot rendering.
if banner_b64:
    # Full Image Direct Render to guarantee 100% exact match
    st.markdown(f"""
        <div style="width:100%; border-radius:12px; overflow:hidden; border:1px solid #CBD5E1; box-shadow:0 4px 12px rgba(0,0,0,0.06); margin-bottom:20px;">
            <img src="data:image/jpeg;base64,{banner_b64}" style="width:100%; display:block;" alt="Workflow AI Banner">
        </div>
    """, unsafe_allow_html=True)

else:
    # Programmatic Recreation in HTML/CSS matching the screenshot
    st.markdown("""
        <div class="workflow-banner">
            <!-- Left Text Content -->
            <div class="banner-left">
                <div class="logo-header">
                    <svg class="gear-logo" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 15C13.6569 15 15 13.6569 15 12C15 10.3431 13.6569 9 12 9C10.3431 9 9 10.3431 9 12C9 13.6569 10.3431 15 12 15Z" fill="#0284C7"/>
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M11 2C10.4477 2 10 2.44772 10 3V4.06189C8.94827 4.28827 7.95779 4.71765 7.07062 5.31952L6.31952 4.56842C5.92899 4.17789 5.29583 4.17789 4.9053 4.56842L3.49109 5.98264C3.10057 6.37316 3.10057 7.00633 3.49109 7.39685L4.24219 8.14795C3.64032 9.03512 3.21094 10.0256 2.98456 11H1.92266C1.37037 11 0.922656 11.4477 0.922656 12C0.922656 12.5523 1.37037 13 1.92266 13H2.98456C3.21094 13.9744 3.64032 14.9649 4.24219 15.8521L3.49109 16.6032C3.10057 16.9937 3.10057 17.6268 3.49109 18.0174L4.9053 19.4316C5.29583 19.8221 5.92899 19.8221 6.31952 19.4316L7.07062 18.6805C7.95779 19.2824 8.94827 19.7117 10 19.9381V21C10 21.5523 10.4477 22 11 22H13C13.5523 22 14 21.5523 14 21V19.9381C15.0517 19.7117 16.0422 19.2824 16.9294 18.6805L17.6805 19.4316C18.071 19.8221 18.7042 19.8221 19.0947 19.4316L20.5089 18.0174C20.8994 17.6268 20.8994 16.9937 20.5089 16.6032L19.7578 15.8521C20.3597 14.9649 20.7891 13.9744 21.0154 13H22.0773C22.6296 13 23.0773 12.5523 23.0773 12C23.0773 11.4477 22.6296 11 22.0773 11H21.0154C20.7891 10.0256 20.3597 9.03512 19.7578 8.14795L20.5089 7.39685C20.8994 7.00633 20.8994 6.37316 20.5089 5.98264L19.0947 4.56842C18.7042 4.17789 18.071 4.17789 17.6805 4.56842L16.9294 5.31952C16.0422 4.71765 15.0517 4.28827 14 4.06189V3C14 2.44772 13.5523 2 13 2H11ZM12 17C14.7614 17 17 14.7614 17 12C17 9.23858 14.7614 7 12 7C9.23858 7 7 9.23858 7 12C7 14.7614 9.23858 17 12 17Z" fill="#0369A1"/>
                    </svg>
                    <h1 class="banner-title">Workflow AI</h1>
                </div>
                <div class="banner-subtitle">Intelligent Workplace Productivity Copilot</div>
                <div class="banner-tagline">Turn workplace information into action.</div>
                
                <!-- Bottom Pills -->
                <div class="features-row">
                    <div class="feature-pill pill-blue">📄 Summarize Documents</div>
                    <div class="feature-pill pill-green">✍️ Extract Tasks & Deadlines</div>
                    <div class="feature-pill pill-purple">📄 Generate Reports</div>
                    <div class="feature-pill pill-orange">⌛ Create Communications</div>
                    <div class="feature-pill pill-teal">📑 Get Recommendations</div>
                </div>
            </div>

            <!-- Right Image Section with Overlay -->
            <div class="banner-right">
                <img src="https://images.unsplash.com/photo-1581092335397-9583fe92d232?q=80&w=1200&auto=format&fit=crop" class="banner-bg-img" alt="Engineer">
                <div class="right-overlay-text">
                    <div class="overlay-title">Mechanical & Industrial<br>Engineering Focused</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
