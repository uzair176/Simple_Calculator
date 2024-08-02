import streamlit as st

# Title of the app
st.title("Simple Calculator by Uzair")

# Taking float inputs
num1 = st.number_input("Enter 1st Number:", value=0.0, step=0.1)
num2 = st.number_input("Enter 2nd Number:", value=0.0, step=0.1)

# Select operator
operator = st.selectbox("Select Operator:", ['+', '-', '*', '/'])

# Calculate button
if st.button("Calculate"):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    st.success(f"Result: {result}")
