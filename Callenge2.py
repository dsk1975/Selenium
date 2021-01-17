from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

path = '../Selenium/chromedriver'
driver = webdriver.Chrome(path)
driver.get('https://wiki.python.org/moin/FrontPage')
searchbox = driver.find_element_by_id('searchinput')
searchbox.clear()
searchbox.send_keys('Beginner')
searchbox.send_keys(Keys.RETURN)
time.sleep(5)

select = Select(driver.find_element_by_xpath('//*/form/div/select'))
select.select_by_value('raw')
time.sleep(5)

driver.close()