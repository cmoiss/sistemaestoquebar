from src.model.category import Categoria

class Produto:
    def __init__(self, nome: str, categoria: Categoria):
        self.nome = nome
        self.categoria = categoria