from selenium import webdriver
import math

# math function
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#open browser and go to link    
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

# find x number
find_x = browser.find_element_by_id("input_value")
x = find_x.text

# calculate x number in to function
num = calc(x)

input_string = browser.find_element_by_id("answer")
input_string.send_keys(num)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)





check_box = browser.find_element_by_id("robotCheckbox")
check_box.click()

check_button = browser.find_element_by_id("robotsRule")
check_button.click()




button.click()

