import streamlit as st
from components.sidebar import show_sidebar

st.set_page_config(page_title="Configurações", layout="wide")
show_sidebar()

st.title("⚙️ Configurações")
st.write("Gerencie categorias e preferências do app.")

st.checkbox("Ativar OCR para extrair dados automaticamente")
st.checkbox("Ativar notificações financeiras")
