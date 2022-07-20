from selenium.webdriver.common.by import By

class LoginPageLocators():
    BTN_LOGIN = (By.CSS_SELECTOR, ".btn-lg")
    TXT_EMAIL = (By.NAME, "email")
    TXT_PASSWORD = (By.NAME, "password")