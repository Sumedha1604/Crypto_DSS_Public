import streamlit as st
import pandas as pd

st.title("DSS Recommendation")

st.caption(
    "Weighted Decision Support System for model selection."
)

# ------------------------
# Load DSS Scores
# ------------------------

dss = pd.read_csv(
    "outputs/dss_scores.csv"
)

best_model = dss.iloc[0]["Model"]

best_score = round(
    dss.iloc[0]["DSS_Score"],
    2
)

# ------------------------
# Decision Criteria
# ------------------------

st.subheader(
    "Decision Criteria"
)

criteria = pd.DataFrame({

    "Criteria": [

        "Accuracy",

        "F1 Score",

        "Training Time",

        "Prediction Time",

        "Interpretability"

    ],

    "Weight": [

        "30%",

        "25%",

        "15%",

        "15%",

        "15%"

    ]

})

st.dataframe(

    criteria,

    hide_index=True,

    use_container_width=True

)

st.divider()

# ------------------------
# Recommended Model
# ------------------------

c1, c2 = st.columns(2)

c1.metric(

    "Recommended Model",

    best_model

)

c2.metric(

    "DSS Score",

    best_score

)

st.divider()

# ------------------------
# Why Selected
# ------------------------

st.subheader(
    "Why was it selected?"
)

st.success(
"""
✔ Higher Accuracy

✔ Higher F1 Score

✔ Better Recall

✔ Faster Prediction Speed

✔ Highest overall DSS score
"""
)

st.divider()

# ------------------------
# Knowledge Base
# ------------------------

st.subheader(
    "Knowledge Base"
)

knowledge = pd.DataFrame({

    "Indicator": [

        "RSI",

        "MACD",

        "Volatility",

        "Lag Features"

    ],

    "Purpose": [

        "Measures market strength",

        "Detects trend momentum",

        "Measures market uncertainty",

        "Captures historical market behaviour"

    ]

})

st.dataframe(

    knowledge,

    hide_index=True,

    use_container_width=True

)

st.divider()

# ------------------------
# DSS Explanation
# ------------------------

st.subheader(
    "Final DSS Explanation"
)

st.info(
"""
The recommendation is based on multiple weighted criteria instead of a single metric.

The model with the highest DSS score is selected automatically.
"""
)