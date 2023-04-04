import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

def create_gui(stock_price, news_articles):
    # Create the main window
    root = tk.Tk()

    # Create an impact font
    impact_font = tkfont.Font(family='Impact', size=20, weight='bold')

    # Create a label to display the current stock price
    price_label = tk.Label(root, text=f'TSLA: ${stock_price:.2f}', font=impact_font)
    price_label.pack()

    # Create a Text widget to display the news articles
    news_text = tk.Text(root, font='TkDefaultFont')
    news_text.pack()

    # Display the news articles
    for article in news_articles:
        news_text.insert(tk.END, article['title'] + '\n\n')
        news_text.insert(tk.END, article['description'] + '\n\n')

    # Create a Combobox widget to select the currency
    currency_var = tk.StringVar()
    currency_combobox = ttk.Combobox(root, textvariable=currency_var, values=['USD', 'GBP', 'ZAR'], font='TkDefaultFont')
    currency_combobox.pack()

    # Create a text entry box to input the number of shares
    shares_var = tk.StringVar()
    shares_entry = tk.Entry(root, textvariable=shares_var, font='TkDefaultFont')
    shares_entry.pack()

    # Create a label to display the value of the user's shares
    value_label = tk.Label(root, text='Value: ', font='TkDefaultFont')
    value_label.pack()

    # Dictionary to map currencies to symbols
    currency_symbols = {
        'USD': '$',
        'GBP': '£',
        'ZAR': 'R'
    }

    # Create a button to calculate the value of the user's shares
    calculate_button = tk.Button(root, text='Calculate', command=lambda: calculate_value(stock_price, currency_var.get(), shares_var.get(), currency_symbols, value_label), font='TkDefaultFont')
    calculate_button.pack()

    # Run the main event loop
    root.mainloop()

def calculate_value(stock_price, currency, shares, currency_symbols, value_label):
    shares = float(shares)
    if currency == 'USD':
        value = stock_price * shares
        symbol = currency_symbols['USD']
    elif currency == 'GBP':
        value = stock_price * shares * 0.72
        symbol = currency_symbols['GBP']
    elif currency == 'ZAR':
        value = stock_price * shares * 14.6
        symbol = currency_symbols['ZAR']
    value_label.config(text=f'Value: {symbol}{value:.2f}')
