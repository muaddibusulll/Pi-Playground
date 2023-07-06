import requests
from datetime import date, timedelta, datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCKS_API_KEY = "your_API"
API_function = "TIME_SERIES_DAILY_ADJUSTED"

def get_stock() -> dict:
    """
        A function witch returns the Daily stock market data from the API.
        In this function we just make an API request and we return all the data.

        Returns:
            This function returns all the stock data from the API.
    """
    stock_parameters = {
        "function" : API_function,
        "symbol" : STOCK,
        "apikey" : STOCKS_API_KEY
    }
    
    stocks_url = f"https://www.alphavantage.co/query"
    stocks_response = requests.get(stocks_url, params=stock_parameters)
    stocks_response.raise_for_status()
    stocks_data = stocks_response.json()
    return stocks_data["Time Series (Daily)"]

def get_the_last_two_days(stock_data: dict) -> list:
    """
        A function witch returns the two latest dates with data. 

        Args:
            stock_data (dictionary) -> the stocks dictionary.
        
        Returns:
            This function returns a list with two values. The two most current days with stock market data.
    """
    sorted_dates = sorted(stock_data.keys(), reverse=True)
    return sorted_dates[:2]

def return_the_percentage() -> float:
    """
        In this function we just take try to take the percentage difference between of the two days.

        Returns:
            This function returns a float number witch is the percentage difference from the two days.
    """

    stocks_data = get_stock()
    last_two_days = get_the_last_two_days(stock_data=stocks_data)

    most_current_day = stocks_data[last_two_days[0]]
    the_day_before = stocks_data[last_two_days[1]]

    most_current_day_closing_price = float(most_current_day["4. close"])
    the_day_before_closing_price = float(the_day_before["4. close"])

    # Take the difference in the price between the two days.
    difference_between_prices = abs(most_current_day_closing_price - the_day_before_closing_price)

    # Here we take the difference percentage of these two days.
    percentage_difference = ( difference_between_prices / most_current_day_closing_price ) * 100

    return round(percentage_difference, 2)

def get_news(percentage_number: float):

    if (percentage_number > 5) or (percentage_number < 5):
        print("Get news")

get_news(percentage_number=return_the_percentage())
