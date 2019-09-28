import os
from selenium import webdriver
import time
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    fname = browser.find_element_by_css_selector(".form-control:nth-child(2)")
    fname.send_keys("Name")
    lname = browser.find_element_by_css_selector(".form-control:nth-child(4)")
    lname.send_keys("Lastname")
    email = browser.find_element_by_css_selector(".form-control:nth-child(6)")
    email.send_keys("email@test.test")
    filebut = browser.find_element_by_css_selector("input[type ='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    filebut.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)