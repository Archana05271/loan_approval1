import paths  # noqa: F401

import pandas as pd
import plotly.express as px
import streamlit as st

from chart_theme import ASSET_COLORS, EDUCATION_COLORS, STATUS_COLORS, apply_fintech_theme
from dataset_utils import load_loan_dataset
from streamlit_compat import dataframe_stretch, plotly_chart_stretch
from ui_styles import inject_global_styles

st.set_page_config(
    page_title="LoanSmart | Dashboard",
    page_icon="📊",
    layout="wide",
)

inject_global_styles()

try:
    df = load_loan_dataset()
except FileNotFoundError as exc:
    st.error(str(exc))
    st.stop()

st.markdown("""
<div class='title'>
📊 Dashboard Analytics
</div>

<div class='subtitle'>
AI-Powered Loan Insights & Financial Analytics Dashboard
</div>

<div class='badge-row'>
    <div class='badge'>📈 Smart Analytics</div>
    <div class='badge'>⚡ Real-Time Insights</div>
    <div class='badge'>🏦 Financial Dashboard</div>
    <div class='badge'>📊 Interactive Charts</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='sub-header'>
📁 Dataset Preview
</div>
""", unsafe_allow_html=True)

with st.container(border=True):
    dataframe_stretch(df.head(10))

st.markdown("<br>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

with m1:
    with st.container(border=True):
        st.metric("Total Records", f"{len(df):,}")

with m2:
    with st.container(border=True):
        st.metric("Average Income", f"₹{int(df['income_annum'].mean()):,}")

with m3:
    with st.container(border=True):
        st.metric("Average Loan", f"₹{int(df['loan_amount'].mean()):,}")

with m4:
    with st.container(border=True):
        approval_rate = (df["loan_status"] == "Approved").mean() * 100
        st.metric("Approval Rate", f"{approval_rate:.1f}%")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class='sub-header'>
📌 Loan Status Distribution
</div>
""", unsafe_allow_html=True)

with st.container(border=True):
    status_counts = df["loan_status"].value_counts().reset_index()
    status_counts.columns = ["Status", "Count"]

    fig_pie = px.pie(
        status_counts,
        values="Count",
        names="Status",
        hole=0.45,
        color="Status",
        color_discrete_map=STATUS_COLORS,
    )
    apply_fintech_theme(fig_pie, height=500)
    plotly_chart_stretch(fig_pie)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class='sub-header'>
📈 Average Loan Amount by Education
</div>
""", unsafe_allow_html=True)

with st.container(border=True):
    edu_df = df.groupby("education")["loan_amount"].mean().reset_index()

    fig_bar = px.bar(
        edu_df,
        x="loan_amount",
        y="education",
        orientation="h",
        text_auto=True,
        color="education",
        color_discrete_sequence=EDUCATION_COLORS,
    )
    apply_fintech_theme(fig_bar, height=450)
    fig_bar.update_layout(xaxis_title="Average Loan Amount", yaxis_title="Education")
    plotly_chart_stretch(fig_bar)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class='sub-header'>
📊 CIBIL Score vs Loan Amount
</div>
""", unsafe_allow_html=True)

with st.container(border=True):
    fig_scatter = px.scatter(
        df,
        x="cibil_score",
        y="loan_amount",
        color="loan_status",
        size="income_annum",
        hover_data=["education", "self_employed"],
        color_discrete_map=STATUS_COLORS,
    )
    apply_fintech_theme(fig_scatter, height=500)
    plotly_chart_stretch(fig_scatter)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class='sub-header'>
🏛️ Average Asset Distribution
</div>
""", unsafe_allow_html=True)

with st.container(border=True):
    asset_df = pd.DataFrame({
        "Asset Type": ["Residential", "Commercial", "Luxury", "Bank"],
        "Average Value": [
            df["residential_assets_value"].mean(),
            df["commercial_assets_value"].mean(),
            df["luxury_assets_value"].mean(),
            df["bank_asset_value"].mean(),
        ],
    })

    fig_assets = px.bar(
        asset_df,
        x="Average Value",
        y="Asset Type",
        orientation="h",
        text_auto=True,
        color="Asset Type",
        color_discrete_sequence=ASSET_COLORS,
    )
    apply_fintech_theme(fig_assets, height=500)
    plotly_chart_stretch(fig_assets)

st.markdown("""
<div class='footer'>
🏦 LoanSmart Dashboard · Built with Streamlit & Plotly · Developed by Archana
</div>
""", unsafe_allow_html=True)
