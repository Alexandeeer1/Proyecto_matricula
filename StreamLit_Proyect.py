import streamlit as st

# Añadir la imagen desde GitHub
imagen_url = "https://github.com/Alexandeeer1/Proyecto_matricula/blob/e0789261055abb229fc8926be09940af6a169f84/Logo_cayetano.jpg"
st.markdown(
    f'<div style="text-align:center"><img src="{imagen_url}" width="100"></div>',
    unsafe_allow_html=True
)

# Añadir el título
st.title("Portal de\nMatrícula")
