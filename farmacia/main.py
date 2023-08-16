from farmacia import Farmacia
from vendas import Venda 
def exibir_menu():
    print("1. Cadastrar Cliente")
    print("2. Consultar Cliente")
    print("3. Alterar Cadastro")
    print("4. Cadastrar Medicamento Quimioterápico")
    print("5. Cadastrar Medicamento Fitoterápico")
    print("6. Buscar Medicamento por Nome")
    print("7. Cadastrar Laboratório")
    print("8. Listar Laboratórios Cadastrados")
    print("9. Efetuar Venda")
    print("10. Emitir Relatórios")
    print("11. Sair")

def main():
    farmacia = Farmacia()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
         
        if opcao == "1":
            farmacia.clientes.cadastrar_novo()
        elif opcao == "2":
            cpf = input("Digite o CPF do cliente: ")  
            farmacia.clientes.visualizar_cadastro(cpf)
        elif opcao == "3":
            cpf = input("Digite o CPF do cliente: ")
            farmacia.clientes.alterar_cadastro(cpf)
        elif opcao == "4":
            farmacia.medicamentos.cadastrar_medicamento(farmacia.laboratorios,'quimioterapico')
        elif opcao == "5":
            farmacia.medicamentos.cadastrar_medicamento(farmacia.laboratorios,'fitoterapico')
        elif opcao == "6":
            nome_medicamento = input("Digite o nome do medicamento: ")
            medicamento = farmacia.medicamentos.buscar_medicamento_por_nome(nome_medicamento)
            if medicamento:
                print(medicamento)
            else:
                print("Medicamento não encontrado.")
        elif opcao == "7":
            farmacia.laboratorios.cadastrar_laboratorio()
        elif opcao == "8":
            farmacia.laboratorios.listar_laboratorios()           
        elif opcao == "9":
            cpf_cliente = input("Digite o CPF do cliente: ")
            nome_medicamento = input("Digite o nome do medicamento: ")
            data_hora = input("Digite a data e hora da venda: ")
            venda = Venda(data_hora, [], None, 0)  # Os valores serão atualizados no método efetuar_venda
            venda.efetuar_venda(farmacia, cpf_cliente, nome_medicamento, data_hora)
                        
            venda.imprimir_venda()

        elif opcao == "10":
            farmacia.emitir_relatorio()
        elif opcao == "11":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    main()