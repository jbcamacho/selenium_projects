from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from os import getenv
FIREFOX = 'geckodriver'
CHROME = 'chromedriver'
OPERA = 'operadriver'
PATH =  '/'.join([getenv('HOME'), "webDrivers", FIREFOX])

URL = "https://www.python.org/"
driver = webdriver.Firefox(executable_path=PATH)
driver.get(URL)
assert "Python" in driver.title
elem = driver.find_element(By.XPATH, '//*[@id="id-search-field"]')
elem.clear()
elem.send_keys("ast")
elem.send_keys(Keys.ENTER)
try:
    x_path_ul = '/html/body/div/div[3]/div/section/form/ul'
    content = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(
            (By.XPATH, x_path_ul)
        )
    )
    #content = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/form/ul')
except TimeoutError:
    print('Timeout')
except Exception as e:
    print(f'Error found: {e}')
else:
    list_elements = content.find_elements(By.TAG_NAME, 'h3')
    el = driver.find_element(By.LINK_TEXT)
    for i, li in enumerate(list_elements):
        print(f"Element number {i} \nText:\n{li.text} ")
finally:
    driver.quit()