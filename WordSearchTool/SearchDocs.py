import os
import tkinter as tk
from tkinter import filedialog
from docx import Document

def browse_folder():
    folder_path = filedialog.askdirectory() # Open a file dialog to select a folder
    search_folder(folder_path)

def search_folder(folder_path):
    search_term = search_entry.get() # Get the search term from the text box
    results = [] # List to store the search results
    for filename in os.listdir(folder_path):
        if filename.endswith('.docx'):
            docx_path = os.path.join(folder_path, filename)
            doc = Document(docx_path)
            for paragraph in doc.paragraphs:
                if search_term in paragraph.text:
                    # Append the result to the list
                    results.append(f'File: {filename} - Found: {paragraph.text}')
    
    # Write the results to a text file
    with open('search_results.txt', 'w') as file:
        for result in results:
            file.write(result + '\n')
    print('Search results written to search_results.txt')


# Create the main window
root = tk.Tk()
root.title('Word Document Search')
root.geometry('300x150')

# Create search entry
search_entry = tk.Entry(root)
search_entry.pack(pady=10)

# Create search button
search_button = tk.Button(root, text='Search', command=browse_folder)
search_button.pack()

root.mainloop()
