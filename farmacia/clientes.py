
class Cliente:
    lista_clientes = {}
    quant_clientes = 0

    def __init__(self, nome: str, data_nasc: str, cpf: str, email: str) -> None:
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.email = email
        Cliente.lista_clientes[self.cpf] = {"Nome": self.nome, "Data_nasc": data_nasc, "Email": email}
        Cliente.quant_clientes += 1

    def __repr__(self) -> str:
        exibir = f'Nome: {self.nome} \nData_nasc: {self.data_nasc} \nCPF: {self.cpf} \nE-mail: {self.email}'
        return exibir

    def listar():
        for cliente in Cliente.lista_clientes.items():
            print(cliente)


teste = Cliente('teste1', '22/12/1959', '11111111111', 'teste@t.com')
teste2 = Cliente('teste2', '22/12/1960', '22222222222', 'teste2@t.com')

print(teste)
print(Cliente.listar())
print(Cliente.quant_clientes)
