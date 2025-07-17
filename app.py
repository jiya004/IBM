import streamlit as st
from health_agent import generate_health_advice  # Function that calls Gemini model

# Page config
st.set_page_config(page_title="AI Health Bot - SDG 3", page_icon="🩺")

# CSS styling
st.markdown("""
    <style>
        .gradient-text {
            font-size: 40px;
            font-weight: bold;
            background: linear-gradient(to right, #FF6347, #4682B4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
        }

        div.stButton > button {
            background: linear-gradient(to right, #1e3c72, #2a5298);
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
        }

        div.stButton > button:hover {
            background: linear-gradient(to right, #2a5298, #1e3c72);
        }

        .input-box {
            background-color: #f4f9ff;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown('<h1 class="gradient-text">AI Health Bot 🩺</h1>', unsafe_allow_html=True)
st.markdown("Helping you understand health risks and how to improve your well-being. *(SDG 3: Good Health & Well-being)*")

# Input form
with st.form("health_form"):
    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    
    age = st.number_input("Enter Age", min_value=1, max_value=120)
    bmi = st.number_input("Enter BMI (Body Mass Index)", min_value=10.0, max_value=50.0)
    bp = st.number_input("Enter Blood Pressure (Systolic)", min_value=60, max_value=200)
    glucose = st.number_input("Enter Glucose Level (mg/dL)", min_value=50, max_value=300)
    
    submitted = st.form_submit_button("Analyze")

    st.markdown('</div>', unsafe_allow_html=True)

# On submit
if submitted:
    with st.spinner("Analyzing with Gemini AI..."):
        result = generate_health_advice(age, bmi, bp, glucose)
    st.success("✅ Analysis Complete")
    st.markdown("### Result")
    st.markdown(result)
