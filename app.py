# STUDENT PERFORMANCE PROGRESSION & RISK ANALYZER
# Streamlit Deployment Version

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# PAGE CONFIG
st.set_page_config(
    page_title="Student Performance Risk Analyzer",
    layout="wide"
)

st.title("📊 Student Performance Progression & Risk Analyzer")
st.markdown("**Major Python Project | Academic Analytics**")

# CREATE SAMPLE DATA
data = {
    "Student": ["Amit","Amit","Amit","Amit","Amit","Amit",
                "Neha","Neha","Neha","Neha","Neha","Neha",
                "Rahul","Rahul","Rahul","Rahul","Rahul","Rahul"],
    "Semester": [1,2,3,1,2,3,
                 1,2,3,1,2,3,
                 1,2,3,1,2,3],
    "Subject": ["Math","Math","Math","Physics","Physics","Physics",
                "Math","Math","Math","Physics","Physics","Physics",
                "Math","Math","Math","Physics","Physics","Physics"],
    "Marks": [65,70,68,60,62,58,
              85,88,90,80,82,85,
              45,50,48,42,40,38],
    "Attendance": [72,75,70,68,70,65,
                   90,92,95,88,90,92,
                   55,58,52,50,48,45]
}

df = pd.DataFrame(data)

# SHOW DATA
st.subheader("📄 Student Dataset")
st.dataframe(df)

# PERFORMANCE TREND
st.subheader("📈 Performance Trend Over Semesters")

trend = df.groupby(["Student","Semester"])["Marks"].mean().reset_index()

fig1, ax1 = plt.subplots()
sns.lineplot(data=trend, x="Semester", y="Marks", hue="Student", marker="o", ax=ax1)
ax1.set_title("Student Performance Progression")
st.pyplot(fig1)

# SUBJECT DIFFICULTY INDEX
st.subheader("📚 Subject Difficulty Index")

subject_difficulty = df.groupby("Subject")["Marks"].mean().reset_index()
subject_difficulty["Difficulty Index"] = 100 - subject_difficulty["Marks"]

st.dataframe(subject_difficulty)

# CONSISTENCY SCORE

st.subheader("📊 Consistency Score (Standard Deviation)")

consistency = df.groupby("Student")["Marks"].std().reset_index()
consistency.rename(columns={"Marks":"Consistency Score"}, inplace=True)

st.dataframe(consistency)

# ATTENDANCE vs MARKS CORRELATION
st.subheader("🔗 Attendance vs Marks Correlation")

correlation = df["Marks"].corr(df["Attendance"])
st.metric(label="Correlation Coefficient", value=round(correlation, 2))

fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x="Attendance", y="Marks", hue="Student", ax=ax2)
ax2.set_title("Attendance vs Marks Relationship")
st.pyplot(fig2)

# DROPOUT RISK ANALYSIS
st.subheader("⚠️ Dropout Risk Analysis")

risk_result = []

for student in df["Student"].unique():
    student_data = df[df["Student"] == student]
    avg_marks = student_data["Marks"].mean()
    avg_attendance = student_data["Attendance"].mean()

    if avg_marks < 50 or avg_attendance < 60:
        risk = "HIGH RISK"
    elif avg_marks < 65 or avg_attendance < 75:
        risk = "MEDIUM RISK"
    else:
        risk = "LOW RISK"

    risk_result.append([student, avg_marks, avg_attendance, risk])

risk_df = pd.DataFrame(
    risk_result,
    columns=["Student","Average Marks","Average Attendance","Risk Level"]
)

st.dataframe(risk_df)

# BOX PLOT
st.subheader("📦 Marks Distribution by Subject")

fig3, ax3 = plt.subplots()
sns.boxplot(data=df, x="Subject", y="Marks", ax=ax3)
ax3.set_title("Marks Distribution")
st.pyplot(fig3)

# FOOTER
st.success("✅ Project executed successfully. Academic risks identified.")
