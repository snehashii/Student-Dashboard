import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("students_cleaned_rich.csv")

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")
st.title("📊 Student Performance Dashboard")

# Sidebar Filters
with st.sidebar:
    st.header("🔍 Filter Options")
    gender = st.multiselect("Gender", df["gender"].unique(), default=df["gender"].unique())
    education = st.multiselect("Parental Education", df["parental_education"].unique(), default=df["parental_education"].unique())
    lunch = st.multiselect("Lunch Type", df["lunch_type"].unique(), default=df["lunch_type"].unique())
    prep = st.multiselect("Test Preparation", df["test_preparation"].unique(), default=df["test_preparation"].unique())

# Filter Data
df_filtered = df[
    (df["gender"].isin(gender)) &
    (df["parental_education"].isin(education)) &
    (df["lunch_type"].isin(lunch)) &
    (df["test_preparation"].isin(prep))
]

# KPIs
st.subheader("🎯 Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("📐 Avg Math Score", round(df_filtered["math_score"].mean(), 1))
col2.metric("📚 Avg Reading Score", round(df_filtered["reading_score"].mean(), 1))
col3.metric("✍️ Avg Writing Score", round(df_filtered["writing_score"].mean(), 1))

# Charts
st.subheader("📈 Performance by Gender")
fig1 = px.bar(df_filtered, x="gender", y=["math_score", "reading_score", "writing_score"], barmode="group")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("📊 Average Score by Parental Education")
fig2 = px.box(df_filtered, x="parental_education", y="average_score", color="gender")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("📊 Score Distribution by Test Preparation")
fig3 = px.histogram(df_filtered, x="average_score", color="test_preparation", nbins=20)
st.plotly_chart(fig3, use_container_width=True)
