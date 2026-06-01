"""Rule-based AI insights for loan approval predictions."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ApplicantProfile:
    no_of_dependents: int
    education: str
    self_employed: str
    income_annum: float
    loan_amount: float
    loan_term: float
    cibil_score: float
    residential_assets_value: float
    commercial_assets_value: float
    luxury_assets_value: float
    bank_asset_value: float


def _total_assets(profile: ApplicantProfile) -> float:
    return (
        profile.residential_assets_value
        + profile.commercial_assets_value
        + profile.luxury_assets_value
        + profile.bank_asset_value
    )


def compute_risk_score(profile: ApplicantProfile) -> int:
    """Return a 0–100 risk score (higher = riskier)."""
    score = 0

    if profile.cibil_score < 550:
        score += 35
    elif profile.cibil_score < 650:
        score += 22
    elif profile.cibil_score < 700:
        score += 10

    if profile.income_annum > 0:
        ratio = profile.loan_amount / profile.income_annum
        if ratio > 5:
            score += 25
        elif ratio > 3:
            score += 15
        elif ratio > 2:
            score += 8
    else:
        score += 20

    if profile.no_of_dependents >= 5:
        score += 12
    elif profile.no_of_dependents >= 3:
        score += 6

    if profile.education == "Not Graduate":
        score += 8

    if profile.self_employed == "Yes":
        score += 5

    if profile.bank_asset_value < 50000:
        score += 10
    elif profile.bank_asset_value < 200000:
        score += 5

    assets = _total_assets(profile)
    if profile.loan_amount > 0 and assets < profile.loan_amount * 0.3:
        score += 12

    if profile.loan_term > 20:
        score += 5

    return min(100, score)


def get_strengths(profile: ApplicantProfile) -> list[str]:
    strengths = []

    if profile.cibil_score >= 750:
        strengths.append("Excellent CIBIL score — strong creditworthiness signal.")
    elif profile.cibil_score >= 700:
        strengths.append("Good CIBIL score supports approval confidence.")

    if profile.income_annum > 0 and profile.loan_amount / profile.income_annum <= 2:
        strengths.append("Healthy income-to-loan ratio — manageable debt burden.")

    if profile.education == "Graduate":
        strengths.append("Graduate education correlates with stable repayment patterns.")

    if _total_assets(profile) >= profile.loan_amount:
        strengths.append("Total asset value covers the requested loan amount.")

    if profile.bank_asset_value >= 500000:
        strengths.append("Strong bank assets indicate financial liquidity.")

    if profile.no_of_dependents <= 2:
        strengths.append("Low dependency count reduces household financial strain.")

    return strengths[:4]


def get_improvement_tips(profile: ApplicantProfile) -> list[dict]:
    """Return prioritized tips: {icon, title, detail, priority}."""
    tips = []

    if profile.cibil_score < 650:
        tips.append({
            "icon": "📈",
            "title": "Improve CIBIL Score",
            "detail": (
                f"Your score is {profile.cibil_score:.0f}. Aim for 700+ by paying EMIs on time, "
                "keeping credit utilization below 30%, and clearing outstanding dues."
            ),
            "priority": "high",
        })

    if profile.income_annum > 0 and profile.loan_amount > profile.income_annum * 2:
        tips.append({
            "icon": "💰",
            "title": "Reduce Loan Amount or Increase Income",
            "detail": (
                "Requested loan is high relative to annual income. Consider a smaller loan, "
                "adding a co-applicant, or documenting additional income sources."
            ),
            "priority": "high",
        })

    if profile.bank_asset_value < 200000:
        tips.append({
            "icon": "🏛️",
            "title": "Build Bank Savings",
            "detail": (
                "Low bank assets weaken your profile. Maintain 6+ months of EMI as savings "
                "and show consistent account balances before reapplying."
            ),
            "priority": "medium",
        })

    if profile.no_of_dependents > 3:
        tips.append({
            "icon": "👨‍👩‍👧",
            "title": "Highlight Stable Household Income",
            "detail": (
                "Multiple dependents increase perceived risk. Provide proof of spouse or "
                "family income to offset dependency burden."
            ),
            "priority": "medium",
        })

    if profile.education == "Not Graduate":
        tips.append({
            "icon": "🎓",
            "title": "Strengthen Application Profile",
            "detail": (
                "Add professional certifications, stable employment history, or collateral "
                "documentation to compensate for education factor."
            ),
            "priority": "low",
        })

    if profile.self_employed == "Yes":
        tips.append({
            "icon": "💼",
            "title": "Submit Business Financials",
            "detail": (
                "Self-employed applicants should include 2–3 years of ITR, GST returns, "
                "and profit statements to prove repayment capacity."
            ),
            "priority": "medium",
        })

    assets = _total_assets(profile)
    if profile.loan_amount > 0 and assets < profile.loan_amount * 0.5:
        tips.append({
            "icon": "🏠",
            "title": "Offer Collateral or Co-Signer",
            "detail": (
                "Asset backing is limited. Property documents, fixed deposits, or a "
                "co-applicant with strong credit can improve approval odds."
            ),
            "priority": "high",
        })

    priority_order = {"high": 0, "medium": 1, "low": 2}
    tips.sort(key=lambda t: priority_order.get(t["priority"], 3))
    return tips


def get_ai_insights(
    profile: ApplicantProfile,
    approved: bool,
    approval_probability: float | None = None,
) -> dict:
    """Generate AI-style summary and suggestions for the prediction outcome."""
    risk_score = compute_risk_score(profile)
    strengths = get_strengths(profile)
    tips = get_improvement_tips(profile)

    prob_text = ""
    if approval_probability is not None:
        pct = approval_probability * 100
        prob_text = f" Model confidence: {pct:.1f}% approval probability."

    if approved:
        summary = (
            "Our AI analysis indicates a favorable risk profile. Your financial indicators "
            "align with patterns seen in approved applications."
            + prob_text
        )
        suggestions = []
        if strengths:
            suggestions.append({
                "icon": "✨",
                "title": "Key Strengths",
                "detail": " · ".join(strengths),
                "priority": "positive",
            })
        suggestions.append({
            "icon": "📋",
            "title": "Next Steps",
            "detail": (
                "Prepare income proof, identity documents, and asset statements for "
                "final verification. Maintain your CIBIL score until disbursement."
            ),
            "priority": "positive",
        })
        if profile.cibil_score < 720:
            suggestions.append({
                "icon": "💡",
                "title": "Pro Tip",
                "detail": (
                    "Even with approval, avoid new credit inquiries before loan disbursal "
                    "to keep your score stable."
                ),
                "priority": "medium",
            })
    else:
        summary = (
            "Our AI risk engine flagged concerns based on credit, income, and asset patterns "
            "similar to rejected applications."
            + prob_text
        )
        suggestions = []
        for tip in tips[:5]:
            suggestions.append(tip)
        if not suggestions:
            suggestions.append({
                "icon": "🔄",
                "title": "Reapply After 3–6 Months",
                "detail": (
                    "Improve overall financial health, reduce existing debt, and reapply "
                    "with updated documentation."
                ),
                "priority": "medium",
            })

    return {
        "summary": summary,
        "risk_score": risk_score,
        "risk_label": _risk_label(risk_score),
        "strengths": strengths,
        "suggestions": suggestions,
    }


def _risk_label(score: int) -> str:
    if score <= 25:
        return "Low Risk"
    if score <= 50:
        return "Moderate Risk"
    if score <= 75:
        return "High Risk"
    return "Very High Risk"
