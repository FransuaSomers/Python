import requests

def get_stock_price(api_key, symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return float(data['Global Quote']['05. price'])

def get_news_articles(api_key, symbol):
    url = f'https://newsapi.org/v2/everything?q={symbol}&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['articles'][:5]
