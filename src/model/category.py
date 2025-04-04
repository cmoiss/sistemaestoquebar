class Categoria:
    def __init__(self, nome: str):
        self.nome = nome
        
    def get_table_name(self):
       return "categorias"
   
    def get_fields(self) -> list[str]:
        return ["nome"]
