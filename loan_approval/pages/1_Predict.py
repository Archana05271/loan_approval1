import paths  # noqa: F401

import pandas as pd
import streamlit as st

from ai_suggestions import ApplicantProfile, get_ai_insights
from model_loader import load_artifacts
from paths import HAPPY_GIF_PATH, SAD_GIF_PATH
from prediction_ui import (
    inject_prediction_animations,
    render_ai_suggestions,
    render_approval_result,
    render_rejection_result,
)
from streamlit_compat import button as st_button, show_image
from ui_styles import inject_global_styles

# Page configuration with matching LoanSmart branding
st.set_page_config(
    page_title="LoanSmart - Prediction",
    page_icon="🏦",
    layout="wide",
)

# Initialize CIBIL session state value if it doesn't exist
if "cibil_value" not in st.session_state:
    st.session_state.cibil_value = 650.0

# =====================================================================
# SIDEBAR PANEL BRANDING & LOGO
# =====================================================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2830/2830284.png", width=70)
    
    st.markdown("""
        <h2 style='margin-top: -10px; color: #ffffff;'>LoanSmart</h2>
        <p style='font-size: 0.85rem; color: #b0a8b9; margin-top: -15px;'>Smart Financial Intelligence</p>
        <hr style='margin-top: 5px; margin-bottom: 20px; border-color: rgba(255,255,255,0.1);'>
    """, unsafe_allow_html=True)

# =====================================================================

FEATURE_NAMES = [
    "no_of_dependents",
    "education",
    "self_employed",
    "income_annum",
    "loan_amount",
    "loan_term",
    "cibil_score",
    "residential_assets_value",
    "commercial_assets_value",
    "luxury_assets_value",
    "bank_asset_value",
]


@st.cache_resource(show_spinner="Loading AI model…")
def get_model_and_scaler():
    return load_artifacts()


inject_global_styles()
inject_prediction_animations()

try:
    model, scaler = get_model_and_scaler()
except FileNotFoundError as exc:
    st.error(str(exc))
    st.stop()

st.markdown("""
<div class='title'>
🏦 Loan Approval Prediction
</div>

<div class='subtitle'>
AI-Powered Smart Loan Eligibility & Risk Analysis System
</div>

<div class='badge-row'>
    <div class='badge'>✅ AI Prediction</div>
    <div class='badge'>⚡ Instant Results</div>
    <div class='badge'>📊 Risk Analysis</div>
    <div class='badge'>🔒 Secure System</div>
</div>
""", unsafe_allow_html=True)

# Input Form Area
with st.container(border=True):
    col1, col2 = st.columns(2)

    with col1:
        no_of_dependents = st.number_input(
            "👨‍👩‍👧 Dependents",
            min_value=0,
            max_value=10,
            value=0,
        )
        education = st.selectbox(
            "🎓 Education",
            ["Graduate", "Not Graduate"],
        )
        self_employed = st.selectbox(
            "💼 Self Employed",
            ["Yes", "No"],
        )
        income_annum = st.number_input(
            "💰 Annual Income",
            min_value=0.0,
            value=0.0,
        )
        loan_amount = st.number_input(
            "🏦 Loan Amount",
            min_value=0.0,
            value=0.0,
        )

    with col2:
        loan_term = st.number_input(
            "📅 Loan Term (years)",
            min_value=0.0,
            value=0.0,
        )

        # -------------------------------------------------------------
        # CIBIL Score or Estimator Section
        # -------------------------------------------------------------
        dont_know_cibil = st.checkbox("❓ Don't know your CIBIL score?")

        if dont_know_cibil:
            # Dropdowns to dynamically estimate a CIBIL score
            st.markdown("#### 🧮 CIBIL Score Estimator")
            
            pay_history = st.selectbox(
                "Have you paid your past bills/EMIs on time?",
                ["Always on time", "Delayed sometimes", "Frequently delayed", "No prior credit history"]
            )
            
            existing_debts = st.selectbox(
                "How much existing loan/credit card debt do you have?",
                ["Very Low / None", "Moderate", "High"]
            )
            
            credit_age = st.slider(
                "How many years have you been using credit (loans/cards)?", 
                min_value=0, max_value=15, value=2
            )

            # Calculation Logic based on standard banking credit score weightings
            estimated_cibil = 600.0  # Base initial score
            
            if pay_history == "Always on time":
                estimated_cibil += 150
            elif pay_history == "Delayed sometimes":
                estimated_cibil += 30
            elif pay_history == "Frequently delayed":
                estimated_cibil -= 100
            else:
                estimated_cibil = 650.0
                
            if pay_history != "No prior credit history":
                if existing_debts == "Very Low / None":
                    estimated_cibil += 100
                elif existing_debts == "High":
                    estimated_cibil -= 80
                    
                estimated_cibil += min(credit_age * 5, 50)
            
            # Update the session state value instantly
            st.session_state.cibil_value = float(max(300.0, min(900.0, estimated_cibil)))

        # The main input field now reads directly from the session state value
        cibil_score = st.number_input(
            "📈 CIBIL Score",
            min_value=300.0,
            max_value=900.0,
            value=st.session_state.cibil_value,
            key="cibil_input_field"
        )
        
        if dont_know_cibil:
            st.info(f"📊 Auto-calculated and filled: **{int(cibil_score)}**")
        # -------------------------------------------------------------

        residential_assets_value = st.number_input(
            "🏠 Residential Assets",
            min_value=0.0,
            value=0.0,
        )
        commercial_assets_value = st.number_input(
            "🏢 Commercial Assets",
            min_value=0.0,
            value=0.0,
        )
        luxury_assets_value = st.number_input(
            "🚘 Luxury Assets",
            min_value=0.0,
            value=0.0,
        )
        bank_asset_value = st.number_input(
            "🏛️ Bank Assets",
            min_value=0.0,
            value=0.0,
        )

