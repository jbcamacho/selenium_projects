from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner

URL = "https://phptravels.net/"

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox(executable_path="webdrivers/geckodriver")
        cls.driver.implicitly_wait(5)

    def test_login(self) -> None:
        self.driver.get(URL)
        assert 'PHPTRAVELS | Travel Technology Partner - PHPTRAVELS' in self.driver.title
        self.driver.find_element(By.CSS_SELECTOR, "a.theme-btn:nth-child(6)").click()
        assert 'Login - PHPTRAVELS' in self.driver.title
        self.driver.find_element(By.NAME, "email").send_keys("user@phptravels.com")
        self.driver.find_element(By.NAME, "password").send_keys("demouser")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-lg").click()
        assert 'Dashboard - PHPTRAVELS' in self.driver.title

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='9.phptravels_POM/Tests/reports'))