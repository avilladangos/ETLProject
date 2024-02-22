"""
Este script contiene una función para realizar un proceso de ETL (Extract, Transform, Load).

Funciones:
- etl_process: Realiza un proceso de ETL sobre los datos de entrada.
"""
import pandas as pd
import numpy as np
# import pyspark

# ETL function
def etl_process(input_data: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza un proceso de ETL (Extract, Transform, Load) sobre los datos de entrada.

    Parameters:
    - input_data (pd.DataFrame): Los datos de entrada como un DataFrame de Pandas.

    Returns:
    - pd.DataFrame: Los datos procesados como un DataFrame de Pandas.
    """
    # Dummy ETL process
    processed_data = input_data * 2
    return processed_data
