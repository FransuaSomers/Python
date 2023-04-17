import requests
import os
import infi.systray as systray
import threading
import time

# Set the URL of the API endpoint
url = 'https://api.github.com/repos/FransuaSomers/Python/commits'

# Send a GET request to the API endpoint
response = requests.get(url)

# Parse the JSON response
commits = response.json()

# Find the most recent commit that isn't a merge commit
most_recent_commit = None
for commit in commits:
    if 'Merge branch' not in commit['commit']['message']:
        most_recent_commit = commit
        break

# Get the most recent commit title and message
most_recent_commit_title = most_recent_commit['commit']['message'].splitlines()[0]
most_recent_commit_message = most_recent_commit['commit']['message'].replace("+", "\n+")


with open('commit_message.txt', 'w') as f:
    f.write(most_recent_commit_message)

# Define the callback function for the system tray app
def on_quit_callback(systray):
    threading.Thread(target=systray.shutdown).start()

def on_right_click(systray):
    # Define the menu items for the system tray app
    menu_options = (
        ("{}".format(most_recent_commit_title), None, lambda event: None),
        ("View Commit Message", None, lambda event: os.system('notepad.exe commit_message.txt')),
        ("Quit", None, on_quit_callback),
    )
    systray.update(menu_options=menu_options)

# Create the system tray app
tray_icon = systray.SysTrayIcon(
    "github.ico",
    hover_text = most_recent_commit_title,
    on_quit=on_quit_callback,
    menu_options=(
        ("{}".format(most_recent_commit_title), None, lambda event: None),
    )
)

tray_icon.right_click_functions = [on_right_click]
tray_icon.start()

