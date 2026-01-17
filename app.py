import streamlit as st
from core.ai_engine import AIEngine
from domains.water import get_water_questions, get_water_knowledge
from domains.energy import get_energy_questions, get_energy_knowledge
from domains.waste import get_waste_questions, get_waste_knowledge

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Sustainability Decision Support System",
    page_icon="🌍",
    layout="centered"
)

# ---------------- GLOBAL CSS ----------------
st.markdown("""
<style>
/* REAL Streamlit background */
.stApp {
    background: linear-gradient(135deg, #eef2ff, #f0fdfa);
}

/* Main container */
.app-container {
    max-width: 900px;
    margin: auto;
    padding-top: 20px;
}

/* Titles */
.title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 4px;
}
.subtitle {
    text-align: center;
    color: #475569;
    font-size: 15px;
    margin-bottom: 18px;
}

/* Card layout */
.card {
    background-color: #ffffff;
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 16px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.06);
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    margin-top: 24px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='app-container'>", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "ai_engine" not in st.session_state:
    st.session_state.ai_engine = AIEngine()

# =================================================
# 🔐 LOGIN PAGE (WITH TITLE)
# =================================================
if not st.session_state.logged_in:
    st.markdown("<div class='title'>🌍 AI Sustainability Decision Support System</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='subtitle'>AI for sustainable education and informed decision-making</div>",
        unsafe_allow_html=True
    )


    st.subheader("🔐 Login")

    name = st.text_input("Your Name")
    role = st.selectbox(
        "Your Role",
        ["Student", "Resident", "Institution Representative"]
    )

    if st.button("Continue"):
        if name.strip() == "":
            st.warning("Please enter your name to continue")
        else:
            st.session_state.logged_in = True
            st.session_state.user_name = name
            st.session_state.user_role = role
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# =================================================
# 🏠 MAIN PAGE
# =================================================

# Header
st.markdown("<div class='title'>🌍 AI Sustainability Decision Support System</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Helping users make informed sustainability decisions using AI</div>",
    unsafe_allow_html=True
)

st.success(f"Welcome, {st.session_state.user_name} ({st.session_state.user_role})")

# ---------------- DOMAIN SELECTION ----------------

st.subheader("🔍 Select Sustainability Domain")

domain_choice = st.radio(
    "",
    ["💧 Water Management", "⚡ Energy Efficiency", "♻️ Waste Management"],
    index=0
)

st.markdown("</div>", unsafe_allow_html=True)

domain = domain_choice.split(" ")[1]

# ---------------- LOAD DOMAIN DATA ----------------
if domain == "Water":
    questions = get_water_questions()
    knowledge = get_water_knowledge()
elif domain == "Energy":
    questions = get_energy_questions()
    knowledge = get_energy_knowledge()
else:
    questions = get_waste_questions()
    knowledge = get_waste_knowledge()

# ---------------- QUESTIONS (NO EMPTY SPACE) ----------------

st.subheader(f"📋 {domain} Usage Assessment")
st.caption("Answer a few basic questions so the system understands your context")

for q in questions:
    st.text_input(q)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- AI CHAT (CONDITIONAL) ----------------

st.subheader("💬 Ask the AI Advisor")

user_query = st.text_input("Ask your question")

if user_query.strip() != "":
    response = st.session_state.ai_engine.get_best_response(user_query, knowledge)
    st.subheader("🧠 AI Recommendation")
    st.success(response)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>AI for Sustainability</div>",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
