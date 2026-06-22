import streamlit as st

st.set_page_config(
    page_title="",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Knowledge-Rich Crypto DSS") 

st.caption(
    ""
)

st.divider()

st.write(
    """
Welcome to the Bitcoin Decision Support System.

Use the pages on the left to navigate through the application.
"""
)

c1, c2, c3 = st.columns(3)

c1.metric("Models", 2)

c2.metric("Dataset", "53,962")

c3.metric("Asset", "Bitcoin")