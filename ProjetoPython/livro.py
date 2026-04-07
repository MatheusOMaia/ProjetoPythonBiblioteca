class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  
    
    
    def exibir_info(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        print(f"ID: {self.id}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Status: {status}")
        print("-" * 30)
