from livro import Livro
from usuario import Usuario
from emprestimo import Emprestimo

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

        self.prox_id_livro = 1
        self.prox_id_usuario = 1
        self.prox_id_emprestimo = 1

    # CADASTRAR LIVROS
    def cadastrar_livro(self, titulo, autor):
        livro = Livro(self.prox_id_livro, titulo, autor)
        self.livros.append(livro)
        self.prox_id_livro += 1
        print("Livro cadastrado com sucesso!")

    # CADASTRAR USUARIO
    def cadastrar_usuario(self, nome, email):
        usuario = Usuario(self.prox_id_usuario, nome, email)
        self.usuarios.append(usuario)
        self.prox_id_usuario += 1
        print("Usuário cadastrado com sucesso!")

    # BUSCAR LIVRO
    def buscar_livro(self, id):
        for livro in self.livros:
            if livro.id == id:
                return livro
        return None

    def buscar_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario
        return None

    def buscar_emprestimo(self, id):
        for emp in self.emprestimos:
            if emp.id == id:
                return emp
        return None

    # EMPRÉSTIMO
    def realizar_emprestimo(self, id_usuario, id_livro):
        usuario = self.buscar_usuario(id_usuario)
        livro = self.buscar_livro(id_livro)

        if not usuario:
            print("Usuário não encontrado.")
            return

        if not livro:
            print("Livro não encontrado.")
            return

        try:
            emprestimo = Emprestimo(
                self.prox_id_emprestimo,
                usuario,
                livro
            )
            self.emprestimos.append(emprestimo)
            self.prox_id_emprestimo += 1
            print("Empréstimo realizado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    # DEVOLUÇÃO
    def devolver_livro(self, id_emprestimo):
        emprestimo = self.buscar_emprestimo(id_emprestimo)

        if not emprestimo:
            print("Empréstimo não encontrado.")
            return

        emprestimo.registrar_devolucao()

    # LISTAGENS
    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return

        for livro in self.livros:
            livro.exibir_info()

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return

        for usuario in self.usuarios:
            usuario.exibir_info()

    def listar_emprestimos(self):
        if not self.emprestimos:
            print("Nenhum empréstimo registrado.")
            return

        for emp in self.emprestimos:
            emp.exibir_info()