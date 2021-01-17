from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


path = '../Selenium/chromedriver'
driver = webdriver.Chrome(path)
driver.get("http://python.org")

search = driver.find_element_by_name('q')
search.clear()
search.send_keys("pycon")
search.send_keys(Keys.RETURN)
time.sleep(4)

driver.close()




