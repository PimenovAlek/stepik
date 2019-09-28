import math
from selenium import webdriver
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_locate = browser.find_element_by_id("input_value")
    x = int(x_locate.text)
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 130);")
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobut = browser.find_element_by_id("robotsRule")
    radiobut.click()
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)