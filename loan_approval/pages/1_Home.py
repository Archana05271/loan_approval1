import paths  # noqa: F401

import streamlit as st

from streamlit_compat import show_image
from ui_styles import inject_global_styles

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="LoanSmart | Home",
    page_icon="🏦",
    layout="wide",
)

inject_global_styles()

# ======================================================
# HERO SECTION
# ======================================================

st.markdown("""
<div class='hero'>

<div class='title'>
🏦 LoanSmart
</div>

<div class='subtitle'>
Smart AI-Based Loan Approval Prediction System
</div>

<div class='badge-row'>
    <div class='badge'>🤖 AI Prediction</div>
    <div class='badge'>📊 Financial Analysis</div>
    <div class='badge'>⚡ Instant Results</div>
</div>

</div>
""", unsafe_allow_html=True)

# ======================================================
# HERO IMAGE
# ======================================================

show_image(
    "https://images.unsplash.com/photo-1554224155-6726b3ff858f"
)

# ======================================================
# ABOUT SECTION
# ======================================================

st.markdown("""
<br>

<div class='card'>

<h2>📌 About LoanSmart</h2>

<p>
LoanSmart is an AI-powered Loan Approval Prediction System developed
using Machine Learning and Streamlit.

The system analyzes applicant financial details, credit score,
income, assets, and loan information to predict whether
a loan will be approved or rejected.

It also provides smart insights and risk analysis
to help users understand loan eligibility factors.
</p>

</div>
""", unsafe_allow_html=True)

# ======================================================
# FEATURES SECTION
# ======================================================

st.markdown("""
<div class='section-title'>
🚀 Key Features
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='card'>
        <h3>🤖 AI Prediction</h3>
        <p>
        Predict loan approval instantly using Machine Learning.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
        <h3>📊 Dashboard Analytics</h3>
        <p>
        Visualize financial and loan-related insights using charts.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='card'>
        <h3>⚠️ Risk Analysis</h3>
        <p>
        Understand approval and rejection reasons clearly.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# HOW IT WORKS
# ======================================================

st.markdown("""
<div class='section-title'>
🔍 How It Works
</div>
""", unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)

with s1:
    st.markdown("""
    <div class='step-card'>
        <h2>1️⃣</h2>
        <h4>Enter Details</h4>
        <p>Fill applicant financial and personal details.</p>
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class='step-card'>
        <h2>2️⃣</h2>
        <h4>AI Analysis</h4>
        <p>Machine Learning model evaluates applicant data.</p>
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class='step-card'>
        <h2>3️⃣</h2>
        <h4>Prediction Result</h4>
        <p>Receive instant loan approval or rejection result.</p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# BUTTON
# ======================================================

st.markdown("<br>", unsafe_allow_html=True)

st.page_link(
    "pages/2_Predict.py",
    label="🔍 Check Loan Approval",
    icon="🏦"
)

# ======================================================
# FOOTER
# ======================================================

st.markdown("""
<div class='footer'>
🏦 LoanSmart · AI Loan Approval Prediction System
</div>
""", unsafe_allow_html=True)