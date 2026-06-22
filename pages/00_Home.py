import streamlit as st

st.title("Project Overview")

st.subheader(
    "Knowledge-Rich Crypto Decision Support System"
)

st.write(
    """
This application recommends the most suitable machine learning model
for Bitcoin price movement prediction using a weighted Decision Support System (DSS).
"""
)

st.divider()

st.subheader("Project Workflow")

st.markdown(
"""

1. Historical Bitcoin Data

2. Data Preprocessing

3. Feature Engineering

4. Machine Learning Models

5. Weighted DSS Matrix

6. Knowledge Base

7. Final Recommendation

"""
)

st.divider()

st.subheader("Models Used")

c1, c2 = st.columns(2)

c1.info(
    "Random Forest"
)

c2.info(
    "Gradient Boosting"
)

st.divider()

st.subheader("Decision Criteria")

st.markdown(
"""

• Accuracy

• F1 Score

• Training Time

• Prediction Time

• Interpretability

"""
)

st.divider()

st.subheader("System Architecture")

st.markdown(
"""

Data Acquisition

↓

Data Processing

↓

Modeling Layer

↓

DSS Layer

↓

Decision Output

"""
)
st.divider()

st.subheader(
    "Models Used"
)

c1, c2 = st.columns(2)

c1.info(
    "Random Forest"
)

c2.info(
    "Gradient Boosting"
)

st.divider()

st.subheader(
    "Decision Criteria"
)

st.markdown(
"""

• Accuracy

• F1 Score

• Training Time

• Prediction Time

• Interpretability

"""
)