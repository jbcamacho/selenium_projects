from ..base.base_pageObject import BasePage, WebDriver
from .login_locators import LoginPageLocators as Locators

class LoginPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._txt_email = driver.find_element(*Locators.TXT_EMAIL)
        self._txt_password = driver.find_element(*Locators.TXT_PASSWORD)
        self._btn_login = driver.find_element(*Locators.BTN_LOGIN)

    @property
    def txt_email(self):
        return self._txt_email.get_attribute("value")

    @txt_email.setter
    def txt_email(self, value):
        self._txt_email.clear()
        self._txt_email.send_keys(value)

    @property
    def txt_password(self):
        return self._txt_password.get_attribute("value")

    @txt_password.setter
    def txt_password(self, value):
        self._txt_password.clear()
        self._txt_password.send_keys(value)

    def is_title_matches(self) -> bool:
        return 'Login - PHPTRAVELS' in self.driver.title

    def click_login_btn(self) -> None:
        self._btn_login.click()