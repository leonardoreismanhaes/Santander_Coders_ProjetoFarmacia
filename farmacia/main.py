from clientes import *
from medicamentos import *
from laboratorio import *
from vendas import *

class MenuGeral:

    def __init__(self) -> None:
        pass

    def run(self):

        medicamento = CadastroMedicamento()
        venda = CadastroVenda()
        
        print('\nMenu\n1 - Clientes\n2 - Laboratórios\n3 - Medicamentos\n4 - Vendas\n0 - Sair')
        acao_menu = int(input('\nSelecione uma opção (1, 2, 3, ou 0 para sair): '))
        
        while acao_menu != 0:
            
            if acao_menu == 1:
                MenuCliente.run()
                
            elif acao_menu == 2:
                pass
                MenuLaboratorio.run()
            
            elif acao_menu == 3:
                pass
                # MenuMedicamento.run()

            elif acao_menu == 4:
                pass
                # MenuVenda.run()
            
            print('\nMenu\n1 - Clientes\n2 - Laboratórios\n3 - Medicamentos\n4 - Vendas\n0 - Sair')
            acao_menu = int(input('\nSelecione uma opção (1, 2, 3, ou 0 para sair): '))
        
        print('\n===Fim===')

class MenuCliente:

    def __init__(self) -> None:
        pass

    def run():

        cliente = CadastroCliente()
        
        print('\nMenu\n1 - Cadastrar cliente\n2 - Consultar cliente\n3 - Listar clientes\n0 - Menu principal')
        acao_menu = int(input('\nSelecione uma opção (1, 2, 3, ou 0 para voltar ao Menu principal): '))
        
        if acao_menu == 0:
            menu.run()

        elif acao_menu == 1:
            print('\n===Cadastrar cliente===\n')
            cliente.cadastrar_novo()
            
        elif acao_menu == 2:
            print('\n===Consultar cliente===\n')
            cpf = input('Digite o CPF: ')
            cliente.visualizar_cadastro(cpf)
        
        elif acao_menu == 3:
            print('\n===Listar clientes===\n')
            cliente.listar_clientes()
        
        else:
            print('\nOpção não localizada.\nMenu\n1 - Cadastrar cliente\n2 - Consultar cliente\n3 - Listar clientes\n0 - Menu principal')
            acao_menu = int(input('Selecione uma opção (1, 2, 3, ou 0 para voltar ao Menu principal): '))

class MenuLaboratorio:

    def __init__(self) -> None:
        pass

    def run():

        laboratorio = CadastroLaboratorio()
        
        print('\nMenu\n1 - Cadastrar laboratório\n2 - Listar laboratórios\n0 - Menu principal')
        acao_menu = int(input('\nSelecione uma opção (1, 2, ou 0 para voltar ao Menu principal): '))
        
        if acao_menu == 0:
            menu.run()

        elif acao_menu == 1:
            print('\n===Cadastrar laboratório===\n')
            laboratorio.cadastrar_novo()
            
        elif acao_menu == 2:
            print('\n===Listar laboratórios===\n')
            laboratorio.listar_laboratorios()
        
        else:
            print('\nOpção não localizada.\nMenu\n1 - Cadastrar laboratório\n2 - Listar laboratórios\n0 - Menu principal')
            acao_menu = int(input('Selecione uma opção (1, 2, ou 0 para voltar ao Menu principal): '))

menu = MenuGeral()
menu.run()