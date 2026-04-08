class Usuario:
    def __init__(self, id, nome, cpf):
        self.id = id
        self.nome = nome
        self.cpf = cpf

    def exibir_info(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Cpf: {self.cpf}")
        print("-" * 30)
