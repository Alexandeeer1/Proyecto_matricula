import streamlit as st

# Establecer el estilo CSS para el diseño principal y el contenedor interno
st.markdown(
    """
    <style>
    .layout-container {
        width: 100%;
        height: 100vh; /* Altura total de la ventana */
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .content-container {
        max-width: 80%; /* Ancho máximo del contenido */
        padding: 20px; /* Espaciado interno del contenido */
        background-color: #f0f0f0; /* Color de fondo del contenido */
        border-radius: 10px; /* Radio de borde del contenido */
    }

    .titulo {
        text-align: center; /* Centrar el texto del título */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Contenedor principal que ocupa toda la pantalla
st.markdown('<div class="layout-container">', unsafe_allow_html=True)

# Contenedor interno para el contenido
st.markdown('<div class="content-container">', unsafe_allow_html=True)

# Agrega tus elementos dentro de este contenedor
imagen_url = "https://intranet.upch.edu.pe/account/static/img/upch/logo/isotipo.jpg"
st.markdown(
    f'<div style="text-align:center"><img src="{imagen_url}" style="width: 50%; border-radius: 10px;"></div>',
    unsafe_allow_html=True
)

st.markdown('<h1 class="titulo">Portal de Matrícula</h1>', unsafe_allow_html=True)

# Cierre del contenedor interno
st.markdown('</div>', unsafe_allow_html=True)

# Cierre del contenedor principal
st.markdown('</div>', unsafe_allow_html=True)
