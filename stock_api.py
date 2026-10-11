import requests
import os
api_key = ""# add your API key here


#api_key = os.environ.get("FINNHUB_API_KEY")

def get_price(ticker):
    url = "https://finnhub.io/api/v1/quote"

    params = {
        "symbol": ticker,
        "token": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data["c"]


def get_name(ticker):
    url = "https://finnhub.io/api/v1/stock/profile2"

    params = {
        "symbol": ticker,
        "token": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data["name"]








