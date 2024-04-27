
import streamlit as st
import pandas as pd

url_csv = "https://raw.githubusercontent.com/Alexandeeer1/Proyecto_matricula/7cd2140758281c22508e80f81d4e78c34360d983/uss_pass.csv"
df = pd.read_csv(url_csv)
st.markdown("<h1 style='text-align: center;'>𝐏𝐎𝐑𝐓𝐀𝐋 𝐃𝐄 𝐌𝐀𝐓𝐑𝐈𝐂𝐔𝐋𝐀 𝐂𝐀𝐘𝐄𝐓𝐀𝐍𝐎</h1>", unsafe_allow_html=True)
url_imagen = "https://intranet.upch.edu.pe/account/static/img/upch/logo/isotipo.jpg"
st.markdown(f'<div style="text-align: center; border-radius: 20px; overflow: hidden; margin-bottom: 50px;"><img src="{url_imagen}" width="200" style="border-radius: 20px;"></div>', unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>INICIE SESIÓN</h2>", unsafe_allow_html=True)
#####################################################################################

with st.form(key='login_form'):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button(label='Inicie Sesión')
    if submit_button:
        if (df['Usuarios'] == int(username)).any() and (df['Contraseña'] == password).any():
            st.success("¡Inicio de sesión exitoso!")
        else:
            st.error("Usuario o contraseña incorrectos")


