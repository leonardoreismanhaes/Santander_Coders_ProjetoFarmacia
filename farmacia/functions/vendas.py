class Venda:
    lista_vendas = {}
    n_vendas = 0

    def __int__(self, data: str, hora: str, produtos: dict, valor: float):
        self.data = data
        self.hora = hora
        self.produtos = produtos
        self.valor = valor

    def registrar(cliente, data, hora, produtos, valor):
        Venda.n_vendas += 1
        Venda.lista_vendas[Venda.n_vendas] = {"cliente": cliente, "data": data, "hora": hora,
                                              "produtos": produtos, "valor": valor}


    def listar():
        lista_ordenada = dict(sorted(Venda.lista_vendas.items(), key=lambda item: item[0], reverse=False))
        return lista_ordenada
