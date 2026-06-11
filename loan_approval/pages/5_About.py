import paths  # noqa: F401

import streamlit as st

from ui_styles import inject_global_styles

st.set_page_config(
    page_title="LoanSmart | About",
    page_icon="ℹ️",
    layout="wide",
)

# =====================================================================
# SIDEBAR PANEL BRANDING & LOGO
# =====================================================================
with st.sidebar:
    # App Logo Icon (Matches all other application pages)
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
<div class='title'>
ℹ️ About Platform
</div>

<div class='subtitle'>
Enterprise AI Platform for Underwriting Governance & Risk Intelligence
</div>

<div class='badge-row'>
    <div class='badge'>🤖 AI Powered</div>
    <div class='badge'>📊 Analytics Dashboard</div>
    <div class='badge'>🔒 Secure System</div>
    <div class='badge'>⚡ Real-Time Prediction</div>
</div>
""", unsafe_allow_html=True)

# ======================================================
# ENTERPRISE VISION SECTION
# ======================================================
st.markdown("""
<div class='hero-card'>

<h2>
🏦 Corporate Overview & Strategic Mission
</h2>

<p>
<b>LoanSmart</b> is a leading, institutional-grade automated underwriting and financial risk modeling platform designed to replace legacy credit evaluation workflows. By leveraging advanced Machine Learning frameworks, the platform instantly parses applicant profiles, analyzes demographic configurations, evaluates liability concentrations, and returns real-time risk scores with exceptional statistical calibration.
<br><br>
Our mission is to establish transparent, deterministic, and frictionless financial intelligence solutions. By combining deep mathematical model pipelines with enterprise-ready interactive interfaces, LoanSmart empowers banking institutions to lower operational overhead, mitigate credit defaults, and accelerate credit portfolio throughput.
</p>

</div>
""", unsafe_allow_html=True)

# ======================================================
# CORE PLATFORM CAPABILITIES
# ======================================================
st.markdown("""
<div class='section-title'>
📌 System Core Capabilities
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='grid-box'>
    <h4>🔮 Real-Time Inference</h4>
    <p>
    Instantly processes applicant financial attributes and predicts loan approval outcomes using trained Machine Learning models.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='grid-box'>
    <h4>📊 Interactive Analytics</h4>
    <p>
    Visualizes loan trends, approval distributions, income patterns, and financial metrics through interactive Plotly charts.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='grid-box'>
    <h4>🔒 Secure Architecture</h4>
    <p>
    Implements structured data handling, isolated model loading, and efficient system workflow management for safe predictions.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# PROFESSIONAL PLATFORM COMMITMENT
# ======================================================
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class='hero-card' style='border-left: 5px solid #6f42c1;'>
<h3>💼 Model Alignment & Operational Governance</h3>
<p>
LoanSmart is engineered under strict risk management oversight. The underlying machine learning model evaluates asset-to-debt ratios and creditworthiness profiles symmetrically to protect credit ecosystems from high-leverage liabilities, ensuring reliable risk intelligence delivery across all digital channels.
</p>
</div>
""", unsafe_allow_html=True)

# ======================================================
# AUTHOR PROFILE SECTION
# ======================================================
st.markdown("""
<div class='author-card' style='margin-top: 40px; padding: 25px; text-align: center;'>
<h3 style='margin-bottom: 5px;'>Lead Platform Architect</h3>
<h2 style='color: #6f42c1; margin-top: 0px; font-weight: bold;'>Archana</h2>
<p style='font-size: 1.1rem; color: #6c757d; margin-top: -5px;'>Machine Learning Intern</p>
</div>
""", unsafe_allow_html=True)

# ======================================================
# FOOTER
# ======================================================
st.markdown("""
<div class='footer'>
🏦 LoanSmart · AI Loan Approval Prediction System · Developed by Archana (Machine Learning Intern)
</div>
""", unsafe_allow_html=True)
