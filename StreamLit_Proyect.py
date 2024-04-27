import streamlit as st

# Añadir la imagen centrada
imagen_url = "https://intranet.upch.edu.pe/account/static/img/upch/logo/isotipo.jpg"
st.markdown(
    f'<div style="text-align:center"><img src="{imagen_url}" width="100"></div>',
    unsafe_allow_html=True
)

# Añadir el título
st.title("Portal de\nMatrícula")
