import streamlit as st
from PIL import Image
import time
import pandas as pd

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: #49075e;'>Presence of contaminants of emerging concern in Moreton Bay during a la Niña year</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #49075e;'>Media</h2>", unsafe_allow_html=True)
st.image("https://static.streamlit.io/examples/dice.jpg")

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write("The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")
    st.image("https://static.streamlit.io/examples/dice.jpg")