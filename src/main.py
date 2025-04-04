from service.workbook_handlers.workbook_loader import WorkbookLoader

def main():    
    WorkbookLoader().load_or_create_workbook()

if __name__ == "__main__":
    main()