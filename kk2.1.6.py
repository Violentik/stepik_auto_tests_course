import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:    
    browser.get("https://suninjuly.github.io/math.html")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    ye = browser.find_element(By.XPATH, "//*[contains(@id,'input_value')]")
    ye = ye.text
    input1 = browser.find_element(By.XPATH, "//*[contains(@class,'form-control')]")
    input1.send_keys(calc(ye))
    option1 = browser.find_element(By.XPATH, "//*[contains(@type,'checkbox')]").click()
    option2 = browser.find_element(By.XPATH, "//*[contains(@id,'robotsRule')]").click()
    button = browser.find_element(By.XPATH, "//*[contains(@type,'submit')]").click()
finally:
    time.sleep(10)
    browser.quit()
