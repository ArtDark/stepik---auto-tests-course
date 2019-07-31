from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def button():
    button = browser.find_element_by_tag_name("button")
    button.click()

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


find_x = browser.find_element_by_id("input_value")
x = find_x.text

num = calc(x)

input_field = browser.find_element_by_id("answer")
input_field.send_keys(num)

button()