import datetime
import infi.systray
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Define the path to the file where the icon path is stored
ICON_PATH_FILE = "icon_paths.txt"

# Check if the file exists and read the stored icon path
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



# Define the function to show the countdown clock
def show_countdown():

    # Create a new tkinter window
    root = tk.Tk()
    root.geometry('300x160+{}+0'.format(root.winfo_screenwidth()-300))
    root.title('Countdown')
    root.configure(background='#0000FF')
    root.iconbitmap(icon_paths[0]) # set the icon for the window
    root.wm_attributes('-topmost', True) # bring the window to the front
    root.resizable(True, True) # show the minimize and maximize buttons
    root.overrideredirect(False) # show the minimize and maximize buttons
    root.iconify() # minimize the window to the taskbar

    lunch_label = tk.Label(root, text="Lunch Break", font=('Impact', 20, 'bold'), fg='green', bg='#0000FF')
    lunch_label.pack()
    lunch_label.pack_forget()
    
    style = ttk.Style()
    style.theme_create("my_theme", parent="alt", settings={
        "TButton": {
            "configure": {
                "foreground": "green",
                "background": "black",
                "font": ("Impact", 12) # change the font size here
            },
        },
    })
    # use the custom theme for the button
    style.theme_use("my_theme")
    lunch_button = ttk.Button(root, text="Lunch Time")
    lunch_button.pack()

    lunch_time_remaining_label = tk.Label(root, text="", font=('Impact', 12, 'bold'), fg='white', bg='#0000FF')
    lunch_time_remaining_label.pack()

    # Define the function to handle the lunch break button click
    def lunch_break():
        lunch_label.config(text="Lunch Break")
        lunch_label.config(foreground='green')
        lunch_button.config(state="disabled")  # disable the lunch button
        lunch_label.pack()
        lunch_time_remaining_label.pack()
        
        end_time = datetime.datetime.now() + datetime.timedelta(minutes=30)
        remaining_time = end_time - datetime.datetime.now()

        def update_lunch_time_remaining():
            nonlocal remaining_time
            remaining_time -= datetime.timedelta(seconds=1)
            if remaining_time > datetime.timedelta():
                minutes, seconds = divmod(remaining_time.seconds, 60)
                time_label_text = '{:02d}:{:02d}'.format(minutes, seconds)
                lunch_time_remaining_label.config(text=f"Time remaining: {time_label_text}")
                lunch_time_remaining_label.after(1000, update_lunch_time_remaining)
            else:
                lunch_time_remaining_label.config(text="Time's up!")
                lunch_button.config(state="normal")  # enable the lunch button

        update_lunch_time_remaining()
        
        root.after(1800000, end_lunch_break_and_continue_countdown)
        

    # Define the function to handle the end of lunch break and continue the countdown
    def end_lunch_break_and_continue_countdown():
        lunch_label.pack_forget()
        lunch_button.config(state="normal")  # enable the lunch button
        now = datetime.datetime.now()
        if now.weekday() < 4:  # Monday through Thursday
            end_time = now.replace(hour=17, minute=0, second=0, microsecond=0)
        else:  # Friday
            end_time = now.replace(hour=16, minute=30, second=0, microsecond=0)

        remaining_time = end_time - now
        if remaining_time > datetime.timedelta():
            minutes, seconds = divmod(remaining_time.seconds, 60)
            hours, minutes = divmod(minutes, 60)
            time_label_text = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
            time_label.config(foreground='black')
        else:
            time_label_text = 'Time is up!'
            time_label.config(foreground='red')

        time_label.config(text=time_label_text)
        icon.update(hover_text=time_label_text)  # update system tray icon's label text
        root.after(1000, countdown, root, time_label, icon, remaining_time.seconds)


    # Bind the lunch break button to the lunch_break function
    lunch_button.config(command=lunch_break)

    # Define the countdown function
    def countdown(root, time_label, icon, duration, remaining_time=None):
        now = datetime.datetime.now()
        if remaining_time is None:
            if now.weekday() < 4:  # Monday through Thursday
                end_time = now.replace(hour=17, minute=0, second=0, microsecond=0)
            else:  # Friday
                end_time = now.replace(hour=16, minute=30, second=0, microsecond=0)
            remaining_time = end_time - now

        if remaining_time > datetime.timedelta():
            minutes, seconds = divmod(remaining_time.seconds, 60)
            hours, minutes = divmod(minutes, 60)
            time_label_text = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
            time_label.config(foreground='black')
        else:
            time_label_text = 'Time is up!'
            time_label.config(foreground='red')

        time_label.config(text=time_label_text)
        time_label.config(background='#0000FF')
        time_label.update()
        icon.update(hover_text=time_label_text)  # update system tray icon's label text
        root.after(1000, countdown, root, time_label, icon, duration, remaining_time - datetime.timedelta(seconds=1))

        duration -= 1
        if duration == 0:
            root.iconify() # minimize the window after the specified duration


    # Create the time label and countdown button
    time_label = ttk.Label(root, font=('Impact', 40))
    time_label.pack()

    duration = 5 # set the duration for the window to stay open
    countdown(root, time_label, icon, duration) # call countdown function here

    root.update_idletasks() # update the window so that it appears when called
    root.deiconify() # show the window
    root.attributes('-topmost', True) # bring the window to the front
    root.after(3000, lambda: root.attributes('-topmost', False)) # remove the topmost attribute after 3 seconds
    root.mainloop()


# Define the function to handle the right-click event
def on_quit(systray):
    systray.shutdown()

def on_right_click(systray):
    menu_options = (("Countdown", None, lambda: show_countdown()))
    systray.update(menu_options=menu_options)

# Create the icon and set its title
menu_options = (("Countdown", None, lambda systray: show_countdown()),)
icon = infi.systray.SysTrayIcon(icon_paths[0], "CountdownIcon", menu_options)

# Start the app
icon.start()