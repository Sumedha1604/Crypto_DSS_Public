import streamlit as st
import pandas as pd

st.title("DSS Recommendation")

st.caption(
    "Weighted decision support system for model recommendation."
)
priority = st.selectbox(

    "What would you like to prioritize?",

    [

        "Balanced Performance",

        "Speed",

        "Interpretability"

    ]

)

if priority == "Speed":

    st.info(
        "Priority: Faster prediction performance."
    )

elif priority == "Interpretability":

    st.info(
        "Priority: Easier to understand models."
    )

else:

    st.info(
        "Priority: Balanced overall performance."
    )
dss = pd.read_csv(
    "outputs/dss_scores.csv"
)

best_model = dss.iloc[0]["Model"]

st.subheader(
    "Decision Criteria"
)

criteria = pd.DataFrame({

    "Criteria":[

        "Accuracy",

        "F1 Score",

        "Training Time",

        "Prediction Time",

        "Interpretability"

    ],

    "Weight":[

        "30%",

        "25%",

        "15%",

        "15%",

        "15%"

    ]

})

st.table(criteria)

st.divider()

st.subheader(
    "DSS Ranking"
)

ranking = dss[["Model", "DSS_Score"]]

st.dataframe(
    ranking,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader(
    "Recommended Model"
)

st.success(
    best_model
)

st.divider()

st.subheader(
    "Why was it selected?"
)
st.divider()

st.subheader(
    "Weighted DSS Matrix"
)

matrix = dss[[
    "Model",

    "Accuracy",

    "F1",

    "Training_Time",

    "Prediction_Time",

    "DSS_Score"

]]

display = matrix.copy()

display["Accuracy"] = (
    display["Accuracy"] * 100
).round(2)

display["F1"] = (
    display["F1"] * 100
).round(2)

display["Training_Time"] = (
    display["Training_Time"]
).round(2)

display["Prediction_Time"] = (
    display["Prediction_Time"]
).round(4)

display["DSS_Score"] = (
    display["DSS_Score"]
).round(2)

st.dataframe(

    display,

    use_container_width=True,

    hide_index=True

)
st.markdown(
"""

• Higher Accuracy

• Higher F1 Score

• Better Recall

• Faster Prediction Speed

• Highest overall DSS score

"""
)

st.divider()

st.subheader(
    "Knowledge Base"
)

st.info(
"""

RSI → Measures market strength

MACD → Detects trend momentum

Volatility → Measures market uncertainty

Lag Features → Capture historical market behaviour

"""
)

st.divider()

st.subheader(
    "Final DSS Explanation"
)

st.success(
"""

The recommendation is based on multiple weighted criteria rather than a single performance metric.

The model with the highest DSS score is selected.

"""
)
st.divider()

st.subheader(
    "Weighted DSS Matrix"
)

matrix = dss[[
    "Model",
    "Accuracy",
    "F1",
    "Training_Time",
    "Prediction_Time",
    "DSS_Score"
]]

display = matrix.copy()

display["Accuracy"] = (
    display["Accuracy"] * 100
).round(2)

display["F1"] = (
    display["F1"] * 100
).round(2)

display["Training_Time"] = (
    display["Training_Time"]
).round(2)

display["Prediction_Time"] = (
    display["Prediction_Time"]
).round(4)

display["DSS_Score"] = (
    display["DSS_Score"]
).round(2)

st.dataframe(
    display,
    use_container_width=True,
    hide_index=True
)