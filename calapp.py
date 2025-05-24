import streamlit as st
from calculator_normal import add, sub, mul, div

st.header("Calculator application")

choice=st.selectbox("Choose action", ["Add", "Sub", "Mul", "Div"])
result=0.0

num1=st.text_input("Enter number 1")
num2=st.text_input("Enter number 2")

cal_button=st.button("Calculate")

if cal_button:
    num1=float(num1)
    num2=float(num2)

    if choice=="Add":
        result=add(num1, num2)
    elif choice=="Sub":
        result=sub(num1, num2)
    elif choice=="Mul":
        result=mul(num1, num2)
    elif choice=="Div":
        result=div(num1, num2)

if result:
    st.write(f"Result of {choice} is {result}")
