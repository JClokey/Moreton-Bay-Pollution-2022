import streamlit as st
from PIL import Image
import time
import pandas as pd

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: #49075e;'>Presence of contaminants of emerging concern in Moreton Bay during a la Niña year</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #49075e;'>Media</h2>", unsafe_allow_html=True)

with st.expander("Here there be media"):
    st.write("media files here")