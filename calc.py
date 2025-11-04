import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Python Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #DCEAF5, #F8F9FC);
            border-radius: 12px;
            padding: 25px;
        }
        h1 {
            color: #1E3A8A;
            text-align: center;
            font-family: 'Trebuchet MS', sans-serif;
        }
        h2 {
            color: #2563EB;
            font-family: 'Trebuchet MS', sans-serif;
        }
        .stButton>button {
            background-color: #2563EB;
            color: white;
            border-radius: 8px;
            height: 2.8em;
            width: 100%;
            border: none;
            font-size: 16px;
            font-weight: 600;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #1D4ED8;
        }
        .result-box {
            background-color: #EFF6FF;
            border-left: 5px solid #2563EB;
            padding: 10px;
            margin-top: 15px;
            border-radius: 6px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Main Title ---
st.title("🧮 Welcome to the Python Calculator Website")
st.subheader("Perform basic calculations easily")

# --- Input Fields ---
st.markdown("<div class='main'>", unsafe_allow_html=True)
a = st.number_input("Enter first number", step=1.0, format="%.2f")
b = st.number_input("Enter second number", step=1.0, format="%.2f")

operation = st.selectbox("Choose an operation", ["Add ➕", "Subtract ➖", "Multiply ✖️", "Divide ➗"])

# --- Calculation ---
if st.button("Calculate"):
    if operation == "Add ➕":
        result = a + b
    elif operation == "Subtract ➖":
        result = a - b
    elif operation == "Multiply ✖️":
        result = a * b
    elif operation == "Divide ➗":
        result = "Cannot divide by zero" if b == 0 else a / b

    st.markdown(f"<div class='result-box'><h5>✅ Result: {result}</h5></div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)





 
 



