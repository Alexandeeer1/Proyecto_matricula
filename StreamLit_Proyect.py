import streamlit as st

st.title("Mi Página en Streamlit").align("center")

imagen_url = "https://intranet.upch.edu.pe/account/static/img/upch/logo/isotipo.jpg"
st.image(imagen_url, caption='Logo de UPCH', width=200, use_column_width=True)
