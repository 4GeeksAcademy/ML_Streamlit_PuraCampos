import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from pickle import load


model=load(open('./models/decision_tree_classifier_default_42.sav','rb'))

st.set_option("client.showErrorDetails", False)

idioma = {"Español": "es"}
outcome = {"0": "iris setosa", "1": "iris versicolor","2": "iris virginica"}

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
    "sepal length (cm)": "Longitud de los sépalos (cm)",
    "sepal width (cm)": "Anchura de los sépalos (cm)",
    "petal length (cm)": "Longitud de los pétalos (cm)",
    "petal width (cm)": "Anchura de los pétalos (cm)",
    "Resultado": "Resultado",
    "success":"Toma nota:",
    "iris setosa": "iris setosa",
    "iris versicolor": "iris versicolor",
    "iris virginica": "iris virginica",

}
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Iris_tuberosa_Ypey72.jpg/250px-Iris_tuberosa_Ypey72.jpg", width=100)
st.title(text_labels["title"])

st.markdown(text_labels["instructions"])

left, right = st.columns(2)
with left:
    sepal_length_cm = st.slider("Longitud de los sépalos (cm)", min_value=1,max_value=10,value=1)
    sepal_width_cm = st.slider("Ancho de los sépalos (cm)", min_value=1,max_value=6,value=1)
with right:
    petal_length_cm = st.slider("Longitud de los pétalos (cm)", min_value=1,max_value=10,value=1)
    petal_width_cm = st.slider("Ancho de los pétalos (cm)", min_value=1,max_value=4,value=1)

if st.button(text_labels["Resultado"]):
    if not sepal_length_cm or not sepal_width_cm or not petal_length_cm or not petal_width_cm :
        st.error("Por favor, complete todos los campos antes de continuar.")
    else:
        sepal_length_cm = float(sepal_length_cm)
        sepal_width_cm = float(sepal_width_cm)
        petal_length_cm = float(petal_length_cm)
        petal_width_cm = float(petal_width_cm)


        data = np.array([[5.1, 3.5, 1.4, 0.2]])
        st.info(text_labels["success"])
        prediction = str(model.predict(data)[0])
        if prediction == "0":
            result = text_labels["iris setosa"]
        elif prediction == "1":
            result = text_labels["iris versicolor"]
        else:
            result = text_labels["iris virginica"]

        st.success(result)
        st.set_option