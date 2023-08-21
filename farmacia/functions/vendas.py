class Venda:
    lista_vendas = {}
    n_vendas = 0

    def __int__(self, data: str, hora: str, produto: list, valor: float):
        self.data = data
        self.hora = hora
        self.produto = produto
        self.valor = valor

    def registrar(cliente, data, hora, produto, valor):
        Venda.n_vendas += 1
        Venda.lista_vendas[Venda.n_vendas] = {"cliente": cliente, "data": data, "hora": hora,
                                              "produto": produto, "valor": valor}


    def listar():
        lista_ordenada = dict(sorted(Venda.lista_vendas.items(), key=lambda item: item[0], reverse=False))
        return lista_ordenada
