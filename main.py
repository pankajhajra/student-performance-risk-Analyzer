
# STUDENT PERFORMANCE PROGRESSION & RISK ANALYZER
# Major Python Project (Single File)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# PERFORMANCE TREND ANALYSIS
trend = df.groupby(["Student","Semester"])["Marks"].mean().reset_index()

# SUBJECT DIFFICULTY INDEX
subject_difficulty = df.groupby("Subject")["Marks"].mean().reset_index()
subject_difficulty["Difficulty_Index"] = 100 - subject_difficulty["Marks"]

# CONSISTENCY SCORE (STD DEV)
consistency = df.groupby("Student")["Marks"].std().reset_index()
consistency.rename(columns={"Marks":"Consistency_Score"}, inplace=True)

# ATTENDANCE vs MARKS CORRELATION
correlation = df["Marks"].corr(df["Attendance"])

# DROPOUT RISK ANALYSIS
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

# OUTPUT RESULTS
print("\n=== STUDENT PERFORMANCE TREND ===")
print(trend)

print("\n=== SUBJECT DIFFICULTY INDEX ===")
print(subject_difficulty)

print("\n=== CONSISTENCY SCORE ===")
print(consistency)

print("\n=== ATTENDANCE vs MARKS CORRELATION ===")
print(round(correlation, 2))

print("\n=== DROPOUT RISK ANALYSIS ===")
print(risk_df)

# -------------------------------
# VISUALIZATION SECTION
# -------------------------------

# Line Trend per Student
plt.figure()
sns.lineplot(data=trend, x="Semester", y="Marks", hue="Student", marker="o")
plt.title("Student Performance Progression Over Semesters")
plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.show()

# Subject Heatmap
pivot_table = df.pivot_table(values="Marks", index="Student", columns="Subject")
plt.figure()
sns.heatmap(pivot_table, annot=True, cmap="coolwarm")
plt.title("Subject-wise Performance Heatmap")
plt.show()

# Box Plot
plt.figure()
sns.boxplot(data=df, x="Subject", y="Marks")
plt.title("Marks Distribution by Subject")
plt.show()

# Attendance vs Marks Scatter
plt.figure()
sns.scatterplot(data=df, x="Attendance", y="Marks", hue="Student")
plt.title("Attendance vs Marks Relationship")
plt.show()

# FINAL MESSAGE
print("\nPROJECT EXECUTED SUCCESSFULLY")
print("Early-risk students identified and performance analytics generated.")
