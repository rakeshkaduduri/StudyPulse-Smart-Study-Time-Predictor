import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import base64

st.set_page_config(page_title="StudyPulse Dashboard", layout="wide")

# ---------- BACKGROUND ----------
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("assets/bg.png")

st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{bg}");
    background-size: cover;
}}
[data-testid="stAppViewContainer"]::before {{
    content:"";
    position:fixed;
    width:100%;
    height:100%;
    background: rgba(0,0,0,0.75);
}}
h1,h2,h3,p,li {{ color:white !important; }}

.glass {{
    background: rgba(255,255,255,0.15);
    padding: 25px;
    border-radius: 18px;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    margin-bottom: 20px;
    transition: all 0.3s ease;
}}

.glass:hover {{
    transform: scale(1.02);
    box-shadow: 0 0 20px rgba(255,255,255,0.25);
}}
</style>
""", unsafe_allow_html=True)

# ---------- LOAD ----------
data = st.session_state.get("data", None)
if data is None:
    st.warning("Go to Input page first")
    st.stop()

saved = joblib.load("model/model.pkl")
model = saved["model"]
difficulty_map = saved["difficulty_map"]
time_map = saved["time_map"]
reverse_time_map = {v:k for k,v in time_map.items()}

study, sleep, focus = data["study"], data["sleep"], data["focus"]
break_dur, exam_days = data["break"], data["exam_days"]
difficulty, score, stress = data["difficulty"], data["score"], data["stress"]
subject = data["subject"]

subject_val = abs(hash(subject)) % 100
difficulty_val = difficulty_map[difficulty]

# ---------- ML ----------
X = [[study, sleep, focus, break_dur, exam_days, difficulty_val, score, stress, subject_val]]
ml_time = reverse_time_map[model.predict(X)[0]]

# ---------- LOGIC ----------
if sleep >= 7 and focus >= 7:
    best_time = "Morning"
elif sleep < 5:
    best_time = "Afternoon"
elif stress >= 7:
    best_time = "Night"
elif focus >= 6:
    best_time = "Morning"
else:
    best_time = ml_time

# ---------- SLEEP ANALYSIS ----------
if sleep < 5:
    sleep_msg = f"You are sleeping only {sleep} hours. This negatively impacts concentration, memory retention, and problem-solving ability."
elif sleep <= 7:
    sleep_msg = f"You are getting {sleep} hours of sleep. This is acceptable, but increasing it slightly will improve cognitive performance."
else:
    sleep_msg = f"You are getting {sleep} hours of sleep, which is ideal. This supports strong memory retention, faster learning, and better focus."

# ---------- BREAK LOGIC ----------
if focus >= 8:
    study_block = 50
    break_time = 10
elif focus >= 5:
    study_block = 40
    break_time = 10
else:
    study_block = 30
    break_time = 15

break_msg = f"You should follow a cycle of {study_block} minutes of focused study followed by a {break_time}-minute break."

# ---------- DYNAMIC SCHEDULE ----------
# Start time based on sleep
if sleep >= 7:
    start_hour = 7
elif sleep >= 5:
    start_hour = 8
else:
    start_hour = 9

# Session duration based on focus
if focus >= 8:
    session_minutes = 60
elif focus >= 5:
    session_minutes = 45
else:
    session_minutes = 30


# Total sessions
sessions = study
schedule_rows = []
current_minutes = start_hour * 60              # convert to minutes

for i in range(sessions):

    start = current_minutes
    end = current_minutes + session_minutes

    start_h, start_m = divmod(start, 60)
    end_h, end_m = divmod(end, 60)

    # ---------- INTELLIGENT ACTIVITY ----------
    if exam_days <= 3:

        # EXAM MODE
        if i == 0:
            activity = f"Revise {subject} (Important Topics)"
        elif i == sessions - 1:
            activity = f"Solve Previous Papers ({subject})"
        else:
            activity = f"Quick Revision + Practice ({subject})"

    elif exam_days <= 7:

        # PRACTICE MODE
        if difficulty == "High":
            if i == 0:
                activity = f"Deep Study {subject} (Concepts)"
            elif i == sessions - 1:
                activity = f"Revise Mistakes ({subject})"
            else:
                activity = f"Practice Hard Problems ({subject})"
        else:
            if i == 0:
                activity = f"Study {subject} Concepts"
            else:
                activity = f"Practice + Revise ({subject})"

    else:
        
        # NORMAL MODE
        if difficulty == "High":
            if i == 0:
                activity = f"Deep Focus Study ({subject})"
            elif i == sessions - 1:
                activity = f"Revise Key Concepts ({subject})"
            else:
                activity = f"Problem Solving ({subject})"
        elif difficulty == "Medium":
            if i == 0:
                activity = f"Understand Concepts ({subject})"
            else:
                activity = f"Practice Questions ({subject})"
        else:
            if i == 0:
                activity = f"Light Study ({subject})"
            else:
                activity = f"Revision ({subject})"

    # ---------- STUDY BLOCK ----------
    schedule_rows.append({
        "Time": f"{start_h:02d}:{start_m:02d} - {end_h:02d}:{end_m:02d}",
        "Activity": activity,
        "Type": "Study"
    })

    # ---------- BREAK BLOCK ----------
    break_start = end
    break_end = break_start + break_time

    bs_h, bs_m = divmod(break_start, 60)
    be_h, be_m = divmod(break_end, 60)

    schedule_rows.append({
        "Time": f"{bs_h:02d}:{bs_m:02d} - {be_h:02d}:{be_m:02d}",
        "Activity": "☕ Break (Recharge)",
        "Type": "Break"
    })
    current_minutes = break_end

schedule_df = pd.DataFrame(schedule_rows)

# ---------- STYLE SCHEDULE ----------
def highlight_rows(row):
    if row["Type"] == "Study":
        return ["background-color: rgba(0,255,100,0.15)"] * len(row)
    else:
        return ["background-color: rgba(255,150,0,0.15)"] * len(row)

styled_df = schedule_df.style.apply(highlight_rows, axis=1)

# ---------- IMPROVEMENT SUGGESTIONS ----------
improvements = []

# Sleep
if sleep < 6:
    improvements.append(f"You are sleeping only {sleep} hours. Increasing it to 7–8 hours will improve memory and focus.")
elif sleep <= 8:
    improvements.append(f"You are getting {sleep} hours of sleep, which is good. Maintaining this will support consistent performance.")
else:
    improvements.append(f"You are sleeping {sleep} hours. Ensure it is not affecting your study time or causing sluggishness.")

# Focus
if focus < 5:
    improvements.append("Use shorter study sessions with breaks to improve concentration.")

# Stress
if stress > 7:
    improvements.append("High stress detected. Include relaxation or light revision sessions.")

# Study hours
if study < 3:
    improvements.append("Your study time is low. Increase it gradually to build consistency.")
elif study > 6:
    improvements.append("You are studying for long hours. Ensure you maintain consistency without burnout.")

# Focus vs Sleep
if focus > sleep and sleep < 7:
    improvements.append("Your focus is good, but increasing sleep will further improve performance.")
elif focus <= sleep and focus < 6:
    improvements.append("Improving your focus should be your top priority for better productivity.")

# Burnout
if sleep < 6 and stress > 7:
    improvements.append("Low sleep and high stress together can lead to burnout. Prioritize rest and reduce workload.")

# Focus potential
if focus >= 8 and study < 3:
    improvements.append("You have strong focus but low study time. Increasing study duration will significantly boost results.")

# Exam awareness
if exam_days <= 3:
    improvements.append("Exams are very close. Prioritize revision and avoid learning new topics.")
elif exam_days <= 7:
    improvements.append("Focus on practice and solving problems to prepare effectively for upcoming exams.")

# Default fallback
if not improvements:
    improvements.append("Your routine is well balanced. Maintain consistency.")


# ---------- TITLE ----------
st.markdown("<h1>📊 Study Intelligence Report</h1>", unsafe_allow_html=True)

# ---------- PRODUCTIVITY SCORE ----------
score = (focus * 2 + sleep * 2 + study - stress) * 5
score = int(max(0, min(score, 100)))

st.markdown(f"""
<div class="glass">
<h3>🎯 Productivity Score</h3>
<h1 style='color:#00FFAA'>{score}/100</h1>
<p>Based on your sleep, focus, stress, and study patterns.</p>
</div>
""", unsafe_allow_html=True)

# ---------- BEST TIME ----------
st.markdown(f"""
<div class="glass">
<h3>🧠 Best Study Time</h3>
<p>Your most productive study period is <b>{best_time}</b>.</p>
<p>This is determined using your focus, sleep, and stress levels to maximize learning efficiency.</p>
<ul>
<li>Higher retention rate</li>
<li>Better understanding</li>
<li>Lower distraction</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------- SLEEP ----------
health_insight = ""

