from openpyxl import Workbook


class SheetFactory:
    def __init__(self):
        pass
    
    def create_sheet_for_model(self, workbook: Workbook, model):
        """Cria uma sheet para um modelo específico"""
        sheet_name = model.get_table_name()
        workbook.create_sheet(sheet_name)
        sheet = workbook[sheet_name]
        
        # Obtém os atributos do modelo
        attributes = model.get_fields()
        sheet.append(attributes)