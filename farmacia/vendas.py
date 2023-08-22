import datetime
from clientes import *
from medicamentos import *
from laboratorio import *

IDADE_DESCONTO = 65 # idade a partir da qual aplica percentual de desconto na venda
PERCENTUAL_DESCONTO_IDADE = 0.2 # percentual de desconto a aplicar para clientes > 65 anos de idade
VALOR_DESCONTO = 150 # valor total da compra a partir da qual aplica percentual de desconto na venda
PERCENTUAL_DESCONTO_VALOR = 0.1 # percentual de desconto a aplicar para vendas com valor total > R$ 150
LEN_CPF = 11 # tamanho do campo CPF

class ProdutosVendidos:

    def __init__(self, medicamento: Medicamento, quantidade: int, valor_un: float):
        self.medicamento = medicamento
        self.quantidade = quantidade
        self.valor_un = valor_un

    def __repr__(self) -> str:
        representacao = '\nMedicamento: ' + self.medicamento + '\nQuantidade: ' + str(self.quantidade) + '\nValor unitário R$: ' + str(self.valor_un)
        return representacao

class Vendas:

    dict_venda = {}

    def __init__(self, data: str, hora: str, produtos_vendidos: ProdutosVendidos, cliente: Cliente, valor_total: float) -> None:
        self.data = data
        self.hora = hora
        self.produtos_vendidos = produtos_vendidos
        self.cliente = cliente
        self.valor_total = valor_total

    def __repr__(self) -> str:
        pass

class CadastroVenda:

    qt_vendas = 0 # quantidade de vendas realizadas no dia  
    qt_med_quimio = 0 # quantidade de medicamentos quimioterápicos vendidos no dia 
    valor_total_med_quimio = 0 # valor total dos medicamentos quimioterápicos vendidos no dia 
    qt_med_fito = 0 # quantidade de medicamentos fitoterápicos vendidos no dia 
    valor_total_med_fito = 0 # valor total dos medicamentos fitoterápicos vendidos no dia 
    valor_total = 0
    carrinho_produtos = {}

    def __init__(self):
        pass

    def desconto_idade():
        pass

    def desconto_valor():
        pass

    def verificar_receita():
        pass

    def cadastrar_venda(self) -> None:

        CadastroVenda.qt_vendas += 1

        data_hora = datetime.datetime.now()
        data = data_hora.date()
        hora = data_hora.time()

        cpf = input('Digite o CPF do cliente (apenas dígitos): ')
        while len(cpf) != LEN_CPF:
            print('O CPF deve conter 11 dígitos.')
            cpf = input('Digite o CPF do cliente (apenas dígitos): ')
            while cpf not in Cliente.dic_clientes:
                print('CPF não localizado.')
                cpf = input('Digite o CPF do cliente (apenas dígitos): ')
        else:
            cliente = Cliente.dic_clientes[cpf].cpf

        nome_med = input('Digite o nome do medicamento: ')
        while nome_med not in Medicamento.dic_medicamentos:
            print("Medicamento não localizado.")
            nome_med = input('Digite o nome do medicamento: ')
        else:
            medicamento = Medicamento.dic_medicamentos[nome_med].nome

            CadastroVenda.valor_total_med_fito = 0

        quantidade = int(input('Digite a quantidade de unidades vendidas: '))
        valor_un  = float(input('Digite o valor unitário do medicamento: R$ '))

        valor_total = quantidade * valor_un
        novo_produto_vendido = ProdutosVendidos(medicamento, quantidade, valor_un)

        if (isinstance(Medicamento.dic_medicamentos[nome_med], Fitoterapicos)):
            CadastroVenda.qt_med_fito += quantidade # quantidade de medicamentos fitoterápicos vendidos no dia 
            CadastroVenda.valor_total_med_fito += valor_total # valor total dos medicamentos fitoterápicos vendidos no dia 
        if (isinstance(Medicamento.dic_medicamentos[nome_med], Quimioterapicos)):
            CadastroVenda.qt_med_quimio += quantidade # quantidade de medicamentos fitoterápicos vendidos no dia 
            CadastroVenda.valor_total_med_quimio += valor_total # valor total dos medicamentos fitoterápicos vendidos no dia 

        if CadastroVenda.carrinho_produtos == {}:
            CadastroVenda.carrinho_produtos[cpf] += novo_produto_vendido
        else:
            CadastroVenda.carrinho_produtos[cpf] = novo_produto_vendido

        print(data, hora, cliente, novo_produto_vendido)
        print('Quantidade de vendas: ', CadastroVenda.qt_vendas)
        print(CadastroVenda.carrinho_produtos)

        # nova_venda = Vendas(data, hora, produtos_vendidos, cliente, valor_total)
        #     Vendas.dict_venda[cliente] = nova_venda
        
        
    def relatorio_vendas(self):
        pass