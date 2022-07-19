from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from os import getenv
import unittest
import HtmlTestRunner



FIREFOX = 'geckodriver'
CHROME = 'chromedriver'
OPERA = 'operadriver'
PATH =  '/'.join([getenv('HOME'), "webDrivers", FIREFOX])
URL = 'https://duckduckgo.com'

class DuckGoSearch(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Firefox(executable_path=PATH)
        # cls.driver.implicitly_wait(1)
        # cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get(URL)
        txtSearchBox = self.driver.find_element(By.NAME, 'q')
        txtSearchBox.send_keys('Im searching in DuckduckGo')
        txtSearchBox.send_keys(Keys.ENTER)

    def test_search_webdriver(self):
        self.driver.get(URL)
        txtSearchBox = self.driver.find_element(By.NAME, 'q')
        txtSearchBox.send_keys('Selenium WebDriver')
        txtSearchBox.send_keys(Keys.ENTER)

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
        print('Completed')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='DuckGoSearch/reports'))



