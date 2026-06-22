import streamlit as st
import pandas as pd

st.title("Model Comparison")

st.caption(
    "Performance comparison of machine learning models."
)

results = pd.read_csv(
    "outputs/model_results.csv"
)

metric_options = [

    "Accuracy",

    "Precision",

    "Recall",

    "F1",

    "Training_Time",

    "Prediction_Time"

]

selected_metrics = st.multiselect(

    "Select Metrics",

    metric_options,

    default=[

        "Accuracy",

        "F1"

    ]

)

columns = ["Model"] + selected_metrics

display = results[columns].copy()

percentage_metrics = [

    "Accuracy",

    "Precision",

    "Recall",

    "F1"

]

for col in percentage_metrics:

    if col in display.columns:

        display[col] = (
            display[col] * 100
        ).round(2)

if "Training_Time" in display.columns:

    display["Training_Time"] = (
        display["Training_Time"]
    ).round(2)

if "Prediction_Time" in display.columns:

    display["Prediction_Time"] = (
        display["Prediction_Time"]
    ).round(4)

st.dataframe(

    display,

    use_container_width=True,

    hide_index=True

)

st.divider()

winner = results.loc[
    results["Accuracy"].idxmax(),
    "Model"
]

st.success(
    f"Final DSS Winner: {winner}"
)