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
    root.geometry('300x150+{}+0'.format(root.winfo_screenwidth()-300))
    root.title('Countdown')
    root.configure(background='#0000FF')
    root.iconbitmap(icon_path) # set the icon for the window
    root.wm_attributes('-topmost', True) # bring the window to the front
    root.resizable(True, True) # show the minimize and maximize buttons
    root.overrideredirect(False) # show the minimize and maximize buttons
    root.iconify() # minimize the window to the taskbar

    lunch_button = ttk.Button(root, text="Lunch Time")
    lunch_button.pack(pady=5)

    # Define the function to handle the lunch break button click
    def lunch_break():
        countdown.lunch_break = True  # set the lunch break flag
        time_label.config(text="Lunch Break")
        time_label.config(foreground='green')
        lunch_button.config(state="disabled")  # disable the lunch button
        root.after(1800000, end_lunch_break)  # schedule the end of lunch break after 30 minutes

    # Define the function to handle the end of lunch break
    def end_lunch_break():
        countdown.lunch_break = False  # reset the lunch break flag
        lunch_button.config(state="normal")  # enable the lunch button

    # Bind the lunch break button to the lunch_break function
    lunch_button.config(command=lunch_break)
        
    # Define the countdown function
    def countdown(root, time_label, icon, duration):
        now = datetime.datetime.now()
        if now.weekday() < 4:  # Monday through Thursday
            end_time = now.replace(hour=17, minute=0, second=0, microsecond=0)
        else:  # Friday
            end_time = now.replace(hour=16, minute=30, second=0, microsecond=0)
            
        # Check if it's within lunch break period (12:00pm-12:30pm)
        if now.weekday() < 5 and now.hour == 12 and now.minute >= 0 and now.minute < 30:
            time_label_text = "Lunch Break"
            time_label.config(text=time_label_text)
            time_label.config(background='#0000FF')
            time_label.config(foreground='green')
            time_label.update()
            icon.update(hover_text=time_label_text)  # update system tray icon's label text
            root.after(1000, countdown, root, time_label, icon, duration)
        else:
            remaining_time = end_time - now
            if remaining_time > datetime.timedelta():
                minutes, seconds = divmod(remaining_time.seconds, 60)
                hours, minutes = divmod(minutes, 60)
                time_label_text = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
                time_label.config(text=time_label_text)
                time_label.config(foreground='black')
                time_label.config(background='#0000FF')
                time_label.update()
                icon.update(hover_text=time_label_text)  # update system tray icon's label text
                root.after(1000, countdown, root, time_label, icon, duration)
            else:
                time_label.config(text='Time is up!')
                time_label.config(background='#0000FF')
                time_label.config(foreground='red')
                icon.update(hover_text='Time is up!')

        duration -= 1
        if duration == 0:
            root.iconify() # minimize the window after the specified duration


    # Create the time label and countdown button
    time_label = ttk.Label(root, font=('Impact', 40))
    time_label.pack(pady=20)

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
icon = infi.systray.SysTrayIcon(icon_path, "CountdownIcon", menu_options)

# Start the app
icon.start()