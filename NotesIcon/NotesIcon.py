import os
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import infi.systray
from PIL import Image, ImageDraw

class NotesApp:
    def __init__(self):
        # Create the root window
        self.root = tk.Tk()
        self.root.iconbitmap(default="default_icon.ico") # Set default icon
        # self.root.withdraw() # Remove this line

        # Create the system tray icon
        self.create_system_tray_icon()

        # Start the main event loop
        self.root.mainloop()

    def create_system_tray_icon(self):
        # Create a blank image for the system tray icon
        icon = Image.new("RGBA", (16, 16), (255, 255, 255, 0))
        draw = ImageDraw.Draw(icon)

        # Draw a black rectangle in the center of the icon
        draw.rectangle((5, 5, 10, 10), fill=(0, 0, 0, 255))

        # Create the system tray icon
        menu = (("Close", None, lambda x: self.quit_app()),
                ("New Note", None, lambda x: self.create_new_note()),
                ("Set Icon", None, lambda x: self.set_icon()))

        # Create the system tray icon and set its title
        tray_icon = infi.systray.SysTrayIcon(icon, "Notes", menu)

        # Start the system tray icon
        tray_icon.start()

    def set_icon(self):
        # Set the icon filepath to a hardcoded value
        icon_file = r"C:\Users\fransua\Desktop\Python\Python\NotesIcon\notes.ico"

        # Save the icon filepath to a text file
        with open("icon_filepaths.txt", "w") as f:
            f.write(icon_file)

        # Load the selected image file
        icon = Image.open(icon_file)

        # Update the system tray icon with the selected icon
        menu = (("Close", None, lambda x: self.quit_app()),
                ("New Note", None, lambda x: self.create_new_note()),
                ("Remove Icon", None, lambda x: self.remove_icon()))

        tray_icon = infi.systray.SysTrayIcon(icon, "Notes", menu)
        tray_icon.update(icon)
    
    def quit_app(self):
        # Quit the application
        self.root.quit()
        self.root.destroy()

    def create_new_note(self):
        # Create a new note
        pass

    def remove_icon(self):
        # Remove the icon
        pass
