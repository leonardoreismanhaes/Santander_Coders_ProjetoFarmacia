class CadastroCliente:
    
    def __init__(self) -> None:
        self.cadastrados = {}
        
    def cadastrar_novo(self) -> None:
        nome = input("Digite o nome do cliente: ")
        email = input('Digite o email do cliente: ')
        cpf = input('Digite o CPF do cliente: ')
        
        if cpf not in self.cadastrados:
            novo_cliente = Cliente(nome, email, cpf)
            self.cadastrados[cpf] = novo_cliente
        else:
            raise ValueError('CPF já cadastrado')
            
    def visualizar_cadastro(self, cpf) -> None:
        for cpf in self.cadastrados:
            if cpf == self.cadastrados[cpf]:
                print(self.cadastrados[cpf])
            
    def alterar_cadastro(self, cpf):
        if cpf not in self.cadastrados:
            print('Esse CPF não está cadastrado')
            return
            #raise ValueError('Esse CPF não está cadastrado')
        cliente = self.cadastrados[cpf]
        alteracao = input('O que deseja alterar? ')
        
        while alteracao.lower() not in ('nome', 'email', 'cpf'):
            alteracao = input('Erro. Digite novamente o que quer alterar: ')
        
        if alteracao == 'nome':
            novo_nome = input('Digite o novo nome: ')
            cliente.nome = novo_nome
        
        elif alteracao == 'email':
            novo_email = input('Digite o novo e-mail: ')
            cliente.email = novo_email
            
        elif alteracao == 'cpf':
            novo_cpf = input('Digite o novo CPF: ')
            cliente.cpf = novo_cpf
            self.cadastrados.pop(cpf)
            
        self.cadastrados[cliente.cpf] = cliente
        
    def run(self):
        
        print('Menu\n1 - Novo cadastro\n2 - Visualizar cadastros\n3 - Alterar cadastro\n0 - Sair')
        o_que_fazer = int(input('O que deseja fazer? '))
        
        while o_que_fazer != 0:
            
            if o_que_fazer == 1:
                print('===Novo cadastro===\n')
                self.cadastrar_novo()
                print('\n===Fim do cadastro===')
                
            elif o_que_fazer == 2:
                print('===Visualização dos cadastrados===\n')
                self.visualizar_cadastros()
                print('\n===Fim da visualização===')
            
            elif o_que_fazer == 3:
                print('===Alterar cadastros===\n')
                cpf_a_alterar = input('Digite o CPF a ser alterado: ')
                self.alterar_cadastro(cpf_a_alterar)
                print('\n===Fim da alteração===')
            
            print('Menu\n1 - Novo cadastro\n2 - Visualizar cadastros\n3 - Alterar cadastro\n0 - Sair')
            o_que_fazer = int(input("O que deseja fazer? "))
        
        print('===Fim===')