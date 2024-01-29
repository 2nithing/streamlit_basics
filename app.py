import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from PIL import Image




# st.text("this is a test")
st.title("This is the header")
# st.write("this is **another** test _testing_")
df = pd.read_csv('./Iris.csv')
st.write(df)


fig = plt.figure()
plt.plot(np.arange(5),np.arange(5)**2)
plt.xlabel('xvalues')
plt.ylabel('yvalues')
st.write(fig)

st.header("Header")
st.subheader('subheaders')

# st.table(d  f)
df=df.drop('Id',axis=1)
st.line_chart(df)

# pr = st.button("click me")
# st.write(pr)

# if pr == True:
#     st.write("wow!! you clicked the button")
# def fn():
#     st.write("wow")

# st.button("click",on_click=fn)

option = st.radio(label="order food",options = ('pizza','burger','kanji'))

pr = st.button('order')
if pr==True:
    if option == 'pizza':
        st.write('you ordered pizza')
    elif option == 'burger':
        st.write('you ordered burger')
    elif option == 'kanji':
        st.write('you ordered kanji')


slider_out = st.slider(
    label="enter your height in inches",
    min_value=10,
    max_value=100,
    value = 50,
    step=1
)

st.write(slider_out)


txt = st.text_input(label="Enter your name",
                    max_chars=20,
                    placeholder='john')
st.write(txt)

num = st.number_input(label='enter your weight',
                    min_value=10,
                    max_value=100,
                    value=50,
                    step=1)
st.write(num)

txt = st.text_area(label="Enter your text",
                   height=10,
                   )

dat = st.date_input("enter your birthday",
                    value = datetime.date.today())

fl = st.file_uploader(label="upload here",
                      )
if fl:
    st.write(fl.type)


pic = st.camera_input("take a picture")
if pic:
    img = Image.open(pic)
    st.image(img)
    st.write(np.array(img).shape)


