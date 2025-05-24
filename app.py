import streamlit as st

st.header("Student registration page")
first_name=st.text_input("Enter your first name")
last_name=st.text_input("Enter your last name")

gender=st.radio("Choose your gender", ["Male", "Female", "Other"])
college=st.selectbox("Choose your college", ["VSSUT", "ITER", "KIIT", "TAT", "Gandhi"])

sub_btn=st.button("Click to register")

if sub_btn:
    if first_name and last_name:
        st.header("You have entered following details")
        st.write(f"Full name: {first_name} {last_name}")
        st.write(f"Your gender: {gender}")
        st.write(f"Your college: {college}")
        st.link_button("Go to college", "https://streamlit.io/gallery")
    else:
        st.error("Some mandatory fields are empty")
   