# Format category selections to encoded features for the ML model pipeline
edu_enc = 1 if education == "Graduate" else 0
self_enc = 1 if self_employed == "Yes" else 0

st.markdown("<br>", unsafe_allow_html=True)

_, center_col, _ = st.columns([1, 2, 1])

with center_col:
    predict_btn = st_button("🚀 Predict Loan Status")

if predict_btn:
    if income_annum == 0 or loan_amount == 0 or loan_term == 0:
        st.error("⚠️ Please enter valid income, loan amount, and loan term.")
    else:
        profile = ApplicantProfile(
            no_of_dependents=int(no_of_dependents),
            education=education,
            self_employed=self_employed,
            income_annum=income_annum,
            loan_amount=loan_amount,
            loan_term=loan_term,
            cibil_score=cibil_score,
            residential_assets_value=residential_assets_value,
            commercial_assets_value=commercial_assets_value,
            luxury_assets_value=luxury_assets_value,
            bank_asset_value=bank_asset_value,
        )

        input_data = pd.DataFrame(
            [[
                no_of_dependents,
                edu_enc,
                self_enc,
                income_annum,
                loan_amount,
                loan_term,
                cibil_score,
                residential_assets_value,
                commercial_assets_value,
                luxury_assets_value,
                bank_asset_value,
            ]],
            columns=FEATURE_NAMES,
        )

        scaled_data = scaler.transform(input_data)
        prediction = model.predict(scaled_data)[0]

        approval_prob = None
        if hasattr(model, "predict_proba"):
            approval_prob = float(model.predict_proba(scaled_data)[0][1])

        confidence_pct = (approval_prob * 100) if approval_prob is not None else (
            85.0 if prediction == 1 else 15.0
        )

        approved = prediction == 1
        insights = get_ai_insights(profile, approved, approval_prob)

        if approved:
            render_approval_result(confidence_pct)
            if HAPPY_GIF_PATH.exists():
                show_image(str(HAPPY_GIF_PATH))
        else:
            render_rejection_result(confidence_pct)
            if SAD_GIF_PATH.exists():
                show_image(str(SAD_GIF_PATH))

        render_ai_suggestions(insights)

        # =====================================
        # DOWNLOAD REPORT
        # =====================================

        report = f"""
LoanSmart Prediction Report
===========================

Prediction Result:
{"APPROVED" if approved else "REJECTED"}

Confidence Score:
{confidence_pct:.2f}%

Applicant Details
-----------------
Dependents: {no_of_dependents}
Education: {education}
Self Employed: {self_employed}
Annual Income: ₹{income_annum:,.0f}
Loan Amount: ₹{loan_amount:,.0f}
Loan Term: {loan_term} Years
CIBIL Score: {int(cibil_score)} {"(Estimated)" if dont_know_cibil else ""}

Assets
-------
Residential Assets: ₹{residential_assets_value:,.0f}
Commercial Assets: ₹{commercial_assets_value:,.0f}
Luxury Assets: ₹{luxury_assets_value:,.0f}
Bank Assets: ₹{bank_asset_value:,.0f}

Generated By:
LoanSmart AI Loan Approval Prediction System
"""

        st.download_button(
            label="📄 Download Report",
            data=report,
            file_name="LoanSmart_Report.txt",
            mime="text/plain",
        )

st.markdown("""
<div class='footer'>
🏦 LoanSmart · AI Loan Approval Prediction System · Developed by Archana
</div>
""", unsafe_allow_html=True)
