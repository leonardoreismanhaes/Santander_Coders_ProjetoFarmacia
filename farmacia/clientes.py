class Cliente:

    def __init__(self, nome: str, email:str, cpf: str) -> None:
        self.nome = nome
        self.email = email
        self.cpf = cpf

    def __repr__(self) -> str:
        representacao = 'Nome: ' + self.nome
        representacao += '\nE-mail: ' + self.email
        representacao += '\nCPF: ' + self.cpf
        return representacao