import paths  # noqa: F401

import streamlit as st

from ui_styles import inject_global_styles

st.set_page_config(
    page_title="LoanSmart | About",
    page_icon="ℹ️",
    layout="wide",
)

inject_global_styles()

st.markdown("""
<div class='title'>
ℹ️ About Project
</div>

<div class='subtitle'>
System Architecture Framework Overview & Smart Loan Intelligence Platform
</div>

<div class='badge-row'>
    <div class='badge'>🤖 AI Powered</div>
    <div class='badge'>📊 Analytics Dashboard</div>
    <div class='badge'>🔒 Secure System</div>
    <div class='badge'>⚡ Real-Time Prediction</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero-card'>

<h2>
🏦 Intelligent Loan Evaluation Engine
</h2>

<p>
LoanSmart is an end-to-end AI-powered financial intelligence platform developed to modernize and simplify the traditional loan approval process. The system leverages Machine Learning algorithms to analyze applicant financial records, evaluate risk factors, inspect credit behavior, and generate instant loan eligibility predictions with high accuracy.
<br><br>
The platform combines predictive analytics, interactive dashboards, risk evaluation modules, and smart visualization tools to help financial institutions process loan applications faster and more efficiently while reducing manual verification complexity.
</p>

</div>
""", unsafe_allow_html=True)

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

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class='section-title'>
🚀 Technology Stack
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='stack-container'>

<span class='tech-badge'>🐍 Python 3.x</span>
<span class='tech-badge'>⚡ Streamlit Framework</span>
<span class='tech-badge'>🤖 Scikit-Learn ML Model</span>
<span class='tech-badge'>🐼 Pandas Data Processing</span>
<span class='tech-badge'>🔢 NumPy Computation</span>
<span class='tech-badge'>📈 Plotly Visual Analytics</span>
<span class='tech-badge'>📦 Joblib Serialization</span>
<span class='tech-badge'>🎨 HTML + CSS Styling</span>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='section-title'>
⚙️ System Workflow
</div>
""", unsafe_allow_html=True)

w1, w2, w3, w4 = st.columns(4)

with w1:
    st.markdown("""
    <div class='grid-box'>
    <h4>1️⃣ Data Input</h4>
    <p>User enters applicant financial details and asset information.</p>
    </div>
    """, unsafe_allow_html=True)

with w2:
    st.markdown("""
    <div class='grid-box'>
    <h4>2️⃣ Data Processing</h4>
    <p>Features are encoded, cleaned, scaled, and prepared for prediction.</p>
    </div>
    """, unsafe_allow_html=True)

with w3:
    st.markdown("""
    <div class='grid-box'>
    <h4>3️⃣ ML Prediction</h4>
    <p>Machine Learning model analyzes financial risk and predicts loan status.</p>
    </div>
    """, unsafe_allow_html=True)

with w4:
    st.markdown("""
    <div class='grid-box'>
    <h4>4️⃣ Smart Insights</h4>
    <p>Users receive approval results with intelligent financial analysis insights.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class='author-card'>
<h3>Lead Platform Architect</h3>
<p>✨ Archana ✨</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='footer'>
🏦 LoanSmart · AI Loan Approval Prediction System · Developed using Streamlit & Machine Learning
</div>
""", unsafe_allow_html=True)
