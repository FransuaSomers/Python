import os
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import infi.systray
from PIL import Image, ImageDraw


class NotesApp:
    def __init__(self):
        # Define the path to the file where the icon paths are stored
        ICON_PATH_FILE = "icon_paths.txt"

        # Check if the file exists and read the stored icon paths
        if os.path.exists(ICON_PATH_FILE):
            with open(ICON_PATH_FILE, "r") as f:
                icon_paths = f.read().strip().split("\n")
        else:
            # Prompt the user to select an icon file
            root = tk.Tk()
            root.withdraw()
            icon_paths = [filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])]
            # Write the selected icon path to the file
            with open(ICON_PATH_FILE, "w") as f:
                f.write(icon_paths[0])

        # Check if the specified icon paths exist and prompt the user to enter a new path if not
        for i, path in enumerate(icon_paths):
            if not os.path.exists(path):
                root = tk.Tk()
                root.withdraw()
                new_path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
                icon_paths[i] = new_path
                with open(ICON_PATH_FILE, "w") as f:
                    f.write("\n".join(icon_paths))

        # Create the root window
        self.root = tk.Tk()

        # Set the system tray icon
        if os.path.exists(icon_paths[0]):
            self.icon_path = icon_paths[0]
        else:
            root = tk.Tk()
            root.withdraw()
            self.icon_path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
            icon_paths[0] = self.icon_path
            with open(ICON_PATH_FILE, "w") as f:
                f.write("\n".join(icon_paths))

        # Set the system tray icon
        self.root.iconbitmap(default=self.icon_path)

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
        menu = (("New Note", None, lambda x: self.create_new_note()))

        tray_icon = infi.systray.SysTrayIcon(self.icon_path, "NotesIcon", menu)

        # Start the system tray icon
        tray_icon.start()

        # Store the tray_icon instance as an instance variable
        self.tray_icon = tray_icon

    def set_icon(self):
        # Prompt the user to select an icon file
        root = tk.Tk()
        root.withdraw()
        icon_file = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])

        # Save the icon filepath to a text file
        with open("icon_filepaths.txt", "w") as f:
            f.write(icon_file)

        # Load the selected image file
        icon = Image.open(icon_file)

        # Update the system tray icon with the selected icon
        menu = (("New Note", None, lambda x: self.create_new_note()),
                ("Remove Icon", None, lambda x: self.remove_icon()))

        if os.path.exists(icon_file):
            self.icon_path = icon_file
        else:
            self.icon_path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
            with open("icon_filepaths.txt", "w") as f:
                f.write(self.icon_path)

        tray_icon = infi.systray.SysTrayIcon(self.icon_path, "NotesIcon", menu)
        tray_icon.update(icon)


    def quit_app(self, systray):
        systray.shutdown()

    def create_new_note(self):
        # Create a new note
        pass

    def remove_icon(self):
        # Remove the icon
        pass



if __name__ == "__main__":
    app = NotesApp()

