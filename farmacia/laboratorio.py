class Laboratorio:

    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str) -> None:
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado

    def __repr__(self) -> str:
        representacao = 'Nome: ' + self.nome
        representacao += '\Endereço: ' + self.endereco
        representacao += '\nTelefone: ' + self.telefone
        representacao += '\nCidade: ' + self.cidade
        representacao += '\nEstado: ' + self.estado
        return representacao

