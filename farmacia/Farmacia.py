import streamlit as st
from datetime import date
from functions.clientes import Cliente
from functions.laboratorios import Laboratorio
from functions.medicamentos import Medicamentos, Fitoterapicos, Quimioterapicos

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

with cad_lab_wind.form("cadastrar_laboratorio", clear_on_submit=True):
    nome_lab_cad = st.text_input('Nome: ')
    endereco_lab_cad = st.text_input('Endereco: ')
    telefone_lab_cad = st.text_input('Telefone: ')
    cidade_lab_cad = st.text_input('Cidade: ')
    estado_lab_cad = st.text_input('Estado: ')

    submitted = st.form_submit_button("CADASTRAR")
    if nome_lab_cad and endereco_lab_cad and telefone_lab_cad and cidade_lab_cad and estado_lab_cad:
        if submitted:
            try:
                Laboratorio.cadastrar(nome_lab_cad.title(), endereco_lab_cad, telefone_lab_cad,
                                      cidade_lab_cad, estado_lab_cad)
                st.success('Cadastro realizado')
            except:
                e = ValueError('Laboratorio já cadastrado')
                st.exception(e)

    else:
        st.info('Preencha com todos os dados')

cont4 = st.container()
cad_medicamento_wind = cont4.expander('Cadastrar novo medicamento')
tipo_medicamento_cad = cad_medicamento_wind.radio('Tipo do medicamento: ', options=['Fitoterapico', 'Quimioterapico'],
                                horizontal=True)
if tipo_medicamento_cad == 'Quimioterapico':
    receita_medicamento_cad = cad_medicamento_wind.selectbox('precisa de receita: ', options=['Não', 'Sim'])

with cad_medicamento_wind.form("cadastrar_medicamento", clear_on_submit=True):
    nome_medicamento_cad = st.text_input('Nome: ')
    composto_medicamento_cad = st.text_input('composto: ')
    laboratorio_medicamento_cad = st.selectbox('laboratorio: ', options=list(Laboratorio.listar()))
    descricao_medicamento_cad = st.text_area('descricao: ')

    if tipo_medicamento_cad == 'Quimioterapico':
        submitted = st.form_submit_button("CADASTRAR Quimioterapico")
        if nome_medicamento_cad and composto_medicamento_cad and laboratorio_medicamento_cad and descricao_medicamento_cad:
            if submitted:
                try:
                    Quimioterapicos.cadastrar(nome_medicamento_cad.title(), composto_medicamento_cad.title(),
                                              laboratorio_medicamento_cad.title(), descricao_medicamento_cad,
                                              receita_medicamento_cad)
                    st.success('Cadastro realizado')
                except:
                    e = ValueError('Medicamento já cadastrado')
                    st.exception(e)

        else:
            st.info('Preencha com todos os dados')
    if tipo_medicamento_cad == 'Fitoterapico':
        submitted = st.form_submit_button("CADASTRAR Fitoterapico")
        if nome_medicamento_cad and composto_medicamento_cad and laboratorio_medicamento_cad and descricao_medicamento_cad:
            if submitted:
                try:
                    Fitoterapicos.cadastrar(nome_medicamento_cad.title(), composto_medicamento_cad.title(),
                                            laboratorio_medicamento_cad.title(), descricao_medicamento_cad)
                    st.success('Cadastro realizado')
                except:
                    e = ValueError('Medicamento já cadastrado')
                    st.exception(e)

        else:
            st.info('Preencha com todos os dados')



cont5 = st.container()
cad_venda_wind = cont5.expander('Registrar nova venda')

data_hoje = date.today()
data_hoje = data_hoje.strftime("%d/%m/%y")
data_venda = cad_venda_wind.text(f'Hoje é : {data_hoje}')
