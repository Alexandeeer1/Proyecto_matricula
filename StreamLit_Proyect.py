import streamlit as st
import pandas as pd

# Cargar la base de datos de usuarios desde un archivo CSV
import requests
import pandas as pd

url = "https://raw.githubusercontent.com/Alexandeeer1/Proyecto_matricula/main/uss_pass.csv"
response = requests.get(url)
usuarios_df = pd.read_csv(response.text)

def login(usuario, contraseña):
    """Función para verificar si el usuario y la contraseña son válidos"""
    if usuario in usuarios_df["Usuario"].values:
        index = usuarios_df.index[usuarios_df["Usuario"] == usuario][0]
        if usuarios_df.at[index, "Contraseña"] == contraseña:
            return True
    return False

# Página de inicio de sesión
def main():
    st.title("Página de Inicio de Sesión")

    # Campos de entrada para usuario y contraseña
    usuario = st.text_input("Usuario")
    contraseña = st.text_input("Contraseña", type="password")

    # Botón para iniciar sesión
    if st.button("Iniciar Sesión"):
        if login(usuario, contraseña):
            st.success("Inicio de sesión exitoso!")
            # Redirigir a otra página después del inicio de sesión
            st.write("Aquí puedes colocar el código para redirigir a otra página")
        else:
            st.error("Usuario o contraseña incorrectos")

if __name__ == "__main__":
    main()
