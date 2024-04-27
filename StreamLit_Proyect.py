import streamlit as st

# Añadir la imagen centrada
imagen_url = "https://portalmatricula.cayetano.pe/static/media/logo-icon.134f0cc399e26b0cfaa0.png"
st.markdown(
    f'<div style="text-align:center"><img src="{imagen_url}" width="100"></div>',
    unsafe_allow_html=True
)

# Añadir el título
st.title("Portal de\nMatrícula")
