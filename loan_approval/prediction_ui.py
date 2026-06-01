"""Loan approval result and AI suggestion UI (original purple theme)."""

import streamlit as st

EXTRA_CSS = """
<style>
.ai-panel {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    padding: 1.5rem 1.75rem;
    margin-top: 1.5rem;
    border: 1px solid rgba(91, 30, 92, 0.12);
    box-shadow: 0 6px 20px rgba(91, 30, 92, 0.1);
    opacity: 1;
}
.ai-panel-header h3 { color: #5b1e5c !important; font-weight: 800 !important; }
.ai-badge {
    background: linear-gradient(135deg, #5b1e5c, #8d44ad);
    color: white;
    font-size: 0.65rem;
    font-weight: 700;
    padding: 0.2rem 0.5rem;
    border-radius: 6px;
}
.ai-summary { color: #666; line-height: 1.7; }
.suggestion-card {
    background: #faf5ff;
    border-left: 4px solid #8d44ad;
    border-radius: 0 12px 12px 0;
    padding: 0.9rem 1rem;
    margin-bottom: 0.75rem;
    opacity: 1;
}
.suggestion-card.positive { border-left-color: #16a34a; background: #f0fdf4; }
.suggestion-card.high { border-left-color: #dc2626; background: #fef2f2; }
.suggestion-title { color: #5b1e5c; font-weight: 700; }
.suggestion-detail { color: #666; font-size: 0.9rem; margin: 0; }
.risk-pill {
    display: inline-block;
    padding: 0.35rem 0.85rem;
    border-radius: 999px;
    font-size: 0.8rem;
    font-weight: 700;
    margin-bottom: 1rem;
}
.risk-low { background: #dcfce7; color: #166534; }
.risk-moderate { background: #fef9c3; color: #854d0e; }
.risk-high { background: #ffedd5; color: #c2410c; }
.risk-very-high { background: #fee2e2; color: #b91c1c; }
.confidence-bar-wrap { max-width: 420px; margin: 1rem auto 0; text-align: left; }
.confidence-label { font-size: 0.8rem; color: #666; font-weight: 600; text-transform: uppercase; }
.confidence-track { height: 10px; background: #eee; border-radius: 999px; overflow: hidden; }
.confidence-fill { height: 100%; border-radius: 999px; }
.fill-approved { background: linear-gradient(90deg, #16a34a, #22c55e); }
.fill-rejected { background: linear-gradient(90deg, #dc2626, #ef4444); }
</style>
"""


def inject_prediction_animations() -> None:
    st.markdown(EXTRA_CSS, unsafe_allow_html=True)


def render_approval_result(confidence_pct: float) -> None:
    st.markdown(
        f"""
        <div class="result-card result-approved">
            <h1>✅ LOAN APPROVED</h1>
            <p style="color:#166534;">
            Congratulations! Your loan application has been approved.
            </p>
            <div class="confidence-bar-wrap">
                <div class="confidence-label">Approval Confidence</div>
                <div class="confidence-track">
                    <div class="confidence-fill fill-approved" style="width:{confidence_pct:.0f}%;"></div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_rejection_result(confidence_pct: float) -> None:
    reject_conf = 100 - confidence_pct
    st.markdown(
        f"""
        <div class="result-card result-rejected">
            <h1>❌ LOAN REJECTED</h1>
            <p style="color:#991b1b;">
            Sorry! Your loan application has been rejected.
            </p>
            <div class="confidence-bar-wrap">
                <div class="confidence-label">Rejection Confidence</div>
                <div class="confidence-track">
                    <div class="confidence-fill fill-rejected" style="width:{reject_conf:.0f}%;"></div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _risk_class(label: str) -> str:
    return {
        "Low Risk": "risk-low",
        "Moderate Risk": "risk-moderate",
        "High Risk": "risk-high",
        "Very High Risk": "risk-very-high",
    }.get(label, "risk-moderate")


def render_ai_suggestions(insights: dict) -> None:
    cards_html = ""
    for item in insights["suggestions"]:
        priority = item.get("priority", "medium")
        card_class = "suggestion-card"
        if priority == "positive":
            card_class += " positive"
        elif priority == "high":
            card_class += " high"
        cards_html += f"""
        <div class="{card_class}">
            <div class="suggestion-title">{item['icon']} {item['title']}</div>
            <p class="suggestion-detail">{item['detail']}</p>
        </div>
        """

    st.markdown(
        f"""
        <div class="ai-panel">
            <div class="ai-panel-header">
                <span style="font-size:1.3rem;">🤖</span>
                <h3 style="display:inline;margin-left:8px;">AI Financial Advisor</h3>
                <span class="ai-badge">SMART INSIGHTS</span>
            </div>
            <span class="risk-pill {_risk_class(insights['risk_label'])}">
                Risk Score: {insights['risk_score']}/100 · {insights['risk_label']}
            </span>
            <p class="ai-summary">{insights['summary']}</p>
            {cards_html}
        </div>
        """,
        unsafe_allow_html=True,
    )
