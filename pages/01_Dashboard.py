import streamlit as st
import pandas as pd
import plotly.graph_objects as go

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

# Summary values

dataset_price = df["Close"].iloc[-1]

dataset_date = df["Date"].iloc[-1]

best_model = dss.iloc[0]["Model"]

total_records = len(df)

# Top cards

c1, c2, c3 = st.columns(3)

c1.metric(
    "Dataset Closing Price",
    f"${dataset_price:,.0f}"
)

c2.metric(
    "Best Model",
    best_model
)

c3.metric(
    "Records",
    total_records
)
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
    len(df)
)

c4.metric(
    "DSS Score",
    round(
        dss.iloc[0]["DSS_Score"],
        2
    )
)
st.caption(
    f"Last available record in dataset: {dataset_date}"
)

st.divider()

# Interactive selector

st.subheader(
    "Bitcoin Price Trend"
)

view = st.selectbox(

    "View Data",

    [

        "Last 30 Records",

        "Last 100 Records",

        "Last 500 Records",

        "Entire Dataset"

    ]

)

if view == "Last 30 Records":

    chart_df = df.tail(30)

elif view == "Last 100 Records":

    chart_df = df.tail(100)

elif view == "Last 500 Records":

    chart_df = df.tail(500)

else:

    chart_df = df

# Graph

fig = go.Figure()

fig.add_trace(

    go.Scatter(

        x=chart_df["Date"],

        y=chart_df["Close"],

        mode="lines",

        name="Bitcoin"

    )

)

fig.update_layout(

    height=450,

    xaxis_title="",

    yaxis_title="Price (USD)",

    hovermode="x unified"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

st.divider()

# DSS summary

st.subheader(
    "Decision Support Summary"
)

st.success(
    f"Recommended Model: {best_model}"
)