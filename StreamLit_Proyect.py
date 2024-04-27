import streamlit as st

st.markdown("<h1 style='text-align: center;'>Mi Página en Streamlit</h1>", unsafe_allow_html=True)

url_imagen = "https://intranet.upch.edu.pe/account/static/img/upch/logo/isotipo.jpg"
st.markdown(f'<div style="text-align: center; border-radius: 20px; overflow: hidden;"><img src="{url_imagen}" width="200" style="border-radius: 20px;"></div>', unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Iniciar Sesión</h2>", unsafe_allow_html=True)
#############################################################################################################################
# Formulario de login
username = st.text_input("Usuario")
password = st.text_input("Contraseña", type="password")

if st.button("Iniciar Sesión"):
    # Aquí puedes agregar la lógica para verificar el usuario y contraseña
    # Por ejemplo, puedes comparar los valores ingresados con credenciales predefinidas
    if username == "usuario" and password == "contraseña":
        st.success("¡Inicio de sesión exitoso!")
    else:
        st.error("Usuario o contraseña incorrectos")
