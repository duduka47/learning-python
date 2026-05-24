from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime as dt
import time

driver = webdriver.Chrome()
from selenium.webdriver.chrome.options import Options

options = Options()

# Doesnt closes after finish
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('https://ozh.github.io/cookieclicker/')

language_selection = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "langSelect-PT-BR"))
)
language_selection.click()

time.sleep(5)

cookie = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "bigCookie"))
)

driver.execute_script("document.body.style.zoom='50%'")

# TODO: After 5 mins print to the console the clicks per second
start_minute = dt.datetime.now().minute
start_second = dt.datetime.now().second


# main game automation loop
while True:
    time.sleep(0.01)
    if dt.datetime.now().second % 5:
      available_upgrades = driver.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled')
      while len(available_upgrades) >= 1:
        available_upgrades[-1].click()
        available_upgrades = driver.find_elements(By.CSS_SELECTOR, '.product.unlocked.enabled')

    now = dt.datetime.now()
    if now.minute == start_minute + 5 and now.second() >= start_second:
        driver.find_element(By.ID, 'cookiesPerSecond').text

    cookie.click()