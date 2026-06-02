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

st.set_page_config(
    page_title="Loan Prediction",
    page_icon="🏦",
    layout="wide",
)

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
        cibil_score = st.number_input(
            "📈 CIBIL Score",
            min_value=300.0,
            max_value=900.0,
            value=650.0,
        )
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
            st.balloons()
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
CIBIL Score: {cibil_score}

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