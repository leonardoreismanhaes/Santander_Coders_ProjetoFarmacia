import streamlit as st

from functions.laboratorios import Laboratorio

st.set_page_config(page_title="Laboratorios - Farmacia")

cont1 = st.container()

titulo_busca = cont1.title('Buscar laboratorio')

with cont1.form("buscar_lab", clear_on_submit=True):
    nome_lab_busca = st.text_input('Nome do laboratorio: ')

    submitted = st.form_submit_button("BUSCAR")
    if submitted and nome_lab_busca:
        try:
            resultado = Laboratorio.buscar(nome_lab_busca)
            st.success(f'{resultado}')
        except:
            e = ValueError('Laboratorio não cadastrado')
            st.exception(e)


cont2 = st.container()
titulo_lista = cont2.title('Lista de laboratorios cadastrados')

if Laboratorio.lista_laboratorios:
    exibe1 = cont2.text_area('tx', label_visibility="hidden", value=f'{Laboratorio.listar()}', height=550)




