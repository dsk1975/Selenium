from selenium import webdriver


path = '../Selenium/chromedriver'
driver = webdriver.Chrome(path)
driver.implicitly_wait(10)
driver.get('http://www.python.org')
myDynamicElement = driver.find_element_by_id('start-shell')

driver.close()

