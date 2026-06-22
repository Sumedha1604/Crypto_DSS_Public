import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Market Dashboard")

st.caption(
    "Overview of historical Bitcoin market data and DSS outputs."
)

# Load data

df = pd.read_csv(
    "data/final_btc_dataset.csv"
)

dss = pd.read_csv(
    "outputs/dss_scores.csv"
)

# Values

latest_price = df["Close"].iloc[-1]

best_model = dss.iloc[0]["Model"]

dss_score = round(
    dss.iloc[0]["DSS_Score"],
    2
)

records = len(df)

# Metrics

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Latest Price",
    f"${latest_price:,.0f}"
)

c2.metric(
    "Best Model",
    best_model
)

c3.metric(
    "Records",
    records
)

c4.metric(
    "DSS Score",
    dss_score
)

st.divider()

# Closing Price Chart

st.subheader(
    "Bitcoin Closing Price Trend"
)

chart_data = df.tail(300)

fig = px.line(
    chart_data,
    y="Close"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# Volume Chart

st.subheader(
    "Bitcoin Trading Volume"
)

fig2 = px.line(
    chart_data,
    y="Volume BTC"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

# Dataset Preview

st.subheader(
    "Dataset Preview"
)

st.dataframe(
    df.tail(10),
    use_container_width=True
)