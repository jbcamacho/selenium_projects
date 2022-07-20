from ..base.base_pageObject import BasePage, WebDriver
from .dashboard_locators import DashboardPageLocators as Locators

class DashboardPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._author_title = driver.find_element(*Locators.AUTHOR_TITLE)
        self._author_meta = driver.find_element(*Locators.AUTHOR_META)

    def is_title_matches(self) -> bool:
        return 'Dashboard - PHPTRAVELS' in self.driver.title

    def is_bio_present(self) -> bool:
        return self._author_title.text and self._author_meta.text