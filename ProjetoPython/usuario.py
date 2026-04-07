class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def exibir_info(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print("-" * 30)
