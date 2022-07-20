from selenium.webdriver.common.by import By

class DashboardPageLocators():
    
    AUTHOR_TITLE = (By.CSS_SELECTOR, ".author__title > strong:nth-child(1)")
    AUTHOR_META = (By.CSS_SELECTOR, ".author__meta")