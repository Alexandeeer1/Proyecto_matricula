import streamlit as st
import pandas as pd

# Configurar el diseño de la página
st.set_page_config(page_title="Gestión de Cursos UPCH", page_icon=":books:", layout="wide")

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
                show_logged_in_content(username)
            else:
                st.error("Usuario o contraseña incorrectos")

# Función para mostrar la nueva sección después de iniciar sesión
def show_logged_in_content(username):
    st.markdown(f"<h2 style='text-align: center;'>BIENVENIDO, {username}</h2>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>En este apartado podrás verificar, ver, y coordinar los cursos cupos y disponibilidad</h6>", unsafe_allow_html=True)
    st.header("Gestión de Cursos UPCH")

    # Cargar datos desde el archivo CSV
    url_csv_plan = "https://raw.githubusercontent.com/Alexandeeer1/Proyecto_matricula/94a5f65b0920df8b0f0ad31270c101d381f62546/PLAN_DE_ESTUDIOS.csv"
    data = pd.read_csv(url_csv_plan)

    # Encabezado y descripción
    st.title("Gestión de Cursos de Ingeniería Informática - UPCH")
    st.write("Esta aplicación web permite visualizar los cursos de los 10 ciclos de la carrera de Ingeniería Informática en la Universidad Peruana Cayetano Heredia (UPCH), junto con sus prerrequisitos y detalles.")

    # Estilos CSS
    hide_table_row_index = """
                <style>
                tbody th:nth-child(2), tbody td:nth-child(2) { background-color: #F0F8FF; } /* Color de fondo para la columna "CICLO" */
                .styled th:nth-child(2), .styled td:nth-child(2) { background-color: #F0F8FF; } /* Color de fondo para la columna "CICLO" en la tabla generada */
                tbody th {display:none;}
                .blank {display:none;}
                </style>
                """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    # Función para obtener el color de fondo según el ciclo
    def get_bg_color(ciclo):
        return ""  # Sin color de fondo

    # Mostrar los cursos por ciclo
    for ciclo in data["CICLO"].unique():
        cursos = data[data["CICLO"] == ciclo]
        centered_ciclo = f"<div style='text-align: center; font-size: 36px; font-weight: bold;'>{ciclo}</div>"
        st.markdown(centered_ciclo, unsafe_allow_html=True)
        st.write(cursos.to_html(classes=["styled"], index=False), unsafe_allow_html=True)

    # Nota al pie
    st.write("Nota: Los cursos en color tienen prerrequisitos que deben ser aprobados antes de llevarlos.")

# Mostrar la página de inicio de sesión por defecto
login_page()
