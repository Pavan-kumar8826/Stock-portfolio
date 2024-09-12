import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = '2W8BX8XOKFWSNL8M'
BASE_URL = 'https://www.alphavantage.co/query'

def get_stock_data(symbol):
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': API_KEY,
        'outputsize': 'full'  # Add this parameter to get full data
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    df = pd.DataFrame(data['Time Series (Daily)']).T
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    df.index = pd.to_datetime(df.index)
    return df

def add_stock(portfolio, symbol):
    portfolio[symbol] = get_stock_data(symbol)

def remove_stock(portfolio, symbol):
    if symbol in portfolio:
        del portfolio[symbol]

def track_performance(portfolio):
    for symbol, data in portfolio.items():
        # Check for missing or null values
        data.dropna(inplace=True)
        
        # Ensure 'Close' column is numeric
        data['Close'] = pd.to_numeric(data['Close'], errors='coerce')
        
        # Plot the data
        data['Close'].plot(label=symbol)
    plt.legend()
    plt.show()

portfolio = {}
add_stock(portfolio, 'AAPL')
add_stock(portfolio, 'GOOGL')
track_performance(portfolio)