from laboratorio import Laboratorio
class Medicamento:

    dic_medicamentos = {}

    def __init__(self, nome: str, comp_principal: str, laboratorio: Laboratorio, descricao: str) -> None:
        self.nome: nome
        self.comp_principal = comp_principal
        self.laboratorio = laboratorio
        self.descricao = descricao

    def __repr__(self) -> str:
        representacao = 'Nome: ' + self.nome
        representacao += '\nPrincípio ativo: ' + self.comp_principal
        representacao += '\nLaboratório: ' + self.laboratorio.nome
        representacao += '\nDescrição: ' + self.descricao
        return representacao
class Fitoterapicos(Medicamento):

    def __init__(self, nome, comp_principal, laboratorio, descricao):
        super().__init__(nome, comp_principal, laboratorio, descricao)

class Quimioterapicos(Medicamento):

    def __init__(self, nome, comp_principal, laboratorio, descricao, receita):
        super().__init__(nome, comp_principal, laboratorio, descricao)
        self.receita = receita

class CadastroMedicamento:
        
    def cadastrar_novo(self) -> None:
        nome = input("Digite o nome do medicamento: ")
        comp_principal = input('Digite o princípio ativo do medicamento: ')
        laboratorio = input('Digite o nome do laboratório: ') 
        # if (laboratorio not in Laboratorio)
        descricao = input('Digite a descrição do medicamento: ') 
        receita = input('O medicamento precisa de receita (S/s/N/n): ').lower
        while receita not in ['s', 'S', 'n', 'N']:
            print('Digite um valor válido')
            receita = input('O medicamento precisa de receita (S/s/N/n): ').lower
        if (receita in ['s', 'S']):
            novo_medicamento = Quimioterapicos(nome, comp_principal, laboratorio, descricao, receita)
            Medicamento.dic_medicamentos[nome] = novo_medicamento
        else:
            novo_medicamento = Fitoterapicos(nome, comp_principal, laboratorio, descricao)
            Medicamento.dic_medicamentos[nome] = novo_medicamento

    def listar_medicamentos(self):
        return sorted(Medicamento.dic_medicamentos.items())

    def listar_fitoterapicos(self):
        for med in Medicamento.dic_medicamentos:
            if (isinstance(med, Fitoterapicos)):
                print(med)
            
    def listar_quimioterapicos(self):
        for med in Medicamento.dic_medicamentos:
            if (isinstance(med, Quimioterapicos)):
                print(med)

    def buscar_medicamento_nome(self, med):
        for med in Medicamento.dic_medicamentos:
            if (med == Medicamento.dic_medicamentos.nome):
                print(med)
    
    def buscar_medicamento_laboratorio(self, lab):
        for lab in Medicamento.dic_medicamentos.values():
            # if (lab == Medicamento.dic_medicamentos):
            print(lab)

    def buscar_medicamento_descricao(self, desc):
        for desc in Medicamento.dic_medicamentos.values():
            # if (desc == Medicamento.dic_medicamentos):
            print(desc)