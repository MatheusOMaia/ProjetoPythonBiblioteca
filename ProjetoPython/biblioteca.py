from livro import Livro
from usuario import Usuario
from emprestimo import Emprestimo
from datetime import datetime
import json

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

    # BUSCAR 
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

    # REALIZAR EMPRÉSTIMO
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

    # REMOÇÃO

    def remover_livro(self, id_livro):
        livro = self.buscar_livro(id_livro)

        if not livro:
            print("Livro não encontrado.")
            return
        
        # Verifica se o livro não está sendo emprestado
        if not livro.disponivel:
            print("Não é possível remover um livro emprestado.")
            return
        
        self.livros.remove(livro)
        print("Livro removido com sucesso!")

    def remover_usuario(self, id_usuario):
        usuario = self.buscar_usuario(id_usuario)

        if not usuario:
            print("Usuário não encontrado.")
            return

        # Verifica se o usuário tem empréstimos ativos
        for emp in self.emprestimos:
            if emp.usuario.id == id_usuario and not emp.devolvido:
                print("Usuário possui empréstimos ativos e não pode ser removido.")
                return

        self.usuarios.remove(usuario)
        print("Usuário removido com sucesso!")

        # SALVAR DADOS EM JSON
    def salvar_dados(self):
        dados = {
            "livros": [],
            "usuarios": [],
            "emprestimos": []
        }

        # LIVROS
        for livro in self.livros:
            dados["livros"].append({
                "id": livro.id,
                "titulo": livro.titulo,
                "autor": livro.autor,
                "disponivel": livro.disponivel
            })

        # USUÁRIOS
        for usuario in self.usuarios:
            dados["usuarios"].append({
                "id": usuario.id,
                "nome": usuario.nome,
                "cpf": usuario.cpf
            })

        # EMPRÉSTIMOS
        for emp in self.emprestimos:
            dados["emprestimos"].append({
                "id": emp.id,
                "usuario_id": emp.usuario.id,
                "livro_id": emp.livro.id,
                "data_emprestimo": emp.data_emprestimo.strftime("%Y-%m-%d %H:%M:%S"),
                "data_devolucao": emp.data_devolucao.strftime("%Y-%m-%d %H:%M:%S"),
                "devolvido": emp.devolvido
            })

        with open("dados.json", "w") as f:
            json.dump(dados, f, indent=4)

        print("Dados salvos com sucesso!")
    # CARREGAR DADOS EM JSON
    def carregar_dados(self):
        try:
            with open("dados.json", "r") as f:
                dados = json.load(f)

            # CARREGAR LIVROS
            for l in dados["livros"]:
                livro = Livro(l["id"], l["titulo"], l["autor"])
                livro.disponivel = l["disponivel"]
                self.livros.append(livro)

            # CARREGAR USUARIOS
            for u in dados["usuarios"]:
                usuario = Usuario(u["id"], u["nome"], u["cpf"])
                self.usuarios.append(usuario)

            # CARREGAR EMPRESTIMOS
            for e in dados["emprestimos"]:
                usuario = self.buscar_usuario(e["usuario_id"])
                livro = self.buscar_livro(e["livro_id"])

                emp = Emprestimo(e["id"], usuario, livro, carregando=True)
                emp.data_emprestimo = datetime.strptime(e["data_emprestimo"], "%Y-%m-%d %H:%M:%S")
                emp.data_devolucao = datetime.strptime(e["data_devolucao"], "%Y-%m-%d %H:%M:%S")
                emp.devolvido = e["devolvido"]

                self.emprestimos.append(emp)

            # ATUALIZAR IDS
            if self.livros:
                self.prox_id_livro = max(l.id for l in self.livros) + 1
            if self.usuarios:
                self.prox_id_usuario = max(u.id for u in self.usuarios) + 1
            if self.emprestimos:
                self.prox_id_emprestimo = max(e.id for e in self.emprestimos) + 1

            print("Dados carregados com sucesso!")

        except FileNotFoundError:
            print("Arquivo de dados não encontrado. Iniciando sistema vazio.")