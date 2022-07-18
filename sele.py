from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from os import getenv
FIREFOX = 'geckodriver'
CHROME = 'chromedriver'
OPERA = 'operadriver'
PATH =  '/'.join([getenv('HOME'), "webDrivers", FIREFOX])

driver = webdriver.Firefox(executable_path=PATH)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("as")
elem.send_keys(Keys.RETURN)
elm_text = '' #driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/form/ul/p') 
print(elm_text)
assert "No results found." not in driver.page_source
#driver.close()