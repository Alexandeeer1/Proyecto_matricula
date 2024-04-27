import streamlit as st

st.markdown("<h1 style='text-align: center;'>Mi Página en Streamlit</h1>", unsafe_allow_html=True)

url_imagen = "https://intranet.upch.edu.pe/account/static/img/upch/logo/isotipo.jpg"
st.image(url_imagen, width=200)
