import pandas as pd
import yfinance as yf

def download_data(ticker):
    # Define el símbolo de la acción que deseas analizar
    symbol = ticker  # Cambia esto por el ticker que desees

    # Cargar los datos históricos desde el 14 de octubre de 2022 hasta hoy
    start_date = '2022-10-14'
    end_date = '2024-10-14'  

    # Descargar datos históricos
    data_ticker = yf.download(symbol, start=start_date, end=end_date)

    # Guardar los datos en un archivo CSV
    data_ticker.to_csv(f"data/{symbol}_historical_data.csv")
    



def type_and_ticker(df, type, ticker):
    df["type"] = type
    df["ticker"] = ticker
    