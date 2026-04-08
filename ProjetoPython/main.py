from biblioteca import Biblioteca
import os

def menu():
    biblioteca = Biblioteca()
    biblioteca.carregar_dados()

    while True:
        print("\n===== SISTEMA DE BIBLIOTECA =====")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Listar Livros")
        print("4. Listar Usuários")
        print("5. Realizar Empréstimo")
        print("6. Devolver Livro")
        print("7. Listar Empréstimos")
        print("8. Remover Livro")
        print("9. Remover Usuário")
        print("0. Sair e Salvar")

        opcao = input("Escolha uma opção: ")
        os.system("cls")

        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor: ")
            biblioteca.cadastrar_livro(titulo, autor)

        elif opcao == "2":
            nome = input("Nome do usuário: ")
            cpf = input("Cpf: ")
            biblioteca.cadastrar_usuario(nome, cpf)

        elif opcao == "3":
            biblioteca.listar_livros()

        elif opcao == "4":
            biblioteca.listar_usuarios()

        elif opcao == "5":
            try:
                id_usuario = int(input("ID do usuário: "))
                id_livro = int(input("ID do livro: "))
                biblioteca.realizar_emprestimo(id_usuario, id_livro)
            except ValueError:
                print("Entrada inválida! Digite números.")

        elif opcao == "6":
            try:
                id_emprestimo = int(input("ID do empréstimo: "))
                biblioteca.devolver_livro(id_emprestimo)
            except ValueError:
                print("Entrada inválida!")

        elif opcao == "7":
            biblioteca.listar_emprestimos()

        elif opcao == "8":
            try:
                id_livro = int(input("ID do livro a remover: "))
                biblioteca.remover_livro(id_livro)
            except ValueError:
                print("Entrada inválida!")

        elif opcao == "0":
            biblioteca.salvar_dados()
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")
        input("\nPressione ENTER para continuar...")
        os.system("cls")

if __name__ == "__main__":
    menu()