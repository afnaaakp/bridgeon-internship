import streamlit as st


# CSS for green buttons
st.markdown("""
<style>
div.stButton > button {
    background-color: green;
    color: white;
    border-radius: 10px;
}
div.stButton > button:hover {
    background-color: darkgreen;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("Task Manager")

option = st.selectbox(
    "Choose an option",
    ["register", "login"]
)

if option == "register":
    username = st.text_input("username")
    email = st.text_input("Email")
    password = st.text_input("Password",
type="password")

    if st.button("Register"):
        if username.strip() and email.strip() and password.strip():
            st.success("Registration Successful!")
        else:
            st.error("fill the above fields")   
else:
    username = st.text_input("username")
    password = st.text_input("Password",
type="password")

    if st.button("Login"):
        if username and  password: 
            st.success("Login Successful!")
        else:
             st.error("fill the above fiels")   
           



