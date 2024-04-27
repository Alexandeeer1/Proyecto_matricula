import streamlit as st

# Añadir la imagen desde GitHub
imagen_url = "https://github.com/Alexandeeer1/Proyecto_matricula/raw/main/Logo_cayetano.jpg"
st.markdown(
    f'<div style="text-align:center"><img src="{imagen_url}" width="100"></div>',
    unsafe_allow_html=True
)

# Añadir el título
st.title("Portal de\nMatrícula")
