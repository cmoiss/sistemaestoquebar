from pandas import DataFrame
import pandas as pd

from model.category import Categoria
from model.product import Produto

class DataFrameFactory:
    def __init__(self):
        pass

    def _create_generic_dataframe(self, *columns) -> DataFrame:
        return DataFrame(columns=columns)

    def create_dataframe_categorias(self) -> DataFrame:
        atributes = list(vars(Categoria(None)).keys())
        return self._create_generic_dataframe(*atributes)
    
    def create_dataframe_produtos(self) -> DataFrame:
        atributes = list(vars(Produto(None, None)).keys())
        return self._create_generic_dataframe(*atributes)    
    
