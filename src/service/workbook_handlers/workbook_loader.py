import os
from service.workbook_handlers.sheet_factory import SheetFactory
from service.workbook_handlers.workbook_factory import WorkbookFactory
from service.workbook_handlers.workbook_filename import WorkbookFileNameHandler

from openpyxl import load_workbook, Workbook
from openpyxl.worksheet.worksheet import Worksheet
from model.product import Produto
from model.category import Categoria
from service.workbook_handlers.workbook_validator import WorkbookValidator


class WorkbookLoader:
    def __init__(
        self, 
        file_path: str = "data/ControleEstoque.xlsx", 
        wb_validator: WorkbookValidator = WorkbookValidator(),
        wb_factory: WorkbookFactory = WorkbookFactory(),
        wb_filename: WorkbookFileNameHandler = WorkbookFileNameHandler()
    ):
        self._file_path = file_path
        self._models = [
            Produto(None, None), 
            Categoria(None)
        ]
        
        # Dependências
        self._wb_validator = wb_validator
        self._wb_factory = wb_factory
        self._wb_filename = wb_filename
    
    def load_or_create_workbook(self) -> tuple[Workbook, str]:
        """
        Carrega o workbook existente ou cria um novo.
        Retorna uma tupla com (workbook, caminho_do_arquivo)
        """
        try:
            workbook = load_workbook(self._file_path)

            is_valid, validation_msg = self._wb_validator.validate_workbook_structure(models=self._models, workbook=workbook)
            
            if not is_valid:
                new_path = self._wb_filename.generate_new_filename(self._file_path)
                workbook = self._wb_factory.create_new_workbook(self._models, SheetFactory() , new_path)
                self._file_path = new_path

                print("\nNovo workbook criado devido a estrutura original ter sido modificada")
                print(f"Novo caminho do workbook: {new_path}\n")

                return workbook, new_path
            
            print("\nWorkbook carregado com sucesso!\n")

            return workbook, self._file_path
        except FileNotFoundError:
            workbook = self._wb_factory.create_new_workbook(self._models, SheetFactory())

            print("\nNovo workbook criado!\n")

            return workbook, self._file_path  
    