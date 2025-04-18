from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://cellphones.com.vn")

# Tìm theo XPath
element = driver.find_element(By.XPATH, '//*[@id="box-content"]/div[2]/a')
print(element.text)