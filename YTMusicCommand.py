import pyautogui
import keyboard
import pychrome

# Set up the hotkey for Windows + P
keyboard.add_hotkey('win+p', lambda: pause_youtube_music())

def pause_youtube_music():
    # Create a pychrome client and activate the current tab in Chrome
    chrome = pychrome.Browser(url="http://127.0.0.1:9222")
    tabs = chrome.list_tabs()
    for tab in tabs:
        if tab['active']:
            current_tab = chrome.activate_tab(tab['id'])
            break

    # Send the pause command to the YouTube Music player
    current_tab.call_method("Runtime.evaluate", expression="document.querySelector('ytmusic-player-bar').getPlayerState() == 'PLAYING' && document.querySelector('ytmusic-player-bar').pauseVideo();")

    # Close the pychrome client
    chrome.close()

# Keep the program running to listen for hotkeys
keyboard.wait()
