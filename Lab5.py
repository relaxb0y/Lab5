from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(15)

url = 'https://www.citrus.ua'
search_request = 'IPhone'

driver.get(url)
driver.find_element(By.ID, 'searchStr').send_keys(search_request)
driver.find_element(By.ID, 'searchStr').send_keys(Keys.ENTER)

actualResult = driver.find_element(By.CLASS_NAME, 'searchResults').text
expectedResult = search_request

assert expectedResult in actualResult
driver.close()