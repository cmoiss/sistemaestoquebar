from IPython.display import display
from service.data_frame_factory import DataFrameFactory, DataFrame

def main():
    dataframes: list = DataFrameFactory().setup_dataframes()
    display(dataframes[0])
    display(dataframes[1])

if __name__ == "__main__":
    main()