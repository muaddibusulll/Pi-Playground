import requests
from datetime import date, timedelta, datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCKS_API_KEY = "your_API"
API_function = "TIME_SERIES_DAILY_ADJUSTED"
today = date.today()
yesterday = today - timedelta(days=1)

# STEP 1: Use https://www.alphavantage.co
def get_stock():
    stock_parameters = {
        "function" : API_function,
        "symbol" : STOCK,
        "apikey" : STOCKS_API_KEY
    }
    
    stocks_url = f"https://www.alphavantage.co/query"
    stocks_response = requests.get(stocks_url, params=stock_parameters)
    stocks_data = stocks_response.json()
    return stocks_data

today_stock = get_stock()["Time Series (Daily)"][f"{today}"]
print(today_stock)
