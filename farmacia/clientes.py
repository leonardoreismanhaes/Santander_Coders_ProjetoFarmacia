class Cliente:

    def __init__(self, cpf: str, nome: str, email:str) -> None:
        self.cpf = cpf
        self.nome = nome
        self.email = email

    def __repr__(self) -> str:
        representacao = 'Nome: ' + self.nome
        representacao += '\nCPF: ' + self.cpf
        representacao += '\nE-mail: ' + self.email
        return representacao