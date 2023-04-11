import os
import shutil
import tkinter as tk
from tkinter import filedialog
import pyttsx3
import PyPDF2
import tkinter.messagebox as messagebox
from tkinter import ttk
import mutagen
from mutagen.mp3 import MP3

def convert_pdf():
    # Create a Tkinter file dialog to select a PDF file
    root = tk.Tk()
    root.withdraw()
    pdf_path = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])

    if not pdf_path:
        messagebox.showerror("Error", "No PDF file selected.")
    else:
        # Extract the file name and create a corresponding text file name
        pdf_file_name = os.path.basename(pdf_path)
        txt_prefix = "text_"
        txt_file_name = txt_prefix + f"{pdf_file_name[:-4]}.txt"

        # Open the PDF file and create a PyPDF2 reader object
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Create and pack the progress bar widget
            progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
            progress_bar.pack(pady=10)

            # Iterate through each page of the PDF file and extract the text
            text = ""
            total_pages = len(pdf_reader.pages)
            for i in range(total_pages):
                page = pdf_reader.pages[i]
                text += page.extract_text()
                progress = int((i+1)/total_pages*100)
                progress_bar['value'] = progress
                root.update_idletasks()

            # Destroy the progress bar widget
            progress_bar.destroy()

        # Extract the file name and create a corresponding audio file name
        audio_prefix = "audio_"
        audio_file_name = audio_prefix + f"{pdf_file_name[:-4]}.mp3"

        # Create a new text file with the extracted text if it doesn't already exist
        folder_name = os.path.splitext(pdf_file_name)[0]
        if os.path.exists(folder_name):
            messagebox.showwarning("Warning", "Folder already exists.")
        else:
            os.mkdir(folder_name)
            txt_exists = os.path.exists(os.path.join(folder_name, txt_file_name))
            audio_exists = os.path.exists(os.path.join(folder_name, audio_file_name))
            if not txt_exists:
                with open(os.path.join(folder_name, txt_file_name), 'w', encoding='utf-8') as txt_file:
                    txt_file.write(text)
            if not audio_exists:
                # Convert the text to speech using the pyttsx3 library
                engine = pyttsx3.init()
                engine.setProperty('audio_file_format', 'mp3')
                engine.setProperty('voice', 'english+m3')

                # Calculate the approximate file size
                text_length = len(text)
                bit_rate = 128 # 128 kbps
                audio_length_sec = int(text_length/20) # assume speaking rate of 200 wpm
                audio_file_size_kb = int((bit_rate * audio_length_sec) / 8 / 1024)
                print(f"Approximate audio file size: {audio_file_size_kb} KB")

                engine.save_to_file(text, os.path.join(folder_name, audio_file_name))
                engine.runAndWait()

                # Add length metadata to the audio file
                try:
                    audio_file_path = os.path.abspath(os.path.join(folder_name, audio_file_name))
                    print("audio_file_path:", audio_file_path)
                    audio_length = MP3(audio_file_path).info.length
                    audio_file = mutagen.File(audio_file_path)
                    audio_file.tags.add(mutagen.id3.TLEN(encoding=3, text=str(int(audio_length*1000))))
                    audio_file.save()
                except Exception as e:
                    messagebox.showerror("Error", f"Error processing audio file: {str(e)}")


                # Copy the original PDF file to the newly created folder
                pdf_new_path = os.path.join(folder_name, pdf_file_name)
                shutil.copy2(pdf_path, pdf_new_path)

                # Update the progress bar to indicate that the audio file has been created
                progress_bar['value'] = 100
                root.update_idletasks()

                # Ask the user if they want to open the folder
                result = messagebox.askquestion("Question", "Do you want to open the folder?")
                if result == 'yes':
                    # Open the folder using the default file explorer
                    os.startfile(folder_name)

                # Ask the user if they want to convert another PDF
                result = messagebox.askquestion("Question", "Do you want to convert another PDF?")
                if result == 'no':
                    root.destroy() # Close the current root window



# Call the convert_pdf function to start the program
convert_pdf()