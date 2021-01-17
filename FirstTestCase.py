

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

# 1. Initialize browser driver
driver = webdriver.Chrome()
path = '/Users/dmitry/Downloads/chromedriver'
# 2. Open Browser
# 3. Enter URL
driver = Chrome(executable_path = path)
driver.get('https://thetestingworld.com/testings/')
# 4. Maximize Browser
driver.maximize_window()
# Enter data into textbox
driver.find_element_by_name("fld_username").send_keys('helloworld')
driver.find_element_by_xpath("//input[@name='fld_email']").send_keys('dsko1980@gmail.com')
driver.find_element_by_name("fld_password").send_keys("abcd1234")
driver.find_element_by_name("fld_password").send_keys("abcd1234")
driver.find_element_by_name("fld_username").clear()
driver.find_element_by_name("fld_username").send_keys("dsk1980")
driver.find_element_by_name("dob").send_keys("06/11/2020")
driver.find_element_by_name("phone").send_keys("9253079968")
driver.find_element_by_name("address").send_keys("1460 Contra Costa")

# 5.Working on radio button

driver.find_element_by_xpath("//input[@value='home']").click()

# 6.Working on dropdown
obj = Select(driver.find_element_by_name("sex"))
obj.select_by_value("1")
# obj.select_by_index(1)
# obj.select_by_visible_text("Male")

obj = Select(driver.find_element_by_name("country"))
obj.select_by_value("231")
driver.implicitly_wait(10)

obj = Select(driver.find_element_by_id("stateId"))
obj.select_by_visible_text("California")
driver.implicitly_wait(10)

obj = Select(driver.find_element_by_name("city"))
obj.select_by_value("43181")

driver.find_element_by_name("zip").send_keys("94523")

# 7.Working on Checkbox
driver.find_element_by_xpath("//input[@name= 'terms']").click()

# 8.Working on submit button
driver.find_element_by_xpath("//input[@type='submit']").click()

# Working on link
# driver.find_element_by_link_text("Read Detail").click()

# 9.Close Browser
driver.close()