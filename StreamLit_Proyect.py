import streamlit as st

st.markdown("<h1 style='text-align: center;'>Mi Página en Streamlit</h1>", unsafe_allow_html=True)

url_imagen = "https://intranet.upch.edu.pe/account/static/img/upch/logo/isotipo.jpg"
st.markdown(f'<div style="text-align: center; border-radius: 20px; overflow: hidden;"><img src="{url_imagen}" width="200" style="border-radius: 20px;"></div>', unsafe_allow_html=True)
