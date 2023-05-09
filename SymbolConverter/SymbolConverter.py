import tkinter as tk
import pyperclip

def convert_text():
    # Get the user inputted string
    input_text = entry.get()

    # Define the dictionary of characters to be replaced
    char_dict = {
        'a': '@',
        'e': '3',
        'o': '0',
        's': '$',
        'h': '#',
        'l': '£',
        'z': '2',
        's': '5',
        't': '7',
        'i': '!'
    }

    # Replace the characters in the string
    output_text = ""
    upper_count = 0
    for i, char in enumerate(input_text):
        if char.lower() in char_dict:
            output_text += char_dict[char.lower()]
        elif char.isalpha():
            if upper_count % 2 == 0:
                output_text += char.upper()
            else:
                output_text += char.lower()
            upper_count += 1
        else:
            output_text += char
    # Update the output label with the converted string
    output_label.config(text=output_text)

def copy_to_clipboard():
    # Get the converted text from the output label
    converted_text = output_label.cget('text')

    # Copy the converted text to the clipboard
    pyperclip.copy(converted_text)

    # Update the copy confirmation label
    copy_confirm_label.config(text="Text copied to clipboard!")

# Create the main tkinter window
window = tk.Tk()
window.title("Text Converter")
window.geometry("400x300")
window.config(bg="#1F83FF")

# Create the entry widget for user input
entry = tk.Entry(window, font=("Impact", 14))
entry.pack(pady=10)

# Create the button widget to trigger text conversion
button_convert = tk.Button(window, text="Convert", command=convert_text, font=("Impact", 12), bg="#2c3e50", fg="white")
button_convert.pack()

# Create the label widget to display the converted text
output_label = tk.Label(window, text="", font=("Impact", 14), bg="#1F83FF", fg="black", highlightthickness=0, bd=0)
output_label.pack(pady=10)

# Create the button widget to copy the converted text to the clipboard
button_copy = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, font=("Impact", 12), bg="#2c3e50", fg="white")
button_copy.pack()

# Create the label widget to display the copy confirmation message
copy_confirm_label = tk.Label(window, text="", font=("Impact", 14), bg="#1F83FF", fg="#008000", highlightthickness=0, bd=0)
copy_confirm_label.pack(pady=10)

# Run the tkinter event loop
window.mainloop()
