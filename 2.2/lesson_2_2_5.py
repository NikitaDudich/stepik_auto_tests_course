import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys("Nikita")
    
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys("Dudich")
    
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("test@mail.ru")
    
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
