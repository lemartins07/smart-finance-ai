import streamlit as st
from components.sidebar import show_sidebar
# Configuração da página
st.set_page_config(page_title="SmartFinance AI", layout="wide")

show_sidebar()

st.title("🏠 Dashboard Financeiro")
st.write("Aqui você verá um resumo das suas finanças.")

