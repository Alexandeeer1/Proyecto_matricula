import streamlit as st
import pandas as pd

st.write("¡Hola Mundo!")
st.title("Mi Aplicación Streamlit")
st.sidebar.header("Configuración")
option = st.sidebar.selectbox("Seleccione una opción", ["Opción 1", "Opción 2", "Opción 3"])
