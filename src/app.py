import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from pickle import load

# Cargar modelo
model = load(open('./models/decision_tree_classifier_default_42.sav', 'rb'))

# Configuración inicial
st.set_option("client.showErrorDetails", False)

# Diccionarios para idioma y etiquetas
idioma = {"Español": "es"}
outcome = {"0": "iris setosa", "1": "iris versicolor", "2": "iris virginica"}

text_labels = {
    "title": "Iris (planta)",
    "instructions": """
    ### Instrucciones:
    1. Introducir los datos que se requieren.
    2. Ajuste los parámetros según sea necesario.
    3. Presione el botón "Predecir" para ver el resultado.
    """,
    "sepal length (cm)": "Longitud de los sépalos (cm)",
    "sepal width (cm)": "Ancho de los sépalos (cm)",
    "petal length (cm)": "Longitud de los pétalos (cm)",
    "petal width (cm)": "Ancho de los pétalos (cm)",
    "Resultado": "Predecir",
    "success": "Lo que tienes en tu jardín:",
    "error": "Por favor, complete todos los campos antes de continuar.",
    "iris setosa": "Iris Setosa",
    "iris versicolor": "Iris Versicolor",
    "iris virginica": "Iris Virginica",
}

# Barra lateral
with st.sidebar:
    st.title("Lirio tuberoso")
    st.write("Iris tuberosa")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Iris_tuberosa_Ypey72.jpg/250px-Iris_tuberosa_Ypey72.jpg", width=100)

# Título principal
st.title(text_labels["title"])
st.markdown(text_labels["instructions"])

# Entradas del usuario
left, right = st.columns(2)
with left:
    sepal_length_cm = st.number_input(text_labels["sepal length (cm)"], min_value=1.0, max_value=10.0, value=10.0, step=0.1)
    sepal_width_cm = st.number_input(text_labels["sepal width (cm)"], min_value=1.0, max_value=6.0, value=6.0, step=0.1)
with right:
    petal_length_cm = st.number_input(text_labels["petal length (cm)"], min_value=1.0, max_value=10.0, value=10.0, step=0.1)
    petal_width_cm = st.number_input(text_labels["petal width (cm)"], min_value=1.0, max_value=4.0, value=4.0, step=0.1)

# Botón de predicción
if st.button(text_labels["Resultado"]):
    # Validación de campos
    if not (sepal_length_cm and sepal_width_cm and petal_length_cm and petal_width_cm):
        st.error(text_labels["error"])
    else:
        # Preparar datos para predicción
        data = np.array([[sepal_length_cm, sepal_width_cm, petal_length_cm, petal_width_cm]])
        prediction = str(model.predict(data)[0])

        # Determinar resultado
        result = outcome.get(prediction, "Desconocido")
        
        # Mostrar resultados
        st.subheader(text_labels["success"])
        st.write(f"**Logitud del sépalo:** {sepal_length_cm} cm")
        st.write(f"**Achura del sépalo:** {sepal_width_cm} cm")
        st.write(f"**Logitud del pétalo:** {petal_length_cm} cm")
        st.write(f"**Achura del pétalo:** {petal_width_cm} cm")
        st.success(f"Predicción: {result}")