if focus > sleep:
    health_insight = "Your focus is strong, but improving sleep can further boost performance."
else:
    health_insight = "Improving focus will have the biggest impact on your productivity."

st.markdown(f"""
<div class="glass">
<h3>💤 Health & Cognitive Analysis</h3>
<p>{sleep_msg}</p>
<p><b>Insight:</b> {health_insight}</p>

<ul>
<li>Sleep affects memory consolidation</li>
<li>Low sleep reduces problem-solving ability</li>
<li>Good sleep improves learning speed</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------- STRESS ALERT ----------
if stress >= 8 and sleep < 5:
    st.error("⚠ High burnout risk detected due to low sleep and high stress.")
elif stress >= 8:
    st.error("⚠ High stress levels detected.")
elif stress >= 5:
    st.warning("⚠ Moderate stress levels. Consider breaks and relaxation.")
else:
    st.success("✅ Stress levels are under control.")

# ---------- BREAK ----------
st.markdown(f"""
<div class="glass">
<h3>⏱ Break Strategy</h3>
<p>{break_msg}</p>
<ul>
<li>Breaks prevent burnout</li>
<li>Improve long-term focus</li>
<li>Increase productivity</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------- EXAM MODE ----------
if exam_days <= 3:
    st.markdown("""
    <div class="glass">
    <h3>🔥 Exam Mode Activated</h3>
    <p>You are very close to exams. Focus more on revision, mock tests, and weak areas. Avoid learning new topics.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- SCHEDULE ----------
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.markdown("<h3>📅 Study Schedule</h3>", unsafe_allow_html=True)

def highlight_rows(row):
    if row["Type"] == "Study":
        return ["background-color: rgba(0,255,100,0.15)"] * len(row)
    else:
        return ["background-color: rgba(255,150,0,0.15)"] * len(row)

styled_df = schedule_df.style.apply(highlight_rows, axis=1)
if exam_days <= 3:
    st.warning("🔥 Exam Mode: High intensity revision activated")
elif exam_days <= 7:
    st.info("📘 Practice Mode: Focus on solving problems")
else:
    st.success("🧠 Learning Mode: Build strong concepts")
st.write(styled_df)
st.markdown("""
<div class="glass">
<h3>🧠 Why This Plan Works</h3>

<p>
This schedule is generated based on your focus level, sleep quality, stress, and study capacity. 
High-focus periods are assigned to deep learning tasks, while lower-energy periods are used for revision and lighter work.
Break intervals are optimized to prevent burnout and maintain cognitive performance.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- TABLE ----------
table = pd.DataFrame({
    "Factor": ["Sleep", "Focus", "Study Hours", "Stress"],
    "Value": [sleep, focus, study, stress],
    "Effect": ["Memory", "Efficiency", "Workload", "Mental State"]
})

st.markdown('<div class="glass">', unsafe_allow_html=True)
st.write("### 📊 Performance Summary")
st.table(table)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- GRAPH ----------
df = pd.read_csv("data/data.csv")
df = pd.concat([df, pd.DataFrame([{"TimeOfDay": best_time, "Focus": focus}])])

focus_by_time = df.groupby("TimeOfDay")["Focus"].mean()

fig, ax = plt.subplots()
ax.bar(focus_by_time.index, focus_by_time.values)

ax.set_title(f"Focus Pattern for {subject}")
ax.set_xlabel("Time of Day")
ax.set_ylabel("Focus Level")

st.markdown('<div class="glass">', unsafe_allow_html=True)
st.pyplot(fig)

# ---------- GRAPH INSIGHT ----------
if focus >= 8:
    insight = "You have strong focus ability. Utilize long deep-work sessions."
elif focus >= 5:
    insight = "Your focus is moderate. Balanced study + breaks work best."
else:
    insight = "Low focus detected. Use shorter sessions and frequent breaks."

st.markdown(f"<p style='color:white'>{insight}</p>", unsafe_allow_html=True)
st.markdown(f"""
<p style='color:white'>
Your focus peaks during <b>{best_time}</b>. Schedule your most difficult subject ({subject}) during this time for maximum efficiency.
</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- IMPROVEMENTS ----------
st.markdown(f"""
<div class="glass">
<h3>📈 Personalized Improvement Suggestions</h3>
<ul>
{''.join(f"<li>{i}</li>" for i in improvements)}
</ul>
<ul>
<li>Focus on weak areas in {subject}</li>
</ul>
</div>
""", unsafe_allow_html=True)