import streamlit as st
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

