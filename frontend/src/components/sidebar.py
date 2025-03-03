import streamlit as st

def show_sidebar():
    """Exibe a barra lateral com a navegação personalizada."""
    st.sidebar.title("SmartFinance AI")
    
    st.sidebar.page_link("pages/dashboard.py", label="Dashboard", icon="🏡")
    st.sidebar.page_link("pages/transactions.py", label="Transações", icon="💳")
    st.sidebar.page_link("pages/analysis.py", label="Análise", icon="📈")
    st.sidebar.page_link("pages/settings.py", label="Configurações", icon="🔧")
