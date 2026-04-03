import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("../data/data.csv")

# ---------- ENCODING ----------
difficulty_map = {"Low":1, "Medium":2, "High":3}
time_map = {"Morning":1, "Afternoon":2, "Night":3}

df["Difficulty"] = df["Difficulty"].map(difficulty_map)
df["TimeOfDay"] = df["TimeOfDay"].map(time_map)

# dynamic subject encoding
df["Subject"] = df["Subject"].astype("category").cat.codes

# ---------- FEATURES ----------
X = df[[
    "StudyHours",
    "SleepHours",
    "Focus",
    "BreakDuration",
    "ExamDaysLeft",
    "Difficulty",
    "PreviousScore",
    "Stress",
    "Subject"
]]

y = df["TimeOfDay"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump({
    "model": model,
    "difficulty_map": difficulty_map,
    "time_map": time_map
}, "model.pkl")

print("Model trained successfully")