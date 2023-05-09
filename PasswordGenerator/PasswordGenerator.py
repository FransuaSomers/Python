import requests
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import tkinter.messagebox as messagebox
import pyperclip

# Replace 'YOUR_API_KEY' with your actual API key from API Ninjas
API_KEY = 'wnBFmCYBeQaQPb67weXb1A==1oPE1pOs5J24B5b7'

# Function to generate password
def generate_password():
    length = combo_length.get()
    api_url = 'https://api.api-ninjas.com/v1/passwordgenerator?length={}'.format(length)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        password_json = response.json()
        password = password_json["random_password"]
        # Append to .txt list with username, password, and length
        username = entry_username.get()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        password_data = "{} UN:{} PW:{} (Length: {})".format(date, username, password, length)
        with open('passwords.txt', 'a') as file:
            file.write(password_data + "\n")
        lbl_password.config(text=password)  # Update the text of lbl_password with the password
        lbl_message.config(text="")  # Update the label with an empty message
        btn_copy.grid(column=0, row=4, columnspan=2, padx=10, pady=10)  # Add the "Copy to Clipboard" button back to the grid
        btn_copy.config(state='normal')  # Enable the "Copy to Clipboard" button
    else:
        lbl_password.config(text="Error: {} {}".format(response.status_code, response.text))
        lbl_message.config(text="", foreground="black")  # Update the label with an empty message
        btn_copy.grid_remove()  # Hide the "Copy to Clipboard" button
        btn_copy.config(state='disabled')  # Disable the "Copy to Clipboard" button
        


# Function to copy password to clipboard
def copy_password():
    password = lbl_password.cget("text")
    pyperclip.copy(password)
    lbl_message.config(text="Password copied to clipboard!", foreground="green")  # Update the label with the success message

# Create tkinter window
root = tk.Tk()
root.title("Password Generator")

# Set font size and family
LARGE_FONT = ("Impact", 16)
MEDIUM_FONT = ("Impact", 12)

# Create username entry field
lbl_username = ttk.Label(root, text="Username:", font=LARGE_FONT)
lbl_username.grid(column=0, row=0, padx=10, pady=10)
entry_username = ttk.Entry(root, font=MEDIUM_FONT)
entry_username.grid(column=1, row=0, padx=10, pady=10)

# Create password length combobox
lbl_length = ttk.Label(root, text="Password Length:", font=LARGE_FONT)
lbl_length.grid(column=0, row=1, padx=10, pady=10)
combo_length = ttk.Combobox(root, values=[str(i) for i in range(8, 21)], state="readonly", font=MEDIUM_FONT)
combo_length.set("16")
combo_length.grid(column=1, row=1, padx=10, pady=10)

# Create generate password button
btn_generate = ttk.Button(root, text="Generate Password", command=generate_password)
btn_generate["style"] = "TButton"
btn_generate.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Create password label
lbl_password = ttk.Label(root, text="", font=LARGE_FONT)
lbl_password.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Create copy to clipboard button
btn_copy = ttk.Button(root, text="Copy to Clipboard", command=copy_password, state='disabled')
btn_copy["style"] = "TButton"
btn_copy.grid_remove()

# Create message label
lbl_message = ttk.Label(root, text="", font=LARGE_FONT)
lbl_message.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

# Run tkinter event loop
root.mainloop()

