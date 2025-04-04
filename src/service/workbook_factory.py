from openpyxl import Workbook

from model.product import Produto
from model.category import Categoria

class WorkbookFactory:
    def __init__(self):
        pass

    def _create_generic_sheet(self, book: Workbook, sheet_name: str, model):
        book.create_sheet(sheet_name)
        
        selected_sheet = book[sheet_name]

        # Gera cabeçalho
        atribute_list = list(vars(model).keys())
        selected_sheet.append([*atribute_list])
    
    def _create_sheet_produtos(self, book):
        produto = Produto(None, None)
        self._create_generic_sheet(book, produto.table_name, produto)      
        
    def _create_sheet_categorias(self, book):
        categoria = Categoria(None)
        self._create_generic_sheet(book, categoria.table_name, categoria)
    
    def setup_new_workbook(self):
        book = Workbook()
        book.remove(book["Sheet"])
        self._create_sheet_produtos(book)
        self._create_sheet_categorias(book)
        book.save("data/ControleEstoque.xlsx")