import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.title("Market Analysis")

st.caption(
    "Analyze historical Bitcoin market data using machine learning."
)

df = pd.read_csv(
    "data/final_btc_dataset.csv"
)

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

    trend = (
        "Bullish"
        if bullish_count > bearish_count
        else "Bearish"
    )

    confidence = round(

        np.mean(

            np.max(
                probabilities,
                axis=1
            )

        ) * 100,

        2

    )

    with open(
        "outputs/market_insights.txt",
        "r"
    ) as f:

        insights = f.read()

    if "BUY / HOLD" in insights:

        recommendation = "Buy / Hold"

    elif "SELL / WAIT" in insights:

        recommendation = "Sell / Wait"

    else:

        recommendation = "Hold"

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