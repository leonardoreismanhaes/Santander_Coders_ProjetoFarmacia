from laboratorio import Laboratorio
class Medicamento:

    dic_medicamentos = {}

    def __init__(self, nome: str, comp_principal: str, laboratorio: Laboratorio, descricao: str) -> None:
        self.nome = nome
        self.comp_principal = comp_principal
        self.laboratorio = laboratorio
        self.descricao = descricao

    def __repr__(self) -> str:
        representacao = '\nNome: ' + self.nome + '\nPrincípio ativo: ' + self.comp_principal + '\nLaboratório: ' + self.laboratorio + '\nDescrição: ' + self.descricao
        return representacao
class Fitoterapicos(Medicamento):

    def __init__(self, nome, comp_principal, laboratorio, descricao):
        super().__init__(nome, comp_principal, laboratorio, descricao)

class Quimioterapicos(Medicamento):

    def __init__(self, nome, comp_principal, laboratorio, descricao, receita):
        super().__init__(nome, comp_principal, laboratorio, descricao)
        self.receita = receita

class CadastroMedicamento:

    def __init__(self) -> None:
        pass
        
    def cadastrar_novo(self) -> None:
        nome = input("Digite o nome do medicamento: ")
        comp_principal = input('Digite o princípio ativo: ')

        laboratorio = input('Digite o nome do laboratório: ') 
        while (laboratorio not in Laboratorio.dic_laboratorios):
            print("Laboratório não cadastrado.")
            laboratorio = input('Digite o nome do laboratório: ') 

        descricao = input('Digite a descrição: ') 

        receita = input('O medicamento precisa de receita (S/s/N/n): ')
        while receita not in ['s', 'S', 'n', 'N']:
            print('Digite um valor válido.')
            receita = input('O medicamento precisa de receita (S/s/N/n): ')

        if (receita in ['s', 'S']):
            novo_medicamento = Quimioterapicos(nome, comp_principal, laboratorio, descricao, receita)
            Medicamento.dic_medicamentos[nome] = novo_medicamento
        else:
            novo_medicamento = Fitoterapicos(nome, comp_principal, laboratorio, descricao)
            Medicamento.dic_medicamentos[nome] = novo_medicamento

        print(f'\n=== Medicamento cadastrado === {novo_medicamento}')

    def listar_medicamentos(self):
        sorted_dic = sorted(Medicamento.dic_medicamentos.values(), key=lambda med:med.nome)
        for med in sorted_dic:
            print(med)

    def listar_fitoterapicos(self):
        for med in Medicamento.dic_medicamentos.values():
            if (isinstance(med, Fitoterapicos)):
                print(med)
            
    def listar_quimioterapicos(self):
        for med in Medicamento.dic_medicamentos.values():
            if (isinstance(med, Quimioterapicos)):
                print(med)

    def buscar_medicamento_nome(self, nome):
        resultado = []
        for medicamento in Medicamento.dic_medicamentos.values():
            if nome in medicamento.nome:
                resultado.append(medicamento)
        print(resultado)
    
    def buscar_medicamento_laboratorio(self, lab):
        resultado = []
        for medicamento in Medicamento.dic_medicamentos.values():
            if lab in medicamento.laboratorio:
                resultado.append(medicamento)
        print(resultado)

    def buscar_medicamento_descricao(self, desc):
        resultado = []
        for medicamento in Medicamento.dic_medicamentos.values():
            if desc in medicamento.descricao:
                resultado.append(medicamento)
        print(resultado)