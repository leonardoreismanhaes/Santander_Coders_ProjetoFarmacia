from clientes import *
from medicamentos import *
from laboratorio import *
from vendas import *
from teste import *

class MenuGeral:

    def __init__(self) -> None:
        pass

    def run(self):
        
        print('\nMenu\n1 - Clientes\n2 - Laboratórios\n3 - Medicamentos\n4 - Vendas\n0 - Sair')
        acao_menu = int(input('\nSelecione uma opção (1, 2, 3, 4, ou 0 para sair): '))
        
        while acao_menu != 0:
            
            if acao_menu == 1:
                MenuCliente.run()
                
            elif acao_menu == 2:
                pass
                MenuLaboratorio.run()
            
            elif acao_menu == 3:
                pass
                MenuMedicamento.run()

            elif acao_menu == 4:
                pass
                MenuVenda.run()
            
            print('\nMenu\n1 - Clientes\n2 - Laboratórios\n3 - Medicamentos\n4 - Vendas\n0 - Sair')
            acao_menu = int(input('\nSelecione uma opção (1, 2, 3, 4, ou 0 para sair): '))
        
        print(CadastroVenda.relatorio_vendas(self))
        print('\n=== Fim ===')

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
            print('\n=== Cadastrar cliente ===\n')
            cliente.cadastrar_novo()
            
        elif acao_menu == 2:
            print('\n=== Consultar cliente ===\n')
            cpf = input('Digite o CPF: ')
            cliente.visualizar_cadastro(cpf)
        
        elif acao_menu == 3:
            print('\n=== Listar clientes ===\n')
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
            print('\n=== Cadastrar laboratório ===\n')
            laboratorio.cadastrar_novo()
            
        elif acao_menu == 2:
            print('\n=== Listar laboratórios ===\n')
            laboratorio.listar_laboratorios()
        
        else:
            print('\nOpção não localizada.\nMenu\n1 - Cadastrar laboratório\n2 - Listar laboratórios\n0 - Menu principal')
            acao_menu = int(input('Selecione uma opção (1, 2, ou 0 para voltar ao Menu principal): '))

class MenuMedicamento:

    def __init__(self) -> None:
        pass

    def run():

        medicamento = CadastroMedicamento()
        
        print('\nMenu\n1 - Cadastrar medicamento\n2 - Listar medicamentos\n3 - Listar medicamentos fitoterápicos\n4 - Listar medicamentos quimioterápicos\n5 - Buscar medicamento por nome\n6 - Buscar medicamento por laboratório\n7 - Buscar medicamento por descrição\n0 - Menu principal')
        acao_menu = int(input('\nSelecione uma opção (1, 2, 3, 4, 5, 6, 7, ou 0 para voltar ao Menu principal): '))
        
        if acao_menu == 0:
            menu.run()

        elif acao_menu == 1:
            print('\n=== Cadastrar medicamento ===\n')
            medicamento.cadastrar_novo()
            
        elif acao_menu == 2:
            print('\n=== Listar medicamentos ===\n')
            medicamento.listar_medicamentos()

        elif acao_menu == 3:
            print('\n=== Listar medicamentos fitoterápicos ===\n')
            medicamento.listar_fitoterapicos()

        elif acao_menu == 4:
            print('\n=== Listar medicamentos quimioterápicos ===\n')
            medicamento.listar_quimioterapicos()

        elif acao_menu == 5:
            print('\n=== Buscar medicamento por nome ===\n')
            nome = input('Digite o nome do medicamento: ')
            medicamento.buscar_medicamento_nome(nome)

        elif acao_menu == 6:
            print('\n=== Buscar medicamento por laboratório ===\n')
            lab = input('Digite o nome do laboratório: ')
            medicamento.buscar_medicamento_laboratorio(lab)

        elif acao_menu == 7:
            print('\n=== Buscar medicamento por descrição ===\n')
            desc = input('Digite a descrição do medicamento: ')
            medicamento.buscar_medicamento_descricao(desc)
        
        else:
            print('\nMenu\n1 - Cadastrar medicamento\n2 - Listar medicamentos\n3 - Listar medicamentos fitoterápicos\n4 - Listar medicamentos quimioterápicos\n5 - Buscar medicamento por nome\n6 - Buscar medicamento por laboratório\n7 - Buscar medicamento por descrição\n0 - Menu principal')
            acao_menu = int(input('\nSelecione uma opção (1, 2, 3, 4, 5, 6, 7, ou 0 para voltar ao Menu principal): '))

class MenuVenda:

    def __init__(self) -> None:
        pass

    def run():

        venda = CadastroVenda()
        
        print('\nMenu\n1 - Cadastrar venda\n2 - Relatório de vendas\n0 - Menu principal')
        acao_menu = int(input('\nSelecione uma opção (1, 2, ou 0 para voltar ao Menu principal): '))
        
        if acao_menu == 0:
            menu.run()

        elif acao_menu == 1:
            print('\n=== Cadastrar venda ===\n')
            venda.cadastrar_venda()
            
        elif acao_menu == 2:
            print('\n=== Relatório de vendas ===\n')
            venda.relatorio_vendas()
        
        else:
            print('\nMenu\n1 - Cadastrar venda\n2 - Relatório de vendas\n0 - Menu principal')
            acao_menu = int(input('\nSelecione uma opção (1, 2, ou 0 para voltar ao Menu principal): '))

menu = MenuGeral()
menu.run()