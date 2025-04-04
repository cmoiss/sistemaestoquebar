import os

class WorkbookFileNameHandler:
    def __init__(self):
        pass

    def generate_new_filename(self, file_path: str) -> str:
        """Gera um novo nome de arquivo com sufixo numérico"""
        base, ext = os.path.splitext(file_path)
        counter = 1
        
        while True:
            new_path = f"{base} ({counter}){ext}"
            if not os.path.exists(new_path):
                return new_path
            counter += 1