import streamlit as st
from components.sidebar import show_sidebar

show_sidebar()

st.title("💰 Cadastro de Transações")
st.write("Adicione suas receitas e despesas manualmente ou via OCR.")

transaction_type = st.radio("Tipo", ["Receita", "Despesa"])
amount = st.number_input("Valor", min_value=0.0, format="%.2f")

category = st.selectbox("Categoria", ["Alimentação", "Transporte", "Lazer", "Outros"])
description = st.text_area("Descrição")

if st.button("Adicionar Transação"):
    st.success(f"Transação de {amount} adicionada com sucesso!")
