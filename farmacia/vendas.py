from clientes import Cliente

class Venda:
    def __init__(self, data_hora: str, produtos_vendidos: list, cliente: Cliente, valor_total: float) -> None:
        self.data_hora = data_hora
        self.produtos_vendidos = produtos_vendidos
        self.cliente = cliente
        self.valor_total = valor_total

    def efetuar_venda(self, farmacia, cpf_cliente, nome_medicamento, data_hora):
        cliente = farmacia.clientes.buscar_cliente_por_cpf(cpf_cliente)
        if cliente:
            medicamento = farmacia.medicamentos.buscar_medicamento_por_nome(nome_medicamento)
            if medicamento:
                produtos_venda = [medicamento]
                valor_total = medicamento.preco
                self.cliente = cliente  # Definir o cliente da venda
                self.produtos_vendidos = produtos_venda
                self.valor_total = valor_total
                self.data_hora = data_hora
                farmacia.vendas.append(self)  # Adicionar a venda à lista de vendas
                print("Venda efetuada com sucesso!")
            else:
                print("Medicamento não cadastrado.")
        else:
            print("Cliente não encontrado.")

    def imprimir_venda(self):
        print("Data e Hora da Venda:", self.data_hora)
        print("Produtos Vendidos:")
        for produto in self.produtos_vendidos:
            print("Nome:", produto.nome)
            print("Composto:", produto.comp_principal) 
            
        if self.cliente is not None:
            print("Cliente:")
            print("Nome:", self.cliente.nome)
            print("CPF:", self.cliente.cpf)
        else:
            print("Cliente não encontrado.")
        print("Valor Total:", self.valor_total)