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
                show_logged_in_content(username)
            else:
                st.error("Usuario o contraseña incorrectos")

# Función para mostrar la nueva sección después de iniciar sesión
def show_logged_in_content(username):
    st.markdown(f"<h2 style='text-align: center;'>BIENVENIDO, {username}</h2>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>En este apartado podrás verificar, ver, y coordinar los cursos cupos y disponibilidad</h6>", unsafe_allow_html=True)
    st.header("Gestión de Cursos UPCH")

    # Cargar datos desde el archivo CSV
    data = pd.read_csv("database.csv")

    # Configurar el diseño de la página
    st.set_page_config(page_title="Gestión de Cursos UPCH", page_icon=":books:", layout="wide")

    # Encabezado y descripción
    st.title("Gestión de Cursos de Ingeniería Informática - UPCH")
    st.write("Esta aplicación web permite visualizar los cursos de los 10 ciclos de la carrera de Ingeniería Informática en la Universidad Peruana Cayetano Heredia (UPCH), junto con sus prerrequisitos y detalles.")

    # Estilos CSS
    hide_table_row_index = """
                <style>
                tbody th {display:none;}
                .blank {display:none;}
                </style>
                """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    # Función para obtener el color de fondo según el ciclo
    def get_bg_color(ciclo):
        if ciclo.startswith("PRIMER"):
            return "#F0F8FF"  # Azul claro
        elif ciclo.startswith("SEGUNDO"):
            return "#E0FFFF"  # Turquesa claro
        elif ciclo.startswith("TERCER"):
            return "#FAFAD2"  # Amarillo claro
        elif ciclo.startswith("CUARTO"):
            return "#FAF0E6"  # Lino
        elif ciclo.startswith("QUINTO"):
            return "#FFF5EE"  # Seashell
        elif ciclo.startswith("SEXTO"):
            return "#F5F5DC"  # Beige
        elif ciclo.startswith("SEPTIMO"):
            return "#E6E6FA"  # Lavanda
        elif ciclo.startswith("OCTAVO"):
            return "#FFF0F5"  # Lavanda rojizo
        elif ciclo.startswith("NOVENO"):
            return "#F8F8FF"  # Azul fantasma
        elif ciclo.startswith("DECIMO"):
            return "#F5DEB3"  # Wheat
        else:
            return ""  # Sin color de fondo

    # Mostrar los cursos por ciclo
    for ciclo in data["CICLO"].unique():
        cursos = data[data["CICLO"] == ciclo]
        st.subheader(f"{ciclo}")
        st.write(cursos.style.apply(lambda x: [f"background-color: {get_bg_color(ciclo)}"] * len(x), axis=1).to_html(), unsafe_allow_html=True)

    # Nota al pie
    st.write("Nota: Los cursos en color tienen prerrequisitos que deben ser aprobados antes de llevarlos.")

# Mostrar la página de inicio de sesión por defecto
login_page()

