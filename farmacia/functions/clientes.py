class Cliente:
    lista_clientes = {}
    quant_clientes = 0

    def __init__(self, nome: str, data_nasc: str, cpf: str, email: str) -> None:
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.email = email
        Cliente.lista_clientes[self.cpf] = {"Nome": self.nome, "Data_nasc": self.data_nasc, "Email": self.email}
        Cliente.quant_clientes += 1

    def __repr__(self) -> str:
        exibir = f'Nome: {self.nome} \nData_nasc: {self.data_nasc} \nCPF: {self.cpf} \nE-mail: {self.email}'
        return exibir

    def cadastrar(nome, data_nasc, cpf, email):

        if cpf not in Cliente.lista_clientes:
            Cliente.lista_clientes[cpf] = {"Nome": nome, "Data_nasc": data_nasc, "Email": email}
            Cliente.quant_clientes += 1
        else:
            raise ValueError('CPF já cadastrado')

    def listar():
        lista_ordenada = dict(sorted(Cliente.lista_clientes.items(), key=lambda item: item[0][0], reverse=True))
        return lista_ordenada

    def buscar(cpf):
        if cpf in Cliente.lista_clientes:
            return Cliente.lista_clientes[cpf]
        else:
            raise ValueError('CPF não cadastrado')

