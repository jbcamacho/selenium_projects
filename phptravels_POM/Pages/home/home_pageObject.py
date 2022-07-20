from ..base.base_pageObject import BasePage, WebDriver
from .home_locators import HomePageLocators as Locators

class HomePage(BasePage):
    
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._btn_login = driver.find_element(*Locators.BTN_LOGIN)

    def is_title_matches(self) -> bool:
        return 'PHPTRAVELS | Travel Technology Partner - PHPTRAVELS' in self.driver.title

    def click_login_btn(self) -> None:
        self._btn_login.click()