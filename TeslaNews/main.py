import stocks
import gui

# Alpha Vantage API key
API_KEY = 'XOV78YPS6ANMXOV6'
NEWS_API_KEY = '413e406fb0624d559b7e24ff901efa33'

# Stock symbol
SYMBOL = 'TSLA'

# Get the current stock price and news articles
stock_price = stocks.get_stock_price(API_KEY, SYMBOL)
news_articles = stocks.get_news_articles(NEWS_API_KEY, SYMBOL)

# Create the GUI
gui.create_gui(stock_price, news_articles)
