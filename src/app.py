import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from pickle import load

model=load(open('./models/decision_tree_classifier_default_42.sav','rb'))

st.set_page_config(layout="wide")
st.write("# My app *Margarita*")
file=st.file_uploader("Pick a file", accept_multiple_files=True)

st.title("Your details")
# st.write(pd.read_csv(''))


