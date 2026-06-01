import streamlit as st
import google.generativeai as genai

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="LoanSmart AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

.title{
    text-align:center;
    color:white;
    font-size:45px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#dbeafe;
    font-size:18px;
    margin-bottom:20px;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.2);
    margin-top:15px;
}

.footer{
    text-align:center;
    color:white;
    padding:20px;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# GEMINI CONFIG
# =====================================================

try:

    genai.configure(
        api_key=st.secrets["AQ.Ab8RN6Kg3J4Ibjm2aBBuqNRn0Z3UWRVZG3I7R9ugtUtPkZk6rQ"]
    )

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash"
    )

except Exception as e:

    st.error(f"Gemini Configuration Error: {e}")
    st.stop()

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class='title'>
🤖 LoanSmart AI Assistant
</div>

<div class='subtitle'>
Smart Loan Guidance, Credit Analysis & Financial Recommendations
</div>
""", unsafe_allow_html=True)

st.image(
    "https://images.unsplash.com/photo-1556740749-887f6717d7e4",
    use_container_width=True
)

# =====================================================
# ABOUT SECTION
# =====================================================

st.markdown("""
<div class='card'>

<h2>📌 About LoanSmart AI</h2>

LoanSmart AI helps users understand:

✅ Loan Eligibility

✅ Credit Score Analysis

✅ EMI Calculations

✅ Loan Approval Factors

✅ Financial Risk Assessment

✅ Smart Financial Suggestions

</div>
""", unsafe_allow_html=True)

# =====================================================
# FEATURES
# =====================================================

st.subheader("🚀 Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("💳 Credit Score Analysis")

with col2:
    st.info("📊 Loan Eligibility Assessment")

with col3:
    st.warning("💡 Financial Improvement Guidance")

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.header("💡 Sample Questions")

    st.markdown("""
- What is a good CIBIL score?
- Why was my loan rejected?
- How can I improve my credit score?
- What is EMI?
- Can I get a ₹5 lakh loan?
- Home loan documents required?
- What affects loan approval?
""")

# =====================================================
# CHAT SECTION
# =====================================================

st.subheader("💬 Chat With LoanSmart AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input(
    "Ask about loans, EMI, credit score, eligibility..."
)

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = f"""
You are LoanSmart AI Assistant.

Responsibilities:
- Loan Approval Guidance
- Loan Eligibility Assessment
- Credit Score Analysis
- EMI Information
- Financial Advice
- Banking Information

Rules:
1. Use simple language.
2. Give practical suggestions.
3. Use bullet points.
4. Explain clearly.
5. Stay focused on loan and finance topics.

User Question:
{user_input}
"""

    try:

        with st.spinner("Thinking..."):

            response = model.generate_content(prompt)

            bot_reply = response.text

    except Exception as e:

        bot_reply = f"""
❌ Error generating response

{str(e)}
"""

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_reply
        }
    )

    with st.chat_message("assistant"):
        st.markdown(bot_reply)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class='footer'>
🤖 LoanSmart AI Assistant | Powered by Gemini AI
</div>
""", unsafe_allow_html=True)
