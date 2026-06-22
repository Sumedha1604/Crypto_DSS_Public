import streamlit as st
import pandas as pd
import plotly.express as px

st.title(
    "Model Comparison"
)

comparison = pd.read_csv(
    "outputs/model_results.csv"
)

st.subheader(
    "Performance Metrics"
)

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader(
    "Accuracy Comparison"
)

fig = px.bar(
    comparison,
    x="Model",
    y="Accuracy"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader(
    "F1 Score Comparison"
)

fig2 = px.bar(
    comparison,
    x="Model",
    y="F1"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

winner = comparison.sort_values(
    "Accuracy",
    ascending=False
).iloc[0]["Model"]

st.success(
    f"Final DSS Winner: {winner}"
)