import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    print(x)
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    print(y)
    value = int(x)+int(y)
    print(value)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(value)) # ищем элемент с текстом "Python"
    
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
  

