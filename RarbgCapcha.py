import cv2
import pytesseract
from selenium import webdriver

# Load the captcha image
img = cv2.imread('captcha.png')

# Preprocess the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray = cv2.medianBlur(gray, 3)

# Extract the text from the image using pytesseract
text = pytesseract.image_to_string(gray)

# Pass the extracted text to the input field
driver = webdriver.Chrome()
driver.get('https://rarbg.to/')
driver.find_element_by_xpath('//*[@id="solve_string"]').send_keys(text)
