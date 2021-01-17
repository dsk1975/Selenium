from selenium import webdriver


path = '../Selenium/chromedriver'
driver = webdriver.Chrome(path)
driver.get('http://www.seleniumhq.org')
# element_id = driver.find_element_by_id('q')
# print('element_id')
# element_name = driver.find_element_by_class_name('q')
# print(element_name)
element_Xpath = driver.find_element_by_xpath("//div[contains(@class,'button-container long-section-button')]")
print(element_Xpath)
# element_class = driver.find_element_by_class_name("selenium-sponsors")
# print(element_class)

driver.close()

