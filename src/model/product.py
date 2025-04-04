from model.category import Categoria

class Produto:
    def __init__(self, nome: str, categoria: Categoria):
        self.nome = nome
        self.categoria = categoria
        
    def get_table_name(self):
        return "produtos"
    
    def get_fields(self) -> list[str]:
        return [
            "nome",
            "categoria"
        ]