from cadastro_cliente import *

class Menu:

    def __init__(self) -> None:
        pass

    def run(self):

        cadastro = CadastroCliente()
        
        print('Menu\n1 - Novo cadastro\n2 - Procurar cadastro\n3 - Alterar cadastro\n0 - Sair')
        acao_menu = int(input('O que deseja fazer? '))
        
        while acao_menu != 0:
            
            if acao_menu == 1:
                print('===Novo cadastro===\n')
                cadastro.cadastrar_novo()
                print('\n===Fim do cadastro===')
                
            elif acao_menu == 2:
                print('===Procurar cadastrado===\n')
                cpf_a_procurar = input('Digite o CPF: ')
                cadastro.visualizar_cadastro(cpf_a_procurar)
                print('\n===Fim da visualização===')
            
            elif acao_menu == 3:
                print('===Alterar cadastros===\n')
                cpf_a_alterar = input('Digite o CPF a ser alterado: ')
                cadastro.alterar_cadastro(cpf_a_alterar)
                print('\n===Fim da alteração===')
            
            print('Menu\n1 - Novo cadastro\n2 - Visualizar cadastros\n3 - Alterar cadastro\n0 - Sair')
            acao_menu = int(input("O que deseja fazer? "))
        
        print('===Fim===')

menu = Menu()
menu.run()