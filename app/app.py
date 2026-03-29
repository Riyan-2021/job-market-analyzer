
import streamlit as st
import pandas as pd

st.title("Job Market Analyzer Dashboard")

df = pd.read_csv("data/sample_jobs.csv")

st.subheader("Job Data")
st.dataframe(df)

st.subheader("Top Skills")
skills_series = df['skills'].str.split(", ").explode()
skill_counts = skills_series.value_counts()

st.bar_chart(skill_counts)
