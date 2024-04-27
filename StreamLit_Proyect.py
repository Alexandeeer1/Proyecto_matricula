import streamlit as st

# Título centrado y más pequeño
st.title("Mi Página en Streamlit")
st.markdown("<h1 style='text-align: center; color: black;'>Mi Página en Streamlit</h1>", unsafe_allow_html=True)

# Mostrar la imagen
imagen_url = "https://intranet.upch.edu.pe/account/static/img/upch/logo/isotipo.jpg"
st.image(imagen_url, caption='Logo de UPCH', use_column_width=True)
