import paths  # noqa: F401

import streamlit as st

from streamlit_compat import show_image
from ui_styles import inject_global_styles

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="LoanSmart | Loan Guide",
    page_icon="📘",
    layout="wide"
)

inject_global_styles()

# ======================================================
# HERO SECTION
# ======================================================

st.markdown("""
<div class='hero'>

<div class='title'>
📘 Loan Guide
</div>

<div class='subtitle'>
Learn Everything About Loans, CIBIL Scores & Loan Approval Factors
</div>

<div class='badge-row'>
    <div class='badge'>💳 Credit Score</div>
    <div class='badge'>🏦 Loan Types</div>
    <div class='badge'>📊 Approval Tips</div>
</div>

</div>
""", unsafe_allow_html=True)

# ======================================================
# IMAGE
# ======================================================

show_image(
    "https://images.unsplash.com/photo-1554224155-6726b3ff858f"
)

# ======================================================
# CIBIL SECTION
# ======================================================

st.markdown("""
<div class='section-title'>
💳 Understanding CIBIL Score
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='card'>
    <h3>850 - 750</h3>
    <p>Excellent Credit Score with high approval chances.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card'>
    <h3>749 - 700</h3>
    <p>Good Score. Most banks approve loans easily.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='card'>
    <h3>699 - 650</h3>
    <p>Average Score. Approval may require more checks.</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='card'>
    <h3>Below 650</h3>
    <p>High Risk. Loan approval becomes difficult.</p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# LOAN TYPES
# ======================================================

st.markdown("""
<div class='section-title'>
🏦 Types of Loans
</div>
""", unsafe_allow_html=True)

l1, l2, l3, l4 = st.columns(4)

with l1:
    st.markdown("""
    <div class='card'>
    <h3>🏠 Home Loan</h3>
    <p>Used for purchasing or constructing a house.</p>
    </div>
    """, unsafe_allow_html=True)

with l2:
    st.markdown("""
    <div class='card'>
    <h3>🚗 Vehicle Loan</h3>
    <p>Used to purchase cars, bikes and other vehicles.</p>
    </div>
    """, unsafe_allow_html=True)

with l3:
    st.markdown("""
    <div class='card'>
    <h3>🎓 Education Loan</h3>
    <p>Supports higher education and academic expenses.</p>
    </div>
    """, unsafe_allow_html=True)

with l4:
    st.markdown("""
    <div class='card'>
    <h3>💰 Personal Loan</h3>
    <p>Can be used for personal financial requirements.</p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# APPROVAL FACTORS
# ======================================================

st.markdown("""
<div class='section-title'>
📊 Major Loan Approval Factors
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='card'>

<h3>Important Factors Considered By Banks</h3>

<ul>
<li>✅ CIBIL Score</li>
<li>✅ Annual Income</li>
<li>✅ Existing Loans</li>
<li>✅ Loan Amount Requested</li>
<li>✅ Employment Status</li>
<li>✅ Assets and Property Value</li>
<li>✅ Loan Repayment History</li>
</ul>

</div>
""", unsafe_allow_html=True)

# ======================================================
# IMPROVEMENT TIPS
# ======================================================

st.markdown("""
<div class='section-title'>
💡 Tips To Improve Loan Approval Chances
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='card'>
    <h3>💳 Improve Credit Score</h3>
    <p>Pay EMIs and credit card bills on time.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
    <h3>📉 Reduce Debt</h3>
    <p>Keep your existing liabilities under control.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='card'>
    <h3>💰 Stable Income</h3>
    <p>Maintain consistent income and employment history.</p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# QUICK FACTS
# ======================================================

st.markdown("""
<div class='section-title'>
📈 Loan Facts
</div>
""", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.metric("Ideal CIBIL", "750+")

with s2:
    st.metric("Low Risk", "80%+")

with s3:
    st.metric("Approval Factor", "Income")

with s4:
    st.metric("Best Practice", "On-time EMI")

# ======================================================
# FOOTER
# ======================================================

st.markdown("""
<div class='footer'>
📘 LoanSmart · Loan Education & Financial Awareness
</div>
""", unsafe_allow_html=True)