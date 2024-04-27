import streamlit as st
import pandas as pd

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
                show_logged_in_content(username)
            else:
                st.error("Usuario o contraseña incorrectos")

# Función para mostrar la nueva sección después de iniciar sesión
def show_logged_in_content(username):
    st.markdown(f"<h2 style='text-align: center;'>BIENVENIDO, {username}</h2>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>En este apartado podrás verificar, ver, y coordinar los cursos cupos y disponibilidad</h6>", unsafe_allow_html=True)
    
    st.header("Archivo CSV - PLAN DE ESTUDIOS")
    
    url_csv = "https://raw.githubusercontent.com/Alexandeeer1/Proyecto_matricula/94a5f65b0920df8b0f0ad31270c101d381f62546/PLAN_DE_ESTUDIOS.csv"
    df = pd.read_csv(url_csv)
    
    st.write(df)

# Mostrar la página de inicio de sesión por defecto
login_page()
