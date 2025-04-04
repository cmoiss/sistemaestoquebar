from src.service.data_frame_factory import DataFrameFactory

def main():
    df = DataFrameFactory()
    
    df.create_dataframe_categorias()
    df.create_dataframe_produtos()

if __name__ == "__main__":
    main()