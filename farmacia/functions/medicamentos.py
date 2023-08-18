from functions.laboratorios import Laboratorio


class Medicamentos:
    lista_medicamentos = {}
    quant_medicamentos = 0

    def __int__(self, nome: str, composto: str, laboratorio: Laboratorio, descricao: str) -> None:
        self.nome = nome
        self.composto = composto
        self.laboratorio = laboratorio
        self.descricao = descricao

    def __repr__(self):
        exibir = (f'Nome: {self.nome} \nPrincipal composto: {self.composto} '
                  f'\nLaboratorio: {self.laboratorio} \nDescricao: {self.descricao}')
        return exibir


class Fitoterapicos(Medicamentos):
    lista_medicamentos = {}
    quant_medicamentos = 0

    def __int__(self, nome: str, composto: str, laboratorio: str, descricao: str):
        super.__init__(nome, composto, laboratorio, descricao)

    def cadastrar(nome, composto, laboratorio, descricao):

        if nome not in Fitoterapicos.lista_medicamentos:
            Fitoterapicos.lista_medicamentos[nome] = {"composto": composto, "laboratorio": laboratorio,
                                                      "descricao": descricao}
            Fitoterapicos.quant_medicamentos += 1
        else:
            raise ValueError('Laboratorio já cadastrado')

    def listar():
        lista_ordenada = dict(sorted(Fitoterapicos.lista_medicamentos.items(), key=lambda item: item[0], reverse=True))
        return lista_ordenada

    def buscar(nome):
        if nome in Fitoterapicos.lista_medicamentos:
            return Fitoterapicos.lista_medicamentos[nome]
        else:
            raise ValueError('Laboratorio não cadastrado')


class Quimioterapicos(Medicamentos):
    lista_medicamentos = {}
    quant_medicamentos = 0

    def __int__(self, nome: str, composto: str, laboratorio: str, descricao: str, receita: str):
        super.__init__(nome, composto, laboratorio, descricao)
        self.receita = receita

    def __repr__(self):
        exibir = (f'Nome: {self.nome} \nPrincipal composto: {self.composto} '
                  f'\nLaboratorio: {self.laboratorio} \nDescricao: {self.descricao}'
                  f'\nPrecisa receita: {self.receita}')
        return exibir

    def cadastrar(nome, composto, laboratorio, descricao, receita):

        if nome not in Quimioterapicos.lista_medicamentos:
            Quimioterapicos.lista_medicamentos[nome] = {"composto": composto, "laboratorio": laboratorio,
                                                        "descricao": descricao, "receita": receita}
            Quimioterapicos.quant_medicamentos += 1
        else:
            raise ValueError('Laboratorio já cadastrado')

    def listar():
        lista_ordenada = dict(
            sorted(Quimioterapicos.lista_medicamentos.items(), key=lambda item: item[0], reverse=True))
        return lista_ordenada

    def buscar(nome):
        if nome in Quimioterapicos.lista_medicamentos:
            return Quimioterapicos.lista_medicamentos[nome]
        else:
            raise ValueError('Laboratorio não cadastrado')
