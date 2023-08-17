import streamlit as st

from functions.clientes import Cliente

st.set_page_config(page_title="Clientes - Farmacia")

cont1 = st.container()

titulo_busca = cont1.title('Buscar cliente')

with cont1.form("buscar_cliente", clear_on_submit=True):
    cpf_client_busca = st.text_input('CPF do cliente: ')

    submitted = st.form_submit_button("BUSCAR")
    if submitted and cpf_client_busca:
        try:
            resultado = Cliente.buscar(cpf_client_busca)
            st.success(f'{resultado}')
        except:
            e = ValueError('CPF não cadastrado')
            st.exception(e)

cont2 = st.container()
titulo_lista = cont2.title('Lista de clientes cadastrados')

if Cliente.lista_clientes:
    exibe1 = cont2.text_area('tx', label_visibility="hidden", value=f'{Cliente.listar()}', height=550)

