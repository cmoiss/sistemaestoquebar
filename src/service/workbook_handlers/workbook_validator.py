from openpyxl import Workbook


class WorkbookValidator:
    def __init__(self):
        pass

    def validate_workbook_structure(self, models: list, workbook: Workbook) -> tuple[bool, str]:
        """
        Valida a estrutura do workbook.
        Retorna (True, "") se válido, (False, motivo) se inválido
        """
        for model in models:
            sheet_name = model.get_table_name()
            
            # Verifica se a sheet existe
            if sheet_name not in workbook.sheetnames:
                return False, f"Sheet '{sheet_name}' não encontrada"
            
            sheet = workbook[sheet_name]
            attributes = list(vars(model).keys())
            
            # Verifica se a sheet tem pelo menos uma linha (cabeçalho)
            if sheet.max_row == 0:
                return False, f"Sheet '{sheet_name}' sem cabeçalho"
            
            # Verifica se os cabeçalhos correspondem aos atributos do modelo
            headers = [str(cell.value).strip() for cell in sheet[1] if cell.value is not None]
            if headers != attributes:
                return False, f"Estrutura inválida na sheet '{sheet_name}'. Esperado: {attributes}, encontrado: {headers}"
        
        return True, ""