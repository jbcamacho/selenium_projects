from selenium.webdriver import Firefox
from typing import Type

WebDriver = Type[Firefox]

class BasePage():
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver