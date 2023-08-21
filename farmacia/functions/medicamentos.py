from functions.laboratorios import Laboratorio


class Medicamentos:
    lista_medicamentos = {}
    quant_medicamentos = 0

    def __int__(self, nome: str, composto: str, laboratorio: Laboratorio, descricao: str, preco: float) -> None:
        self.nome = nome
        self.composto = composto
        self.laboratorio = laboratorio
        self.descricao = descricao
        self.preco = preco

    def __repr__(self):
        exibir = (f'Nome: {self.nome} \nPrincipal composto: {self.composto} '
                  f'\nLaboratorio: {self.laboratorio} \nDescricao: {self.descricao}'
                  f'\nPreco: {self.preco}')
        return exibir

    def listar():
        lista_ordenada = dict(sorted(Medicamentos.lista_medicamentos.items(), key=lambda item: item[0], reverse=False))
        return lista_ordenada


class Fitoterapicos(Medicamentos):
    lista_medicamentos = {}
    quant_medicamentos = 0

    def __int__(self, nome: str, composto: str, laboratorio: str, descricao: str, preco: float):
        super.__init__(nome, composto, laboratorio, descricao, preco)

    def cadastrar(nome, composto, laboratorio, descricao, preco):

        if nome not in Fitoterapicos.lista_medicamentos:
            Fitoterapicos.lista_medicamentos[nome] = {"composto": composto, "laboratorio": laboratorio,
                                                      "descricao": descricao, "preco": preco}
            Fitoterapicos.quant_medicamentos += 1
            Medicamentos.lista_medicamentos[nome] = {"tipo": 'Fitoterapico', "composto": composto,
                                                     "laboratorio": laboratorio, "descricao": descricao, "preco": preco}
            Medicamentos.quant_medicamentos += 1
        else:
            raise ValueError('Medicamento já cadastrado')

    def listar():
        lista_ordenada = dict(sorted(Fitoterapicos.lista_medicamentos.items(), key=lambda item: item[0], reverse=False))
        return lista_ordenada

    def buscar(nome):
        if nome in Fitoterapicos.lista_medicamentos:
            return Fitoterapicos.lista_medicamentos[nome]
        else:
            raise ValueError('Medicamento não cadastrado')


class Quimioterapicos(Medicamentos):
    lista_medicamentos = {}
    quant_medicamentos = 0

    def __int__(self, nome: str, composto: str, laboratorio: str, descricao: str, receita: str, preco: float):
        super.__init__(nome, composto, laboratorio, descricao, preco)
        self.receita = receita

    def __repr__(self):
        exibir = (f'Nome: {self.nome} \nPrincipal composto: {self.composto} '
                  f'\nLaboratorio: {self.laboratorio} \nDescricao: {self.descricao}'
                  f'\nPrecisa receita: {self.receita} \nPreco: {self.preco}')
        return exibir

    def cadastrar(nome, composto, laboratorio, descricao, receita, preco):

        if nome not in Quimioterapicos.lista_medicamentos:
            Quimioterapicos.lista_medicamentos[nome] = {"composto": composto, "laboratorio": laboratorio,
                                                        "descricao": descricao, "receita": receita, "preco": preco}
            Quimioterapicos.quant_medicamentos += 1
            Medicamentos.lista_medicamentos[nome] = {"tipo": 'Quimioterapico',"composto": composto,
                                                     "laboratorio": laboratorio, "descricao": descricao,
                                                     "receita": receita, "preco": preco}
            Medicamentos.quant_medicamentos += 1
        else:
            raise ValueError('Medicamento já cadastrado')

    def listar():
        lista_ordenada = dict(
            sorted(Quimioterapicos.lista_medicamentos.items(), key=lambda item: item[0], reverse=False))
        return lista_ordenada

    def buscar(nome):
        if nome in Quimioterapicos.lista_medicamentos:
            return Quimioterapicos.lista_medicamentos[nome]
        else:
            raise ValueError('Medicamento não cadastrado')
