import streamlit as st

# Establecer el color de fondo y el color del texto del título
st.markdown(
    """
    <style>
    .titulo {
        background-color: #f0f0f0; /* Color de fondo del título */
        color: #333333; /* Color del texto del título */
        padding: 10px; /* Espaciado interno del título */
        border-radius: 10px; /* Radio de borde del título */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Añadir el título con la clase CSS personalizada
st.markdown('<h1 class="titulo">Portal de Matrícula</h1>', unsafe_allow_html=True)
