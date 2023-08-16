

class Laboratorio:

    def __int__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado

    def __repr__(self):
        exibir = (f'Nome: {self.nome} \nEndereco: {self.endereco} '
                  f'\nTelefone: {self.telefone} \nCidade: {self.cidade}'
                  f'\nEstado: {self.estado}')
        return exibir
