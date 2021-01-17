import behave2cucumber
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

path = '../Selenium/chromedriver'
driver = webdriver.Chrome(path)
driver.get('http://jqueryui.com/droppable')
driver.switch_to.frame(0)

action_chains = ActionChains(driver)
source = driver.find_element_by_id('draggable')
target = driver.find_element_by_id('droppable')

action_chains.drag_and_drop_by_offset(source,10,10).perform()
time.sleep(2)
action_chains.drag_and_drop(source, target).perform()
time.sleep(2)

driver.close()


