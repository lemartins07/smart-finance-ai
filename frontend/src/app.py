import sys
import streamlit as st


sys.stdout.reconfigure(line_buffering=True)

# Oculta o menu automático do Streamlit
st.set_page_config(page_title="SmartFinance AI", layout="wide")

# Configuração do menu lateral
st.sidebar.title("SmartFinance AI")

# Redirecionar para a página do Dashboard automaticamente
st.switch_page("pages/dashboard.py")

# Exibir uma mensagem de carregamento (caso necessário)
st.write("Redirecionando para o Dashboard...")
