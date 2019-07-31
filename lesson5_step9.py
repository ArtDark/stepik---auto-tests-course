from selenium import webdriver

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element_by_id("input_value")
x = x_element.text

y = calc(x)

input_string = browser.find_element_by_id("answer")
input_string.send_keys(y)

check_box = browser.find_element_by_id("robotCheckbox")
check_box.click()

check_button = browser.find_element_by_id("robotsRule")
check_button.click()



send_button = browser.find_element_by_css_selector("button.btn.btn-default")
send_button.click()

