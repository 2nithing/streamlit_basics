import streamlit as st

choice =  st.sidebar.radio(
    label='choose your option',
    options=['audio','video']
)

if choice=='audio':
    st.write("audio option chosen")


form = st.form("basic form")
name = form.text_input("enter your name")
age = form.slider("age",min_value=10,max_value=100,step=1)
submitted = form.form_submit_button("Submit")

if submitted:
    st.write(name,age)