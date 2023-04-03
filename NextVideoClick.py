from pynput.mouse import Listener, Button
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Replace the URL and the path to the webdriver with your own values
url = "https://www.youtube.com/"
driver_path = "/path/to/chromedriver"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=driver_path)

# Navigate to the URL
driver.get(url)

# Find the button element by its XPath
button_xpath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-button-renderer/yt-button-shape/button"
button = driver.find_element_by_xpath(button_xpath)

# Define a callback function for mouse events
def on_click(x, y, button, pressed):
    if button == Button.right and pressed:
        # Right-click detected, move the mouse over the button and left-click
        actions = ActionChains(driver)
        actions.move_to_element(button).click().perform()

# Start the mouse listener
with Listener(on_click=on_click) as listener:
    listener.join()

# Close the browser
#driver.quit()
