class Cliente:

    dic_clientes = {}

    def __init__(self, nome: str, cpf: str, dt_nascimento: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.dt_nascimento = dt_nascimento

    def __repr__(self) -> str:
        representacao = '\nNome: ' + self.nome
        representacao += '\nCPF: ' + self.cpf
        representacao += '\nData de nascimento: ' + self.dt_nascimento
        return representacao
class CadastroCliente:
    
    def __init__(self) -> None:
        pass
        
    def cadastrar_novo(self) -> None:
        nome = input("Digite o nome do cliente: ")
        cpf = input('Digite o CPF do cliente: ')
        dt_nascimento = input('Digite a data de nascimento do cliente: ')
        
        if cpf not in Cliente.dic_clientes:
            novo_cliente = Cliente(nome, cpf, dt_nascimento)
            Cliente.dic_clientes[cpf] = novo_cliente
        else:
            print('CPF já cadastrado')
            
    def visualizar_cadastro(self, cpf):
        for cadastro in Cliente.dic_clientes:
            if cpf == cadastro:
                print(Cliente.dic_clientes[cadastro])
            if cpf not in Cliente.dic_clientes:
                print('CPF não cadastrado.')

    def listar_clientes(self):
        sorted_dic = sorted(Cliente.dic_clientes.items(), key=lambda x:x[0])
        for cadastro in sorted_dic:
            print(cadastro)