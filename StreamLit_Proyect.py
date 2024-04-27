import streamlit as st

# Añadir la imagen centrada
imagen_url = "https://is2-ssl.mzstatic.com/image/thumb/Purple126/v4/b9/3d/cb/b93dcb5d-0816-86f7-ff52-f9e8d59c5abd/AppIcon-0-1x_U007emarketing-0-5-0-sRGB-85-220.png/1200x630wa.png"
st.markdown(
    f'<div style="text-align:center"><img src="{imagen_url}" width="100"></div>',
    unsafe_allow_html=True
)

# Añadir el título
st.title("Portal de\nMatrícula")
