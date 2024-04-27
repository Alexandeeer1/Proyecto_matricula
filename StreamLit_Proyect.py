import streamlit as st

# Añadir la imagen centrada
imagen_url = "https://staticfileszyxme.s3.us-east.cloud-object-storage.appdomain.cloud/UPCH/422ca812-4555-4692-a386-2dcb7ffd5439/logo-upch-chatbot.png"
st.markdown(
    f'<div style="text-align:center"><img src="{imagen_url}" width="100"></div>',
    unsafe_allow_html=True
)

# Añadir el título
st.title("Portal de\nMatrícula")
