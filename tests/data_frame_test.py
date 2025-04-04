from pandas import DataFrame
from src.service.data_frame_factory import DataFrameFactory
# from IPython.display import display

def test_create_dataframe_categoria():
    expected_columns = ["nome"]
    expected_dataframe = DataFrame(columns=expected_columns)

    generated_df: DataFrame = DataFrameFactory().create_dataframe_categorias()

    # display(expected_dataframe)
    
    assert expected_dataframe.equals(generated_df)
    assert generated_df.empty

def test_create_dataframe_produtos():
    expected_columns = ["nome", "categoria"]
    expected_dataframe = DataFrame(columns=expected_columns)

    generated_df: DataFrame = DataFrameFactory().create_dataframe_produtos()

    # display(expected_dataframe)
    
    assert expected_dataframe.equals(generated_df)
    assert generated_df.empty
    