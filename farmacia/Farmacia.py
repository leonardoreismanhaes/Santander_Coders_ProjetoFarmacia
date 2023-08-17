import streamlit as st
from datetime import date
from functions.clientes import Cliente

st.set_page_config(page_title="Farmacia E-commerce")

cont1 = st.container()

titulo_inicial = cont1.title('Olá! Bem vindo(a) a Farmacia')
subtitulo_inicial = cont1.subheader('selecione abaixo o que deseja fazer')

cont2 = st.container()
cad_cliente_wind = cont2.expander('Cadastrar novo cliente')

with cad_cliente_wind.form("cadastrar_cliente", clear_on_submit=True):
    nome_client_cad = st.text_input('Nome: ')
    data_nasc_client_cad = st.text_input('Data de nascimento: ')
    cpf_client_cad = st.text_input('CPF: ')
    email_client_cad = st.text_input('E-mail: ')

    submitted = st.form_submit_button("CADASTRAR")
    if nome_client_cad and data_nasc_client_cad and cpf_client_cad and email_client_cad:
        if submitted:
            try:
                Cliente.cadastrar(nome_client_cad.title(), data_nasc_client_cad, cpf_client_cad, email_client_cad)
                st.success('Cadastro realizado')
            except:
                e = ValueError('CPF já cadastrado')
                st.exception(e)

    else:
        st.info('Preencha com todos os dados')

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
