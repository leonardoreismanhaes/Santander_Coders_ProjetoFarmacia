LEN_ESTADO = 2 # tamanho do campo estado
LEN_TELEFONE = 10 # tamanho do campo telefone 

class Laboratorio:

    dic_laboratorios = {}

    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str) -> None:

        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado

    def __repr__(self) -> str:
        telefone_formatado = f'({self.telefone[:2]}) {self.telefone[2:6]}-{self.telefone[6:]}'
        representacao = '\nNome: ' + self.nome + '\nEndereço: ' + self.endereco + '\nTelefone: ' + telefone_formatado + '\nCidade: ' + self.cidade + '\nEstado: ' + self.estado
        return representacao
    
class CadastroLaboratorio:
        
    def cadastrar_novo(self) -> None:

        nome = input("Digite o nome do laboratório: ")
        endereco = input("Digite o endereço: ")

        telefone = input("Digite o telefone: ")
        while len(telefone) != LEN_TELEFONE:
            print('O telefone deve conter 10 dígitos, sem pontuação.')
            telefone = input("Digite o telefone: ")

        cidade = input("Digite o Município: ")

        estado = input("Digite o Estado: ")
        while len(estado) != LEN_ESTADO:
            print('A sigla da Unidade da Federação deve ter dois dígitos.')
            estado = input("Digite o Estado: ")

        if nome not in Laboratorio.dic_laboratorios:
            novo_lab = Laboratorio(nome, endereco, telefone, cidade, estado)
            Laboratorio.dic_laboratorios[nome] = novo_lab
        else:
            print('Laboratório já cadastrado.')

        print(f'\n=== Laboratório cadastrado === {novo_lab}')

    def listar_laboratorios(self):

        sorted_dic = sorted(Laboratorio.dic_laboratorios.values(), key=lambda lab:lab.nome)
        for lab in sorted_dic:
            print(lab)
    

