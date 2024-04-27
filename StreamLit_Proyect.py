import streamlit as st

# Establecer el estilo CSS para el título y la imagen
st.markdown(
    """
    <style>
    .titulo {
        background-color: #f0f0f0; /* Color de fondo del título */
        color: #333333; /* Color del texto del título */
        padding: 10px; /* Espaciado interno del título */
        border-radius: 10px; /* Radio de borde del título */
    }

    .imagen {
        width: 100%; /* Ancho completo horizontalmente */
        border-radius: 10px; /* Radio de borde de la imagen */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Añadir la imagen con la clase CSS personalizada
imagen_url = "https://intranet.upch.edu.pe/account/static/img/upch/logo/isotipo.jpg"
st.markdown(
    f'<img src="{imagen_url}" class="imagen">',
    unsafe_allow_html=True
)

# Añadir el título con la clase CSS personalizada
st.markdown('<h1 class="titulo">Portal de Matrícula</h1>', unsafe_allow_html=True)
