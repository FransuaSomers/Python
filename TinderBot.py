from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep 
import random

path = 'C:\chromedriver.exe'
service = Service(executable_path=path)
web = 'https://tinder.com'

options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(service=service, options=options)

driver.get(web)


""" class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def open_tinder(self):
        self.driver.get('https://tinder.com') 

        sleep(3)
        login = self.driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
        login.click()
    def facebook_login(self):
        login_with_facebook= self.driver.find_element('xpath', '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div')
        login_with_facebook.click()


bot = TinderBot()
bot.open_tinder() """