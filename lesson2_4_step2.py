from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def button(x):
    button = browser.find_element_by_id(x)
    button.click()
    

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000"))

button("book")

find_x = browser.find_element_by_id("input_value")
x = find_x.text

num = calc(x)

input_field = browser.find_element_by_id("answer")
input_field.send_keys(num)

button("solve")