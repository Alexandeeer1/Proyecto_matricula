import streamlit as st
import pandas as pd

url_csv = "https://raw.githubusercontent.com/Alexandeeer1/Proyecto_matricula/7cd2140758281c22508e80f81d4e78c34360d983/uss_pass.csv"
df = pd.read_csv(url_csv)
st.markdown("<h1 style='text-align: center;'>PORTAL DE MATRICULA CAYETANO</h1>", unsafe_allow_html=True)
url_imagen = "https://intranet.upch.edu.pe/account/static/img/upch/logo/isotipo.jpg"
st.markdown(f'<div style="text-align: center; border-radius: 20px; overflow: hidden; margin-bottom: 50px;"><img src="{url_imagen}" width="200" style="border-radius: 20px;"></div>', unsafe_allow_html=True)

#####################################################################################
# Página de inicio de sesión
def login_page():
    st.markdown("<h2 style='text-align: center;'>INICIE SESIÓN</h2>", unsafe_allow_html=True)
    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button(label='Inicie Sesión')
        if submit_button:
            if (df['Usuarios'] == int(username)).any() and (df['Contraseña'] == password).any():
                st.success("¡Inicio de sesión exitoso!")
                # Llamar a la función para mostrar la nueva sección
                show_logged_in_section()
            else:
                st.error("Usuario o contraseña incorrectos")

# Función para mostrar la nueva sección después de iniciar sesión
def show_logged_in_section():
    st.sidebar.title("Menú")
    selected_section = st.sidebar.selectbox("Seleccione una opción", ["Inicio", "Perfil", "Otra sección"])
    if selected_section == "Inicio":
        return show_home_page()
    elif selected_section == "Perfil":
        return show_profile_page()
    elif selected_section == "Otra sección":
        return show_other_page()

# Función para mostrar la página de inicio
def show_home_page():
    st.markdown("<h2 style='text-align: center;'>Bienvenido a la página de inicio</h2>", unsafe_allow_html=True)
    st.write("Aquí puedes agregar el contenido de la página de inicio")

# Función para mostrar la página de perfil
def show_profile_page():
    st.markdown("<h2 style='text-align: center;'>Perfil de usuario</h2>", unsafe_allow_html=True)
    st.write("Aquí puedes ver y editar tu perfil")

# Función para mostrar otra página
def show_other_page():
    st.markdown("<h2 style='text-align: center;'>Otra sección</h2>", unsafe_allow_html=True)
    st.write("Aquí puedes agregar el contenido de otra sección")

# Mostrar la página de inicio de sesión por defecto
login_page()
