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
            
    def visualizar_cadastro(self, cpf):
        for cadastro in self.cadastrados:
            if cpf == cadastro:
                print(self.cadastrados[cadastro])
            else:
                print('CPF não cadastrado')
            
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