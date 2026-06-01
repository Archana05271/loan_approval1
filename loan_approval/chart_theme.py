"""Plotly chart styling — original purple theme."""

from __future__ import annotations

import plotly.graph_objects as go

PRIMARY = "#5b1e5c"
PRIMARY_LIGHT = "#c8a6c9"
SUCCESS = "#16a34a"
ERROR = "#dc2626"
GRID = "rgba(91, 30, 92, 0.08)"


def apply_fintech_theme(fig: go.Figure, height: int | None = None) -> go.Figure:
    layout = dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Poppins, sans-serif", color="#333333", size=13),
        margin=dict(t=20, b=20, l=20, r=20),
    )
    if height is not None:
        layout["height"] = height
    fig.update_layout(**layout)
    fig.update_xaxes(gridcolor=GRID, linecolor="#e5e5e5")
    fig.update_yaxes(gridcolor=GRID, linecolor="#e5e5e5")
    return fig


STATUS_COLORS = {"Approved": PRIMARY, "Rejected": PRIMARY_LIGHT}
EDUCATION_COLORS = [PRIMARY, PRIMARY_LIGHT]
ASSET_COLORS = ["#5b1e5c", "#7b4a7c", "#9b6b9c", "#b38cb4"]
