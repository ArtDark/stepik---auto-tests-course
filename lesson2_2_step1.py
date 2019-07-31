from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)


num1 = browser.find_element_by_id("num1")
num1 = num1.text


num2 = browser.find_element_by_id("num2")
num2 = num2.text

control_sum = int(num1) + int(num2)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(control_sum))

send_button = browser.find_element_by_css_selector("button.btn.btn-default")
send_button.click()
