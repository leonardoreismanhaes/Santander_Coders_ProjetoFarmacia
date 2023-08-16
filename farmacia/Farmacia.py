import streamlit as st
from datetime import date


st.set_page_config(page_title="Farmacia E-commerce")

cont1 = st.container()

titulo_inicial = cont1.title('Olá! Bem vindo(a) a Farmacia')
subtitulo_inicial = cont1.subheader('selecione abaixo o que deseja fazer')

cont2 = st.container()
cad_cliente_wind = cont2.expander('Cadastrar novo cliente')

nome_client_cad = cad_cliente_wind.text_input('Nome do cliente: ')

cont3 = st.container()
cad_lab_wind = cont3.expander('Cadastrar novo laboratorio')

nome_lab_cad = cad_lab_wind.text_input('Nome do laboratorio: ')

cont4 = st.container()
cad_medicamento_wind = cont4.expander('Cadastrar novo medicamento')

nome_medicamento_cad = cad_medicamento_wind.text_input('Nome do medicamento: ')

cont5 = st.container()
cad_venda_wind = cont5.expander('Registrar nova venda')

data_hoje = date.today()
data_hoje = data_hoje.strftime("%d/%m/%y")
data_venda = cad_venda_wind.text(f'Hoje é : {data_hoje}')

