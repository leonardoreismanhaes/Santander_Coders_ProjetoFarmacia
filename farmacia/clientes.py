class Cliente:

    def __init__(self, nome: str, cpf: str, dt_nascimento: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.dt_nascimento = dt_nascimento

    def __repr__(self) -> str:
        representacao = 'Nome: ' + self.nome
        representacao += '\nCPF: ' + self.cpf
        representacao += '\nData de nascimento: ' + self.dt_nascimento
        return representacao
class CadastroCliente:
    
    def __init__(self) -> None:
        self.cadastrados = {}
        
    def cadastrar_novo(self) -> None:
        nome = input("Digite o nome do cliente: ")
        cpf = input('Digite o CPF do cliente: ')
        dt_nascimento = input('Digite a data de nascimento do cliente: ')
        
        if cpf not in self.cadastrados:
            novo_cliente = Cliente(nome, dt_nascimento, cpf)
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
        
        while alteracao.lower() not in ('nome', 'nascimento', 'cpf'):
            alteracao = input('Não foi possível encontrar o critério informado. O que deseja alterar? ')
        
        if alteracao == 'nome':
            novo_nome = input('Digite o novo nome: ')
            cliente.nome = novo_nome
        
        elif alteracao == 'nascimento':
            nova_dt_nascimento = input('Digite a nova data de nascimento: ')
            cliente.dt_nascimento = nova_dt_nascimento
            
        elif alteracao == 'cpf':
            novo_cpf = input('Digite o novo CPF: ')
            cliente.cpf = novo_cpf
            self.cadastrados.pop(cpf)
            
        self.cadastrados[cliente.cpf] = cliente