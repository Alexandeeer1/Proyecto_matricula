import streamlit as st

# Establecer el estilo CSS para la imagen
st.markdown(
    """
    <style>
    .imagen-container {
        display: flex;
        justify-content: center;
    }

    .imagen {
        width: 50%; /* Ancho de la imagen */
        border-radius: 10px; /* Radio de borde de la imagen */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Añadir la imagen centrada
imagen_url = "https://intranet.upch.edu.pe/account/static/img/upch/logo/isotipo.jpg"
st.markdown(
    f'<div class="imagen-container"><img src="{imagen_url}" class="imagen"></div>',
    unsafe_allow_html=True
)

# Añadir el título
st.title("Portal de Matrícula")
