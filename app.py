import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Simple Streamlit App", page_icon="🚀")

st.title("🚀 My First Streamlit App")
st.write("This is a simple app deployed on Streamlit Cloud.")

# User input
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 1, 100, 25)

if st.button("Submit"):
    st.success(f"Hello {name}! You are {age} years old.")

st.divider()

st.subheader("Random Data Chart")

# Generate random data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(data)

st.divider()

st.subheader("Simple Calculator")

num1 = st.number_input("Enter first number:", value=0.0)
num2 = st.number_input("Enter second number:", value=0.0)

if st.button("Add Numbers"):
    st.write(f"Result: {num1 + num2}")
