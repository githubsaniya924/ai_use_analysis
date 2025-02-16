import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

# Title for the Streamlit App
st.title("Streamlit and Plotly Example")

# Example DataFrame
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 15, 25],
}
df = pd.DataFrame(data)

# Display DataFrame
st.write("Here is the dataset:")
st.dataframe(df)

# Plot using Plotly
fig = px.bar(df, x="Category", y="Values", title="Bar Chart Example")
st.plotly_chart(fig)
