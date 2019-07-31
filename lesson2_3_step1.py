from selenium import webdriver
import os



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link) 

button = browser.find_element_by_tag_name("button")
button.click()



alert = browser.switch_to.alert
alert.accept()



input_name = browser.find_element_by_name("firstname")
input_name.send_keys("Ivan")

input_lname = browser.find_element_by_name("lastname")
input_lname.send_keys("Petrov")

input_email = browser.find_element_by_name("email")
input_email.send_keys("i.petrov@pidor.su")

element = browser.find_element_by_id("file")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)


send_button = browser.find_element_by_tag_name("button")
send_button.click()
