from datetime import datetime, timedelta

class Emprestimo:
    def __init__(self, id, usuario, livro, dias_para_devolucao=7, carregando=False):
        self.id = id
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = datetime.now()
        self.data_devolucao = self.data_emprestimo + timedelta(days=dias_para_devolucao)
        self.devolvido = False

        # Primeiro vai checar se o empréstimo está sendo carregado do arquivo json ou não, pq quando realiza um emprestimo seta o livro pra
        # indisponivel, mas quando tiver sendo carregado tem que ser igual oq está salvo.
        if not carregando:
            if livro.disponivel:
                livro.disponivel = False
            else:
                raise Exception("Livro já está emprestado!")

    def registrar_devolucao(self):
        if not self.devolvido:
            self.devolvido = True
            self.livro.disponivel = True
            print("Livro devolvido com sucesso!")
        else:
            print("Este empréstimo já foi finalizado.")

    def verificar_atraso(self):
        if not self.devolvido and datetime.now() > self.data_devolucao:
            return True
        return False

    def exibir_info(self):
        status = "Devolvido" if self.devolvido else "Em andamento"
        atraso = "Sim" if self.verificar_atraso() else "Não"

        print(f"ID Empréstimo: {self.id}")
        print(f"Usuário: {self.usuario.nome}")
        print(f"Livro: {self.livro.titulo}")
        print(f"Data Empréstimo: {self.data_emprestimo.strftime('%d/%m/%Y')}")
        print(f"Data Devolução: {self.data_devolucao.strftime('%d/%m/%Y')}")
        print(f"Status: {status}")
        print(f"Atrasado: {atraso}")
        print("-" * 30)