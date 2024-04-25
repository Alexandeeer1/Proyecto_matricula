import streamlit as st
import hashlib

# Configuración de la página
st.set_page_config(page_title="Mi Aplicación", page_icon=":lock:", layout="wide")

# Título grande en el centro
st.title("Bienvenido a Mi Aplicación")
st.write("")  # Espacio en blanco para separar el título del formulario

# Formulario de login
with st.form("login_form"):
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    submit_button = st.form_submit_button("Iniciar sesión")

# Función para autenticar al usuario
def authenticate(username, password):
    # En un sistema real, aquí deberías consultar una base de datos o un servicio de autenticación
    # Para fines de demostración, solo voy a verificar si el usuario y contraseña son "admin"
    if username == "admin" and password == "admin":
        return True
    else:
        return False

# Procesar el formulario de login
if submit_button:
    if authenticate(username, password):
        # Redirigir a la página de bienvenida si el usuario se autentica correctamente
        st.session_state["authenticated"] = True
        st.write("¡Bienvenido!")
        st.write("Has iniciado sesión correctamente.")
        st.button("Ir a la página de bienvenida", on_click=lambda: st.write("¡Hola!"))
    else:
        st.error("Usuario o contraseña incorrectos")

# Página de bienvenida (solo se muestra si el usuario se autentica correctamente)
if "authenticated" in st.session_state and st.session_state["authenticated"]:
    st.title("Página de bienvenida")
    st.write("¡Hola! Has iniciado sesión correctamente.")
    st.button("Cerrar sesión", on_click=lambda: st.session_state["authenticated"] = False)
