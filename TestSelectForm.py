from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("file:/Users/dmitry/Downloads/Ex_Files_Python_Automation_Testing/Exercise Files/CH03/03_02/html_code_03_02.html")
select = Select(driver.find_element_by_name("numReturnSelect"))
select.select_by_index(4)
time.sleep(2)
select.select_by_visible_text("200")
time.sleep(2)
select.select_by_value("250")
time.sleep(2)

option = select.options
print(option)


submit_button = driver.find_element_by_name('continue')
submit_button.submit()
time.sleep(2)

driver.close()
