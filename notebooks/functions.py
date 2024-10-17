import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def name_columns(df):
    df.columns = df.columns.str.strip().str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    return df


def remove_last_digits(df, col_name, num_digits):
    """
    Elimina los últimos 'num_digits' de la columna especificada.
    
    Args:
    df (DataFrame): El DataFrame que contiene la columna.
    col_name (str): El nombre de la columna a modificar.
    num_digits (int): El número de dígitos a eliminar del final.
    
    Returns:
    DataFrame: El DataFrame con la columna modificada.
    """
    df[col_name] = df[col_name].astype(str).str[:-num_digits]
    return df


def multiply_column(df, col_name, factor=12):
    """
    Multiplica los elementos de la columna especificada por un factor.
    
    Args:
    df (DataFrame): El DataFrame que contiene la columna.
    col_name (str): El nombre de la columna a modificar.
    factor (int): El número por el cual multiplicar. Por defecto es 12.
    
    Returns:
    DataFrame: El DataFrame con la columna modificada.
    """
    df[col_name] = df[col_name] * factor
    return df


def replace_approval_status(df, col_name):
    """
    Reemplaza los elementos 'Y' por 'Approved' y 'N' por 'Rejected' en la columna especificada.
    
    Args:
    df (DataFrame): El DataFrame que contiene la columna a modificar.
    col_name (str): El nombre de la columna en la que se realizarán los reemplazos.
    
    Returns:
    DataFrame: El DataFrame con los elementos de la columna modificados.
    """
    df[col_name] = df[col_name].replace({'Y': 'Approved', 'N': 'Rejected'})
    return df


def rename_columns(df):
    """
    Cambia el nombre de las columnas del DataFrame a un conjunto específico de nombres.
    
    Args:
    df (DataFrame): El DataFrame que contiene las columnas a renombrar.
    
    Returns:
    DataFrame: El DataFrame con los nombres de las columnas modificados.
    """
    new_column_names = [
        'gender', 
        'married', 
        'dependents', 
        'education', 
        'self_employed', 
        'income', 
        'loan_amount', 
        'loan_status'
    ]
    
    # Asignar los nuevos nombres de columnas
    df.columns = new_column_names
    return df

def strip_all_columns(df):
    """
    Quita los espacios en blanco al principio y al final de todos los elementos en el DataFrame.
    
    Args:
    df (DataFrame): El DataFrame en el que se eliminarán los espacios.
    
    Returns:
    DataFrame: El DataFrame con los espacios eliminados de todas las columnas.
    """
    return df.applymap(lambda x: x.strip() if isinstance(x, str) else x)


def remove_plus_sign(df, col_name):
    """
    Quita el símbolo '+' de los elementos en la columna especificada.
    
    Args:
    df (DataFrame): El DataFrame que contiene la columna a modificar.
    col_name (str): El nombre de la columna en la que se realizará la modificación.
    
    Returns:
    DataFrame: El DataFrame con el símbolo '+' eliminado de la columna.
    """
    df[col_name] = df[col_name].astype(str).str.replace('+', '', regex=False)
    return df


def convert_columns_to_float(df, col1, col2):
    """
    Convierte las columnas especificadas a tipo float.
    
    Args:
    df (DataFrame): El DataFrame que contiene las columnas a modificar.
    col1 (str): El nombre de la primera columna a convertir.
    col2 (str): El nombre de la segunda columna a convertir.
    
    Returns:
    DataFrame: El DataFrame con las columnas convertidas a float.
    """
    df[col1] = df[col1].astype(float)
    df[col2] = df[col2].astype(float)
    return df
