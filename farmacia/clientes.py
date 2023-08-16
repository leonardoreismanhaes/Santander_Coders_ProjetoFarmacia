class Cliente:

    def __init__(self, cpf:str, nome:str, data_nascimento:str, email:str) -> None:
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.email = email

    def __repr__(self) -> str:
        representacao = 'Nome: ' + self.nome
        representacao += '\nCPF: ' + self.cpf
        representacao += '\nData: ' + self.data_nascimento
        representacao += '\nE-mail: ' + self.email 
               
        return representacao
    
class CadastroCliente:
    
    def __init__(self) -> None:
        self.cadastrados = {}
        self.clientes = []
        
    def cadastrar_novo(self) -> None:
        cpf = input('Digite o CPF do cliente: ')
        nome = input("Digite o nome do cliente: ")
        dataNascimento = input('Digite o CPF do cliente: ')
        email = input('Digite o email do cliente: ')       
        
        if cpf not in self.cadastrados:
            novo_cliente = Cliente(cpf, nome, dataNascimento, email)
            self.cadastrados[cpf] = novo_cliente
        else:
            print('CPF já cadastrado')
            
    def visualizar_cadastro(self, cpf):
        if cpf in self.cadastrados:
            print(self.cadastrados[cpf])
        else:
            print('Cliente não encontrado.')
            
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
        
    def buscar_cliente_por_cpf(self, cpf):
        if cpf in self.cadastrados:
            return self.cadastrados[cpf]
        return None
    
    