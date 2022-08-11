from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import math



driver_service = Service(executable_path="/Users/nikolai/Desktop/lesson/chromedriver")
browser = webdriver.Chrome(service=driver_service)

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)

    button1 = browser.find_element(By.TAG_NAME, 'button')
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    n = browser.find_element(By.ID, 'input_value')
    n1 = n.text
    x = calc(n1)

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(x)

    button2 = browser.find_element(By.TAG_NAME, 'button')
    button2.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
