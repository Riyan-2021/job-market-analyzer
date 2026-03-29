import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from analysis.skill_analysis import analyze_skills
from analysis.salary_analysis import analyze_salary

st.title("Real-Time Job Market Analyzer")

df = pd.read_csv("data/jobs.csv")

st.subheader("Dataset Preview")
st.dataframe(df)

skill_df = analyze_skills()

st.subheader("Top Skills")

fig, ax = plt.subplots()

top_skills = skill_df.head(10)

ax.bar(
    top_skills["Skill"],
    top_skills["Frequency"]
)

plt.xticks(rotation=45)

st.pyplot(fig)

avg_salary, salary_by_location = analyze_salary()

st.subheader("Average Salary")
st.write(avg_salary)

st.subheader("Salary by Location")

fig2, ax2 = plt.subplots()

salary_by_location.plot(
    kind="bar",
    ax=ax2
)

st.pyplot(fig2)
