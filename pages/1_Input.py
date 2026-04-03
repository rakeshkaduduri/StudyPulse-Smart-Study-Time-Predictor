import streamlit as st
import base64

st.set_page_config(page_title="StudyPulse Input", layout="wide")

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("assets/bg.png")

st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{bg}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
[data-testid="stAppViewContainer"]::before {{
    content:"";
    position:fixed;
    width:100%;
    height:100%;
    background: rgba(0,0,0,0.80);
}}
h1,label {{ color:white !important; }}
.glass {{
    background: rgba(255,255,255,0.12);
    padding: 30px;
    border-radius: 18px;
    backdrop-filter: blur(12px);
}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="glass">', unsafe_allow_html=True)

st.title("📝 Enter Your Details")

study = st.slider("Study Hours per Day", 1, 12, 5)
sleep = st.slider("Sleep Hours", 3, 10, 6)
focus = st.slider("Focus Level", 1, 10, 6)
break_dur = st.slider("Break Duration", 5, 30, 10)
exam_days = st.slider("Exam Days Left", 1, 15, 5)

difficulty = st.selectbox("Difficulty", ["Low", "Medium", "High"])
score = st.slider("Previous Score", 0, 100, 70)
stress = st.slider("Stress Level", 1, 10, 5)

subject = st.text_input("Enter Your Subject", "Math")

if st.button("🚀 Generate Plan"):
    st.session_state["data"] = {
        "study": study,
        "sleep": sleep,
        "focus": focus,
        "break": break_dur,
        "exam_days": exam_days,
        "difficulty": difficulty,
        "score": score,
        "stress": stress,
        "subject": subject
    }
    st.success("Plan generated! Go to Dashboard 👉")

st.markdown('</div>', unsafe_allow_html=True)