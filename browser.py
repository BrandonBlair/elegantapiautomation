import time

from selenium import webdriver

start = time.time()
driver = webdriver.Chrome()
driver.get('http://www.google.com')
print(driver.page_source[:200])

elapsed = time.time() - start
print(f"Browser validation took {elapsed} seconds")
driver.quit()
