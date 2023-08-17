class Laboratorio:

    dic_laboratorios = {}

    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str) -> None:

        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado

    def __repr__(self) -> str:

        representacao = '\nNome: ' + self.nome
        representacao += '\nEndereço: ' + self.endereco
        representacao += '\nTelefone: ' + self.telefone
        representacao += '\nCidade: ' + self.cidade
        representacao += '\nEstado: ' + self.estado
        return representacao
    
class CadastroLaboratorio:
        
    def cadastrar_novo(self) -> None:

        nome = input("Digite o nome do laboratório: ")
        endereco = input("Digite o endereço: ")
        telefone = input("Digite o telefone: ")
        cidade = input("Digite o Município: ")
        estado = input("Digite o Estado: ")

        novo_lab = Laboratorio(nome, endereco, telefone, cidade, estado)
        Laboratorio.dic_laboratorios[nome] = novo_lab

    def listar_laboratorios(self):

        sorted_dic = sorted(Laboratorio.dic_laboratorios.items(), key=lambda x:x[0])
        for cadastro in sorted_dic:
            print(cadastro)
    

