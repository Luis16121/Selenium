#Login Facebook
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from secrets import username, password

driver = webdriver.Firefox()
driver.get("https://es-la.facebook.com/")
#driver.maximize_window()

# Ingresar User
elem = driver.find_element(by=By.ID, value="email")
elem.send_keys(username)

# Ingresar Pass
elem = driver.find_element(by=By.ID, value="pass")
elem.send_keys(password)

# login Enter
elem.send_keys(Keys.RETURN)