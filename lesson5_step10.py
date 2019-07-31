from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


pic = browser.find_element_by_id("treasure")
num = pic.get_attribute("valuex")


answer = calc(num)

input_string = browser.find_element_by_id("answer")
input_string.send_keys(answer)

check_box = browser.find_element_by_id("robotCheckbox")
check_box.click()

check_button = browser.find_element_by_id("robotsRule")
check_button.click()



send_button = browser.find_element_by_css_selector("button.btn.btn-default")
send_button.click()



