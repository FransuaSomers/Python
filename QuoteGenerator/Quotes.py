import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Import ttk for themed widgets

API_KEY = 'wnBFmCYBeQaQPb67weXb1A==1oPE1pOs5J24B5b7'  # Replace with your actual API key

# Function to generate a quote of the day using the quotes API
def generate_quote_of_the_day(category):
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        quotes = response.json()
        if quotes:
            quote = quotes[0]['quote']
            author = quotes[0]['author']
            return quote, author
        else:
            return None, None
    else:
        print("Error:", response.status_code, response.text)
        return None, None

# Function to update the quote label
def update_quote_label():
    category = category_combobox.get()  # Get the selected category from the combobox
    quote, author = generate_quote_of_the_day(category)
    if quote:
        quote_label.config(text="Quote of the day: \n\n" + quote + "\n\n" + "Author: " + author, font=("Impact", 14))
    else:
        messagebox.showerror("Error", "This category doesn't exist.")

# Function to handle button click event
def generate_quote_button_click():
    update_quote_label()

# Function to handle exit button click event
def exit_button_click():
    root.destroy()

# Create a Tkinter window
root = tk.Tk()
root.title("Quote of the Day")
root.geometry("400x300")
root.config(bg="white") # Set background color to white

# Create a label for category input
category_label = tk.Label(root, text="Select category:", font=("Impact", 14), bg="white")
category_label.pack()

# Create a combobox for category selection
categories = ["age", "alone", "amazing", "anger", "architecture", "art", "attitude", "beauty", "best", "birthday",
              "business", "car", "change", "communications", "computers", "cool", "courage", "dad", "dating",
              "death", "design", "dreams", "education", "environmental", "equality", "experience", "failure", "faith",
              "family", "famous", "fear", "fitness", "food", "forgiveness", "freedom", "friendship", "funny", "future",
              "god", "good", "government", "graduation", "great", "happiness", "health", "history", "home", "hope",
              "humor", "imagination", "inspirational", "intelligence", "jealousy", "knowledge", "leadership", "learning",
              "legal", "life", "love", "marriage", "medical", "men", "mom", "money", "morning", "movies", "success"]
category_combobox = ttk.Combobox(root, values=categories, font=("Helvetica", 12), width=20)
category_combobox.pack(pady=5, fill=tk.X)  # Add fill=tk.X to fill the horizontal space

# Create a label to display the quote
quote_label = tk.Label(root, text="", wraplength=350, justify="center", font=("Impact", 14), bg="white")
quote_label.pack(pady=10)

# Create a button to generate a new quote
generate_button = tk.Button(root, text="Generate Quote", font=("Impact", 14), command=generate_quote_button_click)
generate_button.pack()

# Create an exit button
def exit_button_click():
    root.destroy()

exit_button = tk.Button(root, text="Exit", font=("Impact", 14), command=exit_button_click)
exit_button.pack()

# Function to update the quote label
def update_quote_label():
    category = category_combobox.get()  # Get the selected category from the combobox
    quote, author = generate_quote_of_the_day(category)
    if quote:
        quote_label.config(text="Quote of the day: \n\n" + quote + "\n\n" + "Author: " + author, font=("Impact", 14))
        # Move the Generate Quote button and Exit button below the updated quote label
        generate_button.pack()
        exit_button.pack()
    else:
        messagebox.showerror("Error", "This category doesn't exist.")

# Function to handle button click event
def generate_quote_button_click():
    update_quote_label()

# Main event loop
root.mainloop()
