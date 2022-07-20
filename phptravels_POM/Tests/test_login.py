from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner
from ..Pages.home.home_pageObject import HomePage
from ..Pages.login.login_pageObect import LoginPage
from ..Pages.dashboard.dashboard_pageObject import DashboardPage
import time

URL = "https://phptravels.net/"

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox(executable_path="webdrivers/geckodriver")
        cls.driver.implicitly_wait(10)

    def test_login_valid(self) -> None:
        driver = self.driver
        driver.get(URL)
        home_page = HomePage(driver)
        self.assertTrue(home_page.is_title_matches())
        home_page.click_login_btn()

        login_page = LoginPage(driver)
        self.assertTrue(login_page.is_title_matches())
        login_page.txt_email = "user@phptravels.com"
        login_page.txt_password = "demouser"
        login_page.click_login_btn()

        dashboard_page = DashboardPage(driver)
        self.assertTrue(dashboard_page.is_title_matches())
        self.assertTrue(dashboard_page.is_bio_present())
        time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="phptravels_POM/Tests/reports"))