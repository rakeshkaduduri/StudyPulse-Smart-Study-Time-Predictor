import streamlit as st
import base64

st.set_page_config(page_title="StudyPulse", layout="wide")

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
    background-position: center;
}}

[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.45);
}}

h1, h2, h3, p, li {{
    color: white !important;
}}

.center {{
    text-align: center;
}}

.glass {{
    background: rgba(255,255,255,0.40);
    padding: 35px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    min-height: 300px;
}}

.bottom-text {{
    text-align: center;
    margin-top: 40px;
    font-size: 20px;
}}

</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<style>


# .hero {{
#     background: rgba(255,255,255,0.40);
#     padding: 40px;
#     border-radius: 20px;
#     text-align: center;
#     backdrop-filter: blur(12px);   /* 🔥 THIS IS THE FIX */
#     -webkit-backdrop-filter: blur(12px); /* for compatibility */
#     border: 1px solid rgba(255,255,255,0.2);
#     box-shadow: 0 0 25px rgba(0,0,0,0.6);
# }}

.hero {{
    width: 80%;
    margin: auto;
    background: rgba(255,255,255,0.40);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 0 25px rgba(0,0,0,0.6);
}}

.hero p {{
    font-size: 20px;
    font-style: italic;
}}

</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<style>

.glass:hover {{
    transform: scale(1.02);
    transition: 0.3s;
    box-shadow: 0 0 20px rgba(255,255,255,0.40);
}}

</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<style>

.hero:hover {{
    transform: scale(1.02);
    transition: 0.3s;
    box-shadow: 0 0 30px rgba(255,255,255,0.40);
}}

</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<style>

.glass, .hero {{
    transition: all 0.3s ease;
}}

</style>
""", unsafe_allow_html=True)


# ---------- TITLE ----------
st.markdown('<h1 class="center">📘 StudyPulse</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="center">AI-Powered Adaptive Study Planner</h3>', unsafe_allow_html=True)
st.markdown('<p class="center">Analyzes your behavior to optimize focus, schedule, and prevent burnout</p>', unsafe_allow_html=True)

st.write("")
st.markdown("<br><br>", unsafe_allow_html=True)

# ---------- TWO COLUMN LAYOUT ----------
col1, col2 = st.columns(2)

# LEFT CARD
with col1:
    st.markdown("""
    <div class="glass">
    <h3>💡 Why this matters</h3>

    <p>Many students study randomly without understanding their own productivity patterns.</p>

    <ul>
        <li>When they focus best</li>
        <li>How long they should study</li>
        <li>When to take breaks</li>
    </ul>

    <p>This app guides you step-by-step to improve your learning efficiency.</p>
    </div>
    """, unsafe_allow_html=True)

# RIGHT CARD
with col2:
    st.markdown("""
    <div class="glass">
    <h3>⚡ What Makes This Smart</h3>

    <ul>
        <li>Adapts to your daily behavior</li>
        <li>Predicts your most productive study time</li>
        <li>Prioritizes subjects based on exam urgency</li>
        <li>Detects burnout before it happens</li>
        <li>Dynamically adjusts study sessions</li>
    </ul>

    <p>This is not a static planner — it learns and evolves with your behavior.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<style>
.spacer {
    height: 40px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero">
<h2>🧠 Your Study Insight</h2>

<p>
"You are most productive in the morning (8–11 AM), and your focus drops after 40 minutes."
</p>
<p><b>→ Study difficult subjects early and take structured breaks.</b></p>

</div>
""", unsafe_allow_html=True)

# ---------- CENTER BOTTOM TEXT ----------
st.markdown("""
<div class="bottom-text">
<b>Start building your smart study plan today</b><br><br>
👉 Use the Input page to get personalized insights
</div>
""", unsafe_allow_html=True)