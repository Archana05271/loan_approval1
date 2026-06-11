import paths  # noqa: F401

import streamlit as st

from streamlit_compat import show_image
from ui_styles import inject_global_styles

# ======================================================
# PAGE CONFIG (Updated Branding Title)
# ======================================================
st.set_page_config(
    page_title="LoanSmart | Home",
    page_icon="🏦",
    layout="wide",
)

# =====================================================================
# SIDEBAR PANEL BRANDING & LOGO (Added for Consistency)
# =====================================================================
with st.sidebar:
    # App Logo Icon (Matches all other sub-pages)
    st.image("https://cdn-icons-png.flaticon.com/512/2830/2830284.png", width=70)
    
    # Custom Sidebar Title Styling
    st.markdown("""
        <h2 style='margin-top: -10px; color: #ffffff;'>LoanSmart</h2>
        <p style='font-size: 0.85rem; color: #b0a8b9; margin-top: -15px;'>Smart Financial Intelligence</p>
        <hr style='margin-top: 5px; margin-bottom: 20px; border-color: rgba(255,255,255,0.1);'>
    """, unsafe_allow_html=True)

# =====================================================================

inject_global_styles()

st.markdown("""
<div class='main-title'>
🏦 Loan Approval Prediction System
</div>

<div class='sub-title'>
AI Powered Banking Platform with Smart Financial Intelligence
</div>

<div class='badge-row'>
    <div class='badge delay-1'>🤖 Machine Learning</div>
    <div class='badge delay-2'>📊 Analytics Dashboard</div>
    <div class='badge delay-3'>⚡ Instant Prediction</div>
    <div class='badge delay-4'>🔒 Secure System</div>
</div>
""", unsafe_allow_html=True)

show_image("https://images.unsplash.com/photo-1554224155-6726b3ff858f")

st.markdown("""
<div class='stats-row'>
    <div class='stat-box'>
        <div class='stat-number'>4K+</div>
        <div class='stat-label'>Applications</div>
    </div>
    <div class='stat-box'>
        <div class='stat-number'>80%</div>
        <div class='stat-label'>Prediction Accuracy</div>
    </div>
    <div class='stat-box'>
        <div class='stat-number'>3s</div>
        <div class='stat-label'>Processing Time</div>
    </div>
    <div class='stat-box'>
        <div class='stat-number'>24/7</div>
        <div class='stat-label'>System Availability</div>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='card'>
    <h2>📊 Dashboard</h2>
    <p>
    Visualize applicant financial analytics, approval distributions,
    asset evaluations, and interactive loan insights using dynamic charts.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
    <h2>🤖 AI Prediction</h2>
    <p>
    Predict loan approval instantly using Machine Learning algorithms
    trained on applicant financial and credit history datasets.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='card'>
    <h2>⚡ Fast Results</h2>
    <p>
    Receive quick and intelligent loan approval insights with
    real-time risk assessment and financial analysis.
    </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class='section-title'>
🔍 How The System Works
</div>
""", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown("""
    <div class='step-card'>
    <div style='font-size:38px;'>1️⃣</div>
    <div class='step-title'>Enter Details</div>
    <div class='step-text'>Fill applicant financial and personal details.</div>
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class='step-card'>
    <div style='font-size:38px;'>2️⃣</div>
    <div class='step-title'>Data Processing</div>
    <div class='step-text'>System scales and processes financial information.</div>
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class='step-card'>
    <div style='font-size:38px;'>3️⃣</div>
    <div class='step-title'>AI Prediction</div>
    <div class='step-text'>ML model evaluates approval probability and risk.</div>
    </div>
    """, unsafe_allow_html=True)

with s4:
    st.markdown("""
    <div class='step-card'>
    <div style='font-size:38px;'>4️⃣</div>
    <div class='step-title'>Get Result</div>
    <div class='step-text'>View approval result and financial insights instantly.</div>
    </div>
    """, unsafe_allow_html=True)

st.success("✅ Navigate through the sidebar to explore prediction, dashboard analytics, and project insights.")
