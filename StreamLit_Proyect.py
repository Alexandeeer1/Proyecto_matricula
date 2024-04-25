import streamlit as st
import csv

# Función para autenticar usuarios desde un archivo CSV
def authenticate_user(username, password):
    with open('uss_pass.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
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
