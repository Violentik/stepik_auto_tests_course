from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
try:
    
    browser.get(link)
    kk = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element(By.LINK_TEXT, kk).click()
    time.sleep(1)
    input1 = browser.find_element(By.XPATH, "//*[contains(@name,'first_name')]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//*[contains(@name,'last_name')]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//*[contains(@name,'firstname')]")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.XPATH, "//*[contains(@id,'country')]")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла