import math
from selenium import webdriver
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    but = browser.find_element_by_tag_name("button")
    but.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_locate = browser.find_element_by_id("input_value")
    x = int(x_locate.text)
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)