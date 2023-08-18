import streamlit as st

from functions.medicamentos import Medicamentos, Fitoterapicos, Quimioterapicos

st.set_page_config(page_title="Medicamentos - Farmacia")


cont2 = st.container()

subtitulo_1 = cont2.title('Medicamentos Quimioterapicos')

titulo_busca_1 = cont2.subheader('Buscar Quimioterapico')

with cont2.form("buscar_quimio", clear_on_submit=True):
    nome_quimio_busca = st.text_input('Nome do medicamento: ')

    submitted = st.form_submit_button("BUSCAR")
    if submitted and nome_quimio_busca:
        try:
            resultado = Quimioterapicos.buscar(nome_quimio_busca)
            st.success(f'{resultado}')
        except:
            e = ValueError('Medicamento não cadastrado')
            st.exception(e)


cont22 = st.container()
titulo_lista = cont22.subheader('Lista de medicamentos cadastrados')

if Quimioterapicos.lista_medicamentos:
    exibe1 = cont22.text_area('tx', label_visibility="hidden", value=f'{Quimioterapicos.listar()}', height=550)

cont3 = st.container()

subtitulo_2 = cont3.title('Medicamentos Fitoterapicos')

titulo_busca_2 = cont3.subheader('Buscar Fitoterapico')

with cont3.form("buscar_fito", clear_on_submit=True):
    nome_fito_busca = st.text_input('Nome do medicamento: ')

    submitted = st.form_submit_button("BUSCAR")
    if submitted and nome_fito_busca:
        try:
            resultado = Fitoterapicos.buscar(nome_fito_busca)
            st.success(f'{resultado}')
        except:
            e = ValueError('Medicamento não cadastrado')
            st.exception(e)


cont33 = st.container()
titulo_lista = cont33.subheader('Lista de medicamentos cadastrados')

if Fitoterapicos.lista_medicamentos:
    exibe1 = cont33.text_area('tx', label_visibility="hidden", value=f'{Fitoterapicos.listar()}', height=550)
