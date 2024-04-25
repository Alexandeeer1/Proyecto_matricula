import streamlit as st
import sqlite3
# Sidebar
st.sidebar.title("Navegación")
opcion = st.sidebar.radio("Selecciona una opción", ["Inicio", "Iniciar sesión"])

# Título centrado
st.write("""
<div style='text-align: center;'>
    <h1>Mi Aplicación</h1>
</div>
""", unsafe_allow_html=True)

# Página de inicio de sesión
if opcion == "Iniciar sesión":
    st.write("## Inicio de sesión")
    usuario = st.text_input("Usuario")
    contraseña = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        # Aquí puedes agregar la lógica para autenticar al usuario
        st.success("Inicio de sesión exitoso")

# Página de inicio
elif opcion == "Inicio":
    st.write("## Bienvenido a mi aplicación")
    # Aquí puedes agregar el contenido de la página de inicio

def verificar_credenciales(usuario, contraseña):
    # Conectar a la base de datos
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Consultar las credenciales del usuario
    c.execute("SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?", (usuario, contraseña))
    resultado = c.fetchone()

    # Cerrar la conexión
    conn.close()

    # Si se encontró un resultado, las credenciales son válidas
    if resultado:
        return True
    else:
        return False

if opcion == "Iniciar sesión":
    st.write("## Inicio de sesión")
    usuario = st.text_input("Usuario")
    contraseña = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        if verificar_credenciales(usuario, contraseña):
            # Redirigir a la nueva pestaña
            st.session_state.autenticado = True
        else:
            st.error("Credenciales inválidas")
