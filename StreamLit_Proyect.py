import streamlit as st
import csv
import requests
from io import StringIO

# URL del archivo CSV en GitHub
csv_url = 'https://raw.githubusercontent.com/Alexandeeer1/Proyecto_matricula/main/uss_pass.csv'

# Función para autenticar usuarios desde un archivo CSV en línea
def authenticate_user(username, password):
    # Descargar el contenido del archivo CSV desde la URL
    response = requests.get(csv_url)
    if response.status_code == 200:
        # Leer el contenido como un archivo CSV utilizando StringIO
        csv_data = StringIO(response.text)
        csv_reader = csv.DictReader(csv_data)
        for row in csv_reader:
            if row['username'] == username and row['password'] == password:
                return True
    return False

def main():
    st.title("Autenticación de Usuarios")

    username = st.text_input("Nombre de Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar Sesión"):
        if username and password:
            if authenticate_user(username, password):
                st.success(f"Bienvenido, {username}!")
            else:
                st.error("Credenciales incorrectas. Por favor, inténtalo de nuevo.")

if __name__ == "__main__":
    main()
