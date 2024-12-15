import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from pickle import load


model=load(open('./models/decision_tree_classifier_default_42.sav','rb'))

idioma = {"Español": "es"}

with st.sidebar:
    st.title("Lirio tuberoso")
    st.title("Iris tuberosa")

text_labels = {
    "title": "Iris (planta)",
    "instructions": """
    ### Instrucciones:
    1. Introducir los datos que se requieren.
    2. Ajuste los parámetros según sea necesario.
    3. Presione el botón "Predecir" para ver el resultado.
    """,
    "sepal length (cm)": "sepal length (cm)",
    "sepal width (cm)": "sepal width (cm)",
    "petal length (cm)": "petal length (cm)",
    "petal width (cm)": "petal width (cm)",
}
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Iris_tuberosa_Ypey72.jpg/250px-Iris_tuberosa_Ypey72.jpg", width=100)
st.title(text_labels["title"])

st.markdown(text_labels["instructions"])

left, right = st.columns(2)
with left:
    sepal_length_cm = st.text_input(text_labels["sepal length (cm)"])
    sepal_width_cm = st.text_input(text_labels["sepal width (cm)"])
with right:
    petal_length_cm = st.text_input(text_labels["petal length (cm)"])
    petal_width_cm = st.text_input(text_labels["petal width (cm)"])