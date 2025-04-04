class DataFrameFactory:
    def __init__(self):
        pass

    def _create_generic_dataframe(self, *columns) -> DataFrame:
        return DataFrame(columns=columns)

    def create_dataframe_categorias(self) -> DataFrame:
        dataframe_categorias = DataFrame(columns=["nome"])
        return dataframe_categorias
    
    
