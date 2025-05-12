import banco

def menu():
    while True:
        print("\n--- Cadastro de Clientes ---")
        print("1. Adicionar cliente")
        print("2. Listar todos os clientes")
        print("3. Buscar cliente por nome")
        print("4. Deletar cliente")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            banco.inserir_cliente(nome, email, telefone)
            print("Cliente cadastrado com sucesso!")

        elif opcao == "2":
            clientes = banco.listar_clientes()
            for c in clientes:
                print(f"{c[0]} - {c[1]} - {c[2]} - {c[3]}")

        elif opcao == "3":
            nome = input("Digite o nome para busca: ")
            resultados = banco.buscar_cliente(nome)
            for r in resultados:
                print(f"{r[0]} - {r[1]} - {r[2]} - {r[3]}")
            if not resultados:
                print("Nenhum cliente encontrado.")

        elif opcao == "4":
            id_cliente = input("Digite o ID do cliente a ser deletado: ")
            banco.deletar_cliente(id_cliente)
            print("Cliente deletado com sucesso!")

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

# Criar tabela se não existir e iniciar menu
if __name__ == "__main__":
    banco.criar_tabela()
    menu()
