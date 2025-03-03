import streamlit as st
from components.sidebar import show_sidebar

st.set_page_config(page_title="Análise", layout="wide")
show_sidebar()

st.title("📈 Análise de Dados")
st.write("Visualize gráficos e relatórios sobre suas finanças.")

st.line_chart([100, 200, 150, 250, 300])
