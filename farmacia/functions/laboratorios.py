

class Laboratorio:
    lista_laboratorios = {}
    quant_laboratorios = 0

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

    def cadastrar(nome, endereco, telefone, cidade, estado):

        if nome not in Laboratorio.lista_laboratorios:
            Laboratorio.lista_laboratorios[nome] = {"Endereco": endereco, "Telefone": telefone,
                                                    "Cidade": cidade, "Estado": estado}
            Laboratorio.quant_laboratorios += 1
        else:
            raise ValueError('Laboratorio já cadastrado')

    def listar():
        lista_ordenada = dict(sorted(Laboratorio.lista_laboratorios.items(), key=lambda item: item[0], reverse=False))
        return lista_ordenada

    def buscar(nome):
        if nome in Laboratorio.lista_laboratorios:
            return Laboratorio.lista_laboratorios[nome]
        else:
            raise ValueError('Laboratorio não cadastrado')

