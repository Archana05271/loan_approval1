import paths  # noqa: F401

import streamlit as st
import google.generativeai as genai

from streamlit_compat import show_image
from ui_styles import inject_global_styles

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="LoanSmart | AI Assistant",
    page_icon="🤖",
    layout="wide",
)

inject_global_styles()

# ======================================================
# GEMINI CONFIG
# ======================================================

GEMINI_API_KEY = "AQ.Ab8RN6Kg3J4Ibjm2aBBuqNRn0Z3UWRVZG3I7R9ugtUtPkZk6rQ"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash")

# ======================================================
# HERO SECTION
# ======================================================

st.markdown("""
<div class='hero'>

<div class='title'>
🤖 LoanSmart AI Assistant
</div>

<div class='subtitle'>
Smart Loan Guidance, Credit Analysis & Financial Recommendations
</div>

<div class='badge-row'>
    <div class='badge'>💳 CIBIL Analysis</div>
    <div class='badge'>📊 Risk Assessment</div>
    <div class='badge'>⚡ Instant Guidance</div>
</div>

</div>
""", unsafe_allow_html=True)

# ======================================================
# IMAGE
# ======================================================

show_image(
    "https://images.unsplash.com/photo-1556740749-887f6717d7e4"
)

# ======================================================
# ABOUT SECTION
# ======================================================

st.markdown("""
<br>

<div class='card'>

<h2>📌 About AI Assistant</h2>

<p>
LoanSmart AI Assistant helps users understand loan eligibility,
credit score requirements, loan approval factors, EMI calculations,
financial risks, and smart improvement strategies.

The assistant provides real-time responses powered by Gemini AI.
</p>

</div>
""", unsafe_allow_html=True)

# ======================================================
# FEATURES
# ======================================================

st.markdown("""
<div class='section-title'>
🚀 AI Features
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='card'>
        <h3>💳 Credit Score Help</h3>
        <p>
        Learn how your CIBIL score impacts loan approval.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
        <h3>📊 Loan Eligibility</h3>
        <p>
        Understand important approval and rejection factors.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='card'>
        <h3>💡 Financial Guidance</h3>
        <p>
        Get recommendations to improve approval chances.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# SIDEBAR
# ======================================================

with st.sidebar:

    st.header("💡 Sample Questions")

    st.info("""
• Will my loan be approved with a CIBIL score of 750?

• How can I improve my credit score?

• What is EMI?

• Why was my loan rejected?

• What documents are required for a home loan?

• Is ₹40,000 income enough for a ₹5 lakh loan?

• What is a good CIBIL score?
""")

# ======================================================
# CHAT TITLE
# ======================================================

st.markdown("""
<div class='section-title'>
💬 Chat With LoanSmart AI
</div>
""", unsafe_allow_html=True)

# ======================================================
# CHAT HISTORY
# ======================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ======================================================
# CHAT INPUT
# ======================================================

user_input = st.chat_input(
    "Ask about loans, EMI, credit score, eligibility..."
)

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = f"""
You are LoanSmart AI Assistant.

Your responsibilities:

- Loan Approval Guidance
- Credit Score Analysis
- Loan Eligibility Assessment
- Risk Analysis
- EMI Guidance
- Financial Improvement Suggestions
- Banking and Loan Information

Guidelines:
- Use simple language.
- Give practical advice.
- Explain clearly.
- Keep responses professional.
- Focus only on loan and financial topics.

User Question:
{user_input}
"""

    try:

        response = model.generate_content(prompt)

        bot_reply = response.text

    except Exception as e:

        bot_reply = f"""
❌ Error generating response

{str(e)}
"""

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })

    with st.chat_message("assistant"):
        st.markdown(bot_reply)

# ======================================================
# FOOTER
# ======================================================

st.markdown("""
<div class='footer'>
🤖 LoanSmart AI Assistant · Powered by Gemini AI
</div>
""", unsafe_allow_html=True)