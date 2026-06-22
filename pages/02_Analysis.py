import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.title("Market Analysis")

st.caption(
    "Analyze historical Bitcoin market data using machine learning."
)

# ------------------------
# Load Dataset
# ------------------------

df = pd.read_csv(
    "data/final_btc_dataset.csv"
)

# ------------------------
# User Input
# ------------------------

window = st.slider(
    "Historical Bitcoin Records",
    min_value=50,
    max_value=500,
    value=100,
    step=10
)

st.info(
    "Public deployment uses Gradient Boosting."
)

# ------------------------
# Run Analysis
# ------------------------

if st.button(
    "Analyze Market",
    use_container_width=True
):

    model = joblib.load(
        "models/gradient_boosting.pkl"
    )

    features = [

        "Open",

        "High",

        "Low",

        "Close",

        "Volume BTC",

        "Volume USDT",

        "tradecount",

        "MA10",

        "EMA10",

        "RSI",

        "MACD",

        "Volatility",

        "Lag1",

        "Lag2",

        "Lag3"

    ]

    selected = df.tail(window)

    X = selected[features]

    predictions = model.predict(X)

    probabilities = model.predict_proba(X)

    bullish_count = np.sum(
        predictions == 1
    )

    bearish_count = np.sum(
        predictions == 0
    )

    # ------------------------
    # Trend
    # ------------------------

    if bullish_count > bearish_count:

        trend = "Bullish"

    elif bearish_count > bullish_count:

        trend = "Bearish"

    else:

        trend = "Neutral"

    # ------------------------
    # Confidence
    # ------------------------

    confidence = round(

        np.mean(

            np.max(
                probabilities,
                axis=1
            )

        ) * 100,

        2

    )

    # ------------------------
    # Recommendation
    # ------------------------

    if bullish_count > bearish_count:

        recommendation = "Buy / Hold"

        outlook = "Bullish"

    elif bearish_count > bullish_count:

        recommendation = "Sell / Wait"

        outlook = "Bearish"

    else:

        recommendation = "Hold"

        outlook = "Neutral"

    # ------------------------
    # Metrics
    # ------------------------

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Market Trend",
        trend
    )

    c2.metric(
        "Confidence",
        f"{confidence}%"
    )

    c3.metric(
        "Recommendation",
        recommendation
    )

    st.divider()

    c4, c5 = st.columns(2)

    c4.metric(
        "Bullish Records",
        bullish_count
    )

    c5.metric(
        "Bearish Records",
        bearish_count
    )

    # ------------------------
    # Dynamic Insights
    # ------------------------

    insights = f"""
Bullish Signals: {bullish_count}

Bearish Signals: {bearish_count}

Market Outlook: {outlook}

Suggested Action: {recommendation}
"""

    st.divider()

    st.subheader(
        "Market Insights"
    )

    st.info(
        insights
    )

else:

    st.info(
        "Choose historical records and click Analyze Market."
    )