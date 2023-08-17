from laboratorios import Laboratorio


class Medicamentos:

    def __int__(self, nome: str, composto: str, laboratorio: Laboratorio, descricao: str) -> None:
        self.nome = nome
        self.composto = composto
        self.laboratorio = laboratorio
        self.descricao = descricao

    def __repr__(self):
        exibir = (f'Nome: {self.nome} \nPrincipal composto: {self.composto} '
                  f'\nLaboratorio: {self.laboratorio} \nDescricao: {self.descricao}')
        return exibir


class Quimioterapicos(Medicamentos):

    def __int__(self, nome: str, composto: str, laboratorio: str, descricao: str, receita: str):
        super.__init__(nome, composto, laboratorio, descricao)
        self.receita = receita

    def __repr__(self):
        exibir = (f'Nome: {self.nome} \nPrincipal composto: {self.composto} '
                  f'\nLaboratorio: {self.laboratorio} \nDescricao: {self.descricao}'
                  f'\nPrecisa receita: {self.receita}')
        return exibir


class Fitoterapicos(Medicamentos):

    def __int__(self, nome: str, composto: str, laboratorio: str, descricao: str):
        super.__init__(nome, composto, laboratorio, descricao)
