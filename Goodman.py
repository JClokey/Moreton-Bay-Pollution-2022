import streamlit as st
from PIL import Image
import time
import pandas as pd

st.set_page_config(layout="wide")

#st.title ("Presence of contaminants of emerging concern in Moreton Bay during a la Niña year")
st.markdown("<h1 style='text-align: center; color: #49075e;'>Presence of contaminants of emerging concern in Moreton Baaaaaay during a la Niña year</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #53277E;'>A QAEHS X Goodman collaboration</h3>", unsafe_allow_html=True)
#st.header("A QAEHS X Goodman collaboration")
st.markdown("Joseph Clokey")

buoy_og = Image.open('Buoy_pumicestone_passage.jpeg')
buoy_rot = buoy_og.transpose(Image.ROTATE_270)
buoy_rot = buoy_rot.resize((423, 564)) #original size was 3024 x 4032

st.subheader("2022")
st.caption("Utilising passive sampling, grab sampling, seagrass and sediment analysis")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.write("Hello")

col1, col2 = st.columns(2)
col1.image(buoy_rot)
col2.video("carly mud.mp4")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
#st.markdown(hide_streamlit_style, unsafe_allow_html=True) #this removes the "made by streamlit" and menu options, comment this out to play with theme etc