from clientes import Cliente


class CadastroCliente:

    def __init__(self) -> None:
        self.cadastrados = {}

    def cadastrar_novo(self) -> None:
        nome = input("Digite o nome do cliente: ")
        email = input('Digite o email do cliente: ')
        cpf = input('Digite o CPF do cliente: ')

        if cpf not in self.cadastrados:
            novo_cliente = Cliente(nome, email, cpf)
            self.cadastrados[cpf] = novo_cliente
        else:
            raise ValueError('CPF já cadastrado')

    def visualizar_cadastro(self, cpf) -> None:
        for cpf in self.cadastrados:
            if cpf == self.cadastrados[cpf]:
                print(self.cadastrados[cpf])

    def alterar_cadastro(self, cpf):
        if cpf not in self.cadastrados:
            print('CPF não cadastrado')
            return
        cliente = self.cadastrados[cpf]
        alteracao = input('O que deseja alterar? ')

        while alteracao.lower() not in ('nome', 'email', 'cpf'):
            alteracao = input('Não foi possível encontrar o critério informado. O que deseja alterar? ')

        if alteracao == 'nome':
            novo_nome = input('Digite o novo nome: ')
            cliente.nome = novo_nome

        elif alteracao == 'email':
            novo_email = input('Digite o novo e-mail: ')
            cliente.email = novo_email

        elif alteracao == 'cpf':
            novo_cpf = input('Digite o novo CPF: ')
            cliente.cpf = novo_cpf
            self.cadastrados.pop(cpf)

        self.cadastrados[cliente.cpf] = cliente

    def run(self):

        print('Menu\n1 - Novo cadastro\n2 - Procurar cadastro\n3 - Alterar cadastro\n0 - Sair')
        acao_menu = int(input('O que deseja fazer? '))

        while acao_menu != 0:

            if acao_menu == 1:
                print('===Novo cadastro===\n')
                self.cadastrar_novo()
                print('\n===Fim do cadastro===')

            elif acao_menu == 2:
                print('===Procurar cadastrado===\n')
                cpf_a_procurar = input('Digite o CPF: ')
                self.visualizar_cadastro(cpf_a_procurar)
                print('\n===Fim da visualização===')

            elif acao_menu == 3:
                print('===Alterar cadastros===\n')
                cpf_a_alterar = input('Digite o CPF a ser alterado: ')
                self.alterar_cadastro(cpf_a_alterar)
                print('\n===Fim da alteração===')

            print('Menu\n1 - Novo cadastro\n2 - Visualizar cadastros\n3 - Alterar cadastro\n0 - Sair')
            acao_menu = int(input("O que deseja fazer? "))

        print('===Fim===')
