LEN_CPF = 11 # tamanho do campo CPF
LEN_DATA = 8 # tamanho dos campos de data

class Cliente:

    dic_clientes = {}

    def __init__(self, nome: str, cpf: str, dt_nascimento: str) -> None:
        self.nome = nome
        self._cpf = cpf
        self.dt_nascimento = dt_nascimento

    @property
    def cpf(self):
        return self._cpf

    def __repr__(self) -> str:
        cpf_formatado = f'{self.cpf[:3]}.***.{self.cpf[6:9]}-{self.cpf[9:]}'
        dt_nascimento_formatada = f'{self.dt_nascimento[:2]}/{self.dt_nascimento[2:4]}/{self.dt_nascimento[4:]}'        
        representacao = '\nNome: ' + self.nome + '\nCPF: ' + cpf_formatado + '\nData de nascimento: ' + dt_nascimento_formatada
        return representacao
class CadastroCliente:
    
    def __init__(self) -> None:
        pass
        
    def cadastrar_novo(self) -> None:
        nome = input("Digite o nome do cliente: ")

        cpf = input('Digite o CPF do cliente (apenas dígitos): ')
        while len(cpf) != LEN_CPF:
            print('O CPF deve conter 11 dígitos.')
            cpf = input('Digite o CPF do cliente (apenas dígitos): ')
            
        dt_nascimento = input('Digite a data de nascimento do cliente (ddmmaaaa): ')
        while len(dt_nascimento) != LEN_DATA:
            print('A data de nascimento deve estar no formato ddmmaaaa.')
            cpf = input('Digite a data de nascimento do cliente (ddmmaaaa):')
        
        if cpf not in Cliente.dic_clientes:
            novo_cliente = Cliente(nome, cpf, dt_nascimento)
            Cliente.dic_clientes[cpf] = novo_cliente
        else:
            print('CPF já cadastrado')

        print(f'\n=== Cliente cadastrado === {novo_cliente}')
            
    def visualizar_cadastro(self, cpf):
        for cadastro in Cliente.dic_clientes:
            if cpf == cadastro:
                print(Cliente.dic_clientes[cadastro])
            if cpf not in Cliente.dic_clientes:
                print('CPF não cadastrado.')

    def listar_clientes(self):
        sorted_dic = sorted(Cliente.dic_clientes.values(), key=lambda cliente:cliente.nome)
        for cliente in sorted_dic:
            print(cliente)


