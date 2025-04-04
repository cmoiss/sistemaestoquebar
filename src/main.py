from service.workbook_handlers.workbook_loader import WorkbookLoader

def main():    
    loader = WorkbookLoader()
    workbook, current_path = loader.load_or_create_workbook()

    while True:
        pass
    

if __name__ == "__main__":
    main()