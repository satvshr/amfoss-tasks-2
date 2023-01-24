
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
browser = webdriver.Firefox()
browser.get('https://play2048.co/')
key_select = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
message = browser.find_element_by_css_selector('.game-message p')
key = browser.find_element_by_tag_name('html')

while message.text != 'Game over!':
    key.send_keys(key_select[random.randint(0, 3)])
    message = browser.find_element_by_css_selector('.game-message p')







