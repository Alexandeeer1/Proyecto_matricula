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
    st.markdown("<h6 style='text-align: center;'>En este apartado podras verificar, ver, y coordinar los cursos cupos y disponibilidad</h6>", unsafe_allow_html=True)
    st.header("PLAN DE ESTUDIOS:")
    url_csv = "https://raw.githubusercontent.com/Alexandeeer1/Proyecto_matricula/94a5f65b0920df8b0f0ad31270c101d381f62546/PLAN_DE_ESTUDIOS.csv"
    df_plan_estudios = pd.read_csv(url_csv)
    st.write("DataFrame de plan de estudios:", df_plan_estudios)  # Mostrar DataFrame para depuración
    #####################################
    # Obtener los ciclos disponibles en el DataFrame
    ciclos = df_plan_estudios['CICLO'].unique()
    st.write("Ciclos disponibles:", ciclos)  # Mostrar los ciclos para depuración

    # Widget multiselect para seleccionar los ciclos
    selected_ciclos = st.multiselect("Seleccione los ciclos:", ciclos)
    st.write("Ciclos seleccionados:", selected_ciclos)  # Mostrar los ciclos seleccionados para depuración

    # Filtrar el DataFrame por los ciclos seleccionados
    filtered_df = df_plan_estudios[df_plan_estudios['CICLO'].isin(selected_ciclos)]
    st.write("DataFrame filtrado:", filtered_df)  # Mostrar el DataFrame filtrado para depuración

    # Mostrar el DataFrame filtrado
    st.write(filtered_df)

# Mostrar la página de inicio de sesión
login_page()
