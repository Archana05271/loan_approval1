"""Streamlit width='stretch' helpers with version fallback."""

from __future__ import annotations

import streamlit as st


def show_image(image, **kwargs) -> None:
    kwargs.setdefault("width", "stretch")
    try:
        st.image(image, **kwargs)
    except (TypeError, ValueError):
        kwargs.pop("width", None)
        st.image(image, use_container_width=True, **kwargs)


def plotly_chart_stretch(fig, **kwargs) -> None:
    kwargs.setdefault("width", "stretch")
    try:
        st.plotly_chart(fig, **kwargs)
    except (TypeError, ValueError):
        kwargs.pop("width", None)
        st.plotly_chart(fig, use_container_width=True, **kwargs)


def dataframe_stretch(data, **kwargs) -> None:
    kwargs.setdefault("width", "stretch")
    try:
        st.dataframe(data, **kwargs)
    except (TypeError, ValueError):
        kwargs.pop("width", None)
        st.dataframe(data, use_container_width=True, **kwargs)


def button(label: str, **kwargs):
    kwargs.setdefault("width", "stretch")
    try:
        return st.button(label, **kwargs)
    except (TypeError, ValueError):
        kwargs.pop("width", None)
        return st.button(label, use_container_width=True, **kwargs)
