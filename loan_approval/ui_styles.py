"""Original LoanSmart purple theme (with safe Streamlit rendering)."""

import streamlit as st

FONT_LINK = (
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    'family=Poppins:wght@300;400;500;600;700;800&display=swap">'
)

GLOBAL_CSS = """
<style>
:root {
    --primary: #5b1e5c;
    --primary-light: #8d44ad;
    --primary-dark: #3d1240;
    --accent: #c084fc;
    --surface: rgba(255, 255, 255, 0.95);
    --text: #333333;
    --text-muted: #666666;
    --success: #16a34a;
    --error: #dc2626;
    --radius-lg: 24px;
    --radius-xl: 28px;
    --shadow-sm: 0 4px 14px rgba(91, 30, 92, 0.08);
    --shadow-md: 0 12px 28px rgba(91, 30, 92, 0.14);
    --gradient-bg: linear-gradient(135deg, #f8f5fb, #f3edf7, #ffffff);
    --gradient-hero: linear-gradient(135deg, #5b1e5c, #7b2d7d, #8d44ad);
}

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: var(--gradient-bg);
    position: relative;
}

.stApp::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse 70% 50% at 10% 20%, rgba(141, 68, 173, 0.08), transparent 50%),
        radial-gradient(ellipse 60% 40% at 90% 80%, rgba(91, 30, 92, 0.06), transparent 50%);
    pointer-events: none;
    z-index: 0;
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
.block-container {
    position: relative;
    z-index: 1;
}

.block-container {
    padding-top: 1rem;
    padding-left: clamp(1rem, 3vw, 2rem);
    padding-right: clamp(1rem, 3vw, 2rem);
    padding-bottom: 2rem;
    max-width: 1400px;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #5b1e5c, #7b2d7d) !important;
    border-right: 2px solid rgba(255, 255, 255, 0.08);
}

[data-testid="stSidebar"] * {
    color: white !important;
}

[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover {
    background: rgba(255, 255, 255, 0.12) !important;
    border-radius: 12px;
}

.main-title, .title {
    text-align: center;
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 800;
    color: var(--primary);
    margin-bottom: 0.5rem;
    opacity: 1;
}

.sub-title, .subtitle {
    text-align: center;
    color: var(--text-muted);
    font-size: clamp(1rem, 2.5vw, 1.35rem);
    margin-bottom: 1.25rem;
    opacity: 1;
}

.sub-header, .section-title {
    font-size: clamp(1.25rem, 3vw, 1.65rem);
    color: var(--primary);
    font-weight: 800;
    margin: 1.5rem 0 1rem;
    opacity: 1;
}

.section-title {
    text-align: center;
    margin: 2.5rem 0 1.5rem;
}

.badge-row {
    display: flex;
    justify-content: center;
    gap: 0.75rem;
    flex-wrap: wrap;
    margin-bottom: 1.75rem;
    opacity: 1;
}

.badge {
    background: white;
    padding: 0.55rem 1.1rem;
    border-radius: 30px;
    color: var(--primary);
    font-size: 0.85rem;
    font-weight: 700;
    box-shadow: var(--shadow-sm);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    opacity: 1;
}

.badge:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-md);
}

.hero {
    background: var(--gradient-hero);
    padding: clamp(2rem, 5vw, 3.5rem) clamp(1.25rem, 4vw, 2rem);
    border-radius: var(--radius-xl);
    text-align: center;
    color: white;
    margin-bottom: 2rem;
    box-shadow: var(--shadow-md);
    position: relative;
    overflow: hidden;
    opacity: 1;
}

.hero .title {
    color: white;
    -webkit-text-fill-color: white;
}

.hero .subtitle {
    color: #f3e8ff;
}

.hero .badge {
    background: rgba(255, 255, 255, 0.15);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.25);
    -webkit-text-fill-color: white;
}

.card, .step-card, .grid-box, .stat-box {
    background: var(--surface);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    box-shadow: var(--shadow-sm);
    transition: transform 0.35s ease, box-shadow 0.35s ease;
    min-height: 200px;
    opacity: 1;
    border: 1px solid rgba(255, 255, 255, 0.8);
}

.card {
    border-top: 5px solid var(--primary);
}

.card:hover, .step-card:hover, .grid-box:hover, .stat-box:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-md);
}

.card h2, .grid-box h4 {
    color: var(--primary) !important;
    font-size: 1.4rem;
    margin-bottom: 0.75rem;
    font-weight: 700;
}

.card p, .grid-box p, .step-text {
    color: var(--text-muted) !important;
    font-size: 0.95rem;
    line-height: 1.75;
}

.step-card {
    text-align: center;
    padding: 1.5rem;
}

.step-title {
    color: var(--primary);
    font-size: 1.15rem;
    font-weight: 700;
    margin-top: 0.75rem;
}

.stats-row, .stat-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 1.25rem;
    margin: 2rem 0;
}

.stat-box {
    text-align: center;
    padding: 1.25rem;
}

.stat-number {
    font-size: clamp(1.75rem, 4vw, 2.25rem);
    font-weight: 800;
    color: var(--primary);
    opacity: 1;
}

.stat-label {
    color: var(--text-muted);
    font-size: 0.9rem;
    margin-top: 0.35rem;
}

.hero-card {
    background: var(--surface);
    border-radius: var(--radius-xl);
    padding: 2rem;
    box-shadow: var(--shadow-sm);
    border-left: 8px solid var(--primary);
    margin-bottom: 2rem;
    opacity: 1;
}

.hero-card h2 {
    color: var(--primary) !important;
    font-weight: 800;
}

.hero-card p {
    color: #444444 !important;
    line-height: 1.85;
}

.stack-container {
    background: var(--surface);
    padding: 2rem 1.5rem;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-sm);
    text-align: center;
    opacity: 1;
}

.tech-badge {
    display: inline-block;
    background: linear-gradient(135deg, #ede3ef, #f7f1f9);
    color: var(--primary) !important;
    padding: 0.6rem 1rem;
    border-radius: 30px;
    font-weight: 700;
    font-size: 0.85rem;
    margin: 0.4rem;
    box-shadow: var(--shadow-sm);
    opacity: 1;
}

.author-card {
    background: linear-gradient(135deg, #1f1f2f, #2d2d44);
    padding: 2rem;
    border-radius: var(--radius-lg);
    text-align: center;
    margin-top: 2rem;
    box-shadow: var(--shadow-md);
    opacity: 1;
}

.author-card h3 {
    color: #d5b4d7 !important;
    font-size: 0.85rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
}

.author-card p {
    color: white !important;
    font-size: 1.75rem;
    font-weight: 800;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--surface) !important;
    padding: 1.25rem !important;
    border-radius: var(--radius-lg) !important;
    box-shadow: var(--shadow-sm) !important;
    border: 1px solid rgba(91, 30, 92, 0.08) !important;
    opacity: 1 !important;
}

div[data-testid="stMetricLabel"] p {
    color: var(--text-muted) !important;
    font-weight: 600 !important;
}

div[data-testid="stMetricValue"] div {
    color: var(--primary) !important;
    -webkit-text-fill-color: var(--primary) !important;
    font-weight: 800 !important;
    opacity: 1 !important;
}

.stButton > button {
    background: linear-gradient(135deg, #5b1e5c, #8d44ad) !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    height: 3.25rem !important;
    min-width: 220px !important;
    font-weight: 700 !important;
    box-shadow: 0 6px 18px rgba(91, 30, 92, 0.25) !important;
    opacity: 1 !important;
    transition: transform 0.3s ease !important;
}

.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 22px rgba(91, 30, 92, 0.3) !important;
}

label p {
    color: var(--text) !important;
    font-weight: 600 !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    border-radius: 12px !important;
}

[data-testid="stImage"] img {
    border-radius: var(--radius-lg) !important;
    box-shadow: var(--shadow-sm) !important;
    opacity: 1 !important;
}

.stSuccess {
    background: rgba(91, 30, 92, 0.08) !important;
    border: 1px solid var(--primary) !important;
    border-radius: 14px !important;
}

.result-card {
    padding: 2rem;
    border-radius: var(--radius-lg);
    text-align: center;
    margin-top: 1.5rem;
    opacity: 1;
}

.result-approved {
    background: linear-gradient(135deg, #ecfff3, #d1fae5);
    border-left: 8px solid var(--success);
}

.result-rejected {
    background: linear-gradient(135deg, #fff1f1, #fee2e2);
    border-left: 8px solid var(--error);
}

.result-approved h1 { color: var(--success) !important; }
.result-rejected h1 { color: var(--error) !important; }

.js-plotly-plot { border-radius: 16px !important; }

.footer {
    text-align: center;
    color: #888888;
    font-size: 0.875rem;
    margin-top: 2.5rem;
    padding: 1rem;
    opacity: 1;
}

[data-testid="stMarkdownContainer"] div,
[data-testid="stMarkdown"] div {
    opacity: 1 !important;
}

@media (prefers-reduced-motion: no-preference) {
    .card, .step-card, .stat-box, .grid-box {
        animation: fadeInUp 0.7s ease forwards;
    }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 768px) {
    .stButton > button { width: 100% !important; min-width: unset !important; }
    .stats-row, .stat-row { grid-template-columns: repeat(2, 1fr); }
}
</style>
"""


def inject_global_styles() -> None:
    st.markdown(FONT_LINK, unsafe_allow_html=True)
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
