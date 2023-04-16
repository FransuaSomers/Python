import requests
import infi.systray as systray

# Set the URL of the API endpoint
url = 'https://api.github.com/repos/FransuaSomers/Python/commits'

# Send a GET request to the API endpoint
response = requests.get(url)

# Parse the JSON response
commits = response.json()


# Get the most recent commit title
most_recent_commit_title = commits[0]['commit']['message'].splitlines()[0]

# Get the most recent commit message
most_recent_commit_message = commits[0]['commit']['message'].replace("+", "\n+")

with open('commit_message.txt', 'w') as f:
    f.write(most_recent_commit_message)


# Define the callback function for the system tray app
def on_quit_callback(systray):
    print("Quitting System Tray App...")
    systray.shutdown()


def on_right_click(systray):
    # Define the menu items for the system tray app
    menu_options = (
        ("{}".format(most_recent_commit_title), None, lambda event: None),
    )
    systray.update(menu_options=menu_options)


def on_hover_callback(systray):
    # Update the hover text to display the most recent commit message
    print("Hovering Over Icon...")
    systray.hover_text = " " + most_recent_commit_title


# Create the system tray app
tray_icon = systray.SysTrayIcon(
    "python.ico",
    hover_text="GitHub Commits",
    on_quit=on_quit_callback,
    menu_options=(
        ("{}".format(most_recent_commit_title), None, lambda event: None),
    )
)

tray_icon.right_click_functions = [on_right_click]
tray_icon.hover_functions = [on_hover_callback]
tray_icon.start()
