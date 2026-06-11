import paths  # noqa: F401

import streamlit as st

from streamlit_compat import show_image
from ui_styles import inject_global_styles

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="LoanSmart | Risk Analysis",
    page_icon="⚠️",
    layout="wide"
)

# =====================================================================
# SIDEBAR PANEL BRANDING & LOGO (Added for Consistency)
# =====================================================================
with st.sidebar:
    # App Logo Icon (Matches Predict and Dashboard Pages)
    st.image("https://cdn-icons-png.flaticon.com/512/2830/2830284.png", width=70)
    
    # Custom Sidebar Title Styling
    st.markdown("""
        <h2 style='margin-top: -10px; color: #ffffff;'>LoanSmart</h2>
        <p style='font-size: 0.85rem; color: #b0a8b9; margin-top: -15px;'>Smart Financial Intelligence</p>
        <hr style='margin-top: 5px; margin-bottom: 20px; border-color: rgba(255,255,255,0.1);'>
    """, unsafe_allow_html=True)

# =====================================================================

inject_global_styles()

# ======================================================
# HERO SECTION
# ======================================================

st.markdown("""
<div class='hero'>

<div class='title'>
⚠️ Risk Analysis
</div>

<div class='subtitle'>
Understand the factors that influence loan approval and rejection
</div>

<div class='badge-row'>
    <div class='badge'>📊 Risk Score</div>
    <div class='badge'>💳 Credit Analysis</div>
    <div class='badge'>🏦 Loan Assessment</div>
</div>

</div>
""", unsafe_allow_html=True)

# ======================================================
# IMAGE
# ======================================================

show_image(
    "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40"
)

# ======================================================
# ABOUT SECTION
# ======================================================

st.markdown("""
<div class='card'>

<h2>📌 What is Risk Analysis?</h2>

<p>
Risk Analysis helps determine the likelihood of loan approval
or rejection based on an applicant's financial profile.

Banks evaluate various risk factors such as credit score,
income, liabilities, loan amount, and repayment history
before approving a loan.
</p>

</div>
""", unsafe_allow_html=True)

# ======================================================
# RISK LEVELS
# ======================================================

st.markdown("""
<div class='section-title'>
📊 Risk Categories
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class='card'>
    <h3>🟢 Low Risk</h3>
    <p>
    CIBIL Score above 750,<br>
    Stable income,<br>
    Low liabilities,<br>
    High approval chances.
    </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card'>
    <h3>🟡 Medium Risk</h3>
    <p>
    CIBIL Score between 650–750,<br>
    Moderate income,<br>
    Existing debts,<br>
    Approval depends on lender policy.
    </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='card'>
    <h3>🔴 High Risk</h3>
    <p>
    CIBIL below 650,<br>
    High liabilities,<br>
    Poor repayment history,<br>
    Increased rejection probability.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# MAJOR RISK FACTORS
# ======================================================

st.markdown("""
<div class='section-title'>
⚡ Major Risk Factors
</div>
""", unsafe_allow_html=True)

r1, r2, r3, r4 = st.columns(4)

with r1:
    st.markdown("""
    <div class='card'>
    <h3>💳 Credit Score</h3>
    <p>Low scores increase lending risk.</p>
    </div>
    """, unsafe_allow_html=True)

with r2:
    st.markdown("""
    <div class='card'>
    <h3>💰 Income</h3>
    <p>Insufficient income affects repayment ability.</p>
    </div>
    """, unsafe_allow_html=True)

with r3:
    st.markdown("""
    <div class='card'>
    <h3>📉 Existing Debt</h3>
    <p>Higher liabilities increase financial burden.</p>
    </div>
    """, unsafe_allow_html=True)

with r4:
    st.markdown("""
    <div class='card'>
    <h3>🏦 Loan Amount</h3>
    <p>Large loans may require stronger financial backing.</p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# IMPROVEMENT TIPS
# ======================================================

st.markdown("""
<div class='section-title'>
💡 Risk Reduction Tips
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='card'>

<h3>Improve Your Approval Chances</h3>

<ul>
<li>✅ Pay EMIs and credit card bills on time</li>
<li>✅ Maintain a CIBIL score above 750</li>
<li>✅ Reduce outstanding debts</li>
<li>✅ Avoid multiple loan applications</li>
<li>✅ Maintain stable employment</li>
<li>✅ Increase savings and financial assets</li>
</ul>

</div>
""", unsafe_allow_html=True)

# ======================================================
# QUICK STATS
# ======================================================

st.markdown("""
<div class='section-title'>
📈 Risk Indicators
</div>
""", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.metric("Safe CIBIL", "750+")

with s2:
    st.metric("Moderate Risk", "650-749")

with s3:
    st.metric("High Risk", "<650")

with s4:
    st.metric("Key Factor", "Income")

# ======================================================
# FOOTER
# ======================================================

st.markdown("""
<div class='footer'>
⚠️ LoanSmart · Risk Analysis & Financial Assessment
</div>
""", unsafe_allow_html=True)
