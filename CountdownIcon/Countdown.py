import datetime
import infi.systray
from PIL import Image
import tkinter as tk
from tkinter import ttk

# Set the path to the icon file
icon_path = "C:/Users/frans/Desktop/Python/CountdownIcon/clock1.ico"

# Define the function to show the countdown clock
def show_countdown():
    # Create a new tkinter window
    root = tk.Tk()
    root.geometry('300x100+{}+0'.format(root.winfo_screenwidth()-300))
    root.title('Countdown')

    # Define the countdown function
    def countdown(root, time_label, icon):
        end_time = datetime.datetime.now().replace(hour=17, minute=0, second=0, microsecond=0)
        remaining_time = end_time - datetime.datetime.now()
        if remaining_time > datetime.timedelta():
            time_label_text = '{}:{}:{}'.format(int(remaining_time.seconds/3600), int(remaining_time.seconds/60%60), int(remaining_time.seconds%60))
            time_label.config(text=time_label_text)
            time_label.update()
            icon.update(hover_text=time_label_text)  # update system tray icon's label text
            root.after(1000, countdown, root, time_label, icon)
        else:
            time_label.config(text='Time is up!')
            time_label.config(foreground='red')
            icon.update(hover_text='Time is up!')


    # Create the time label and countdown button
    time_label = ttk.Label(root, font=('Impact', 40))
    time_label.pack(pady=20)
    countdown(root, time_label, icon) # call countdown function here

    root.mainloop()

# Define the function to handle the right-click event
def on_quit(systray):
    systray.shutdown()

def on_right_click(systray):
    menu_options = (("Countdown", None, lambda: show_countdown()))
    systray.update(menu_options=menu_options)

# Create the icon and set its title
menu_options = (("Countdown", None, lambda systray: show_countdown()),)
icon = infi.systray.SysTrayIcon(icon_path, "CountdownIcon", menu_options)

# Start the app
icon.start()
