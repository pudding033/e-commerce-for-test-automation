from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Cấu hình webdriver
driver = webdriver.Chrome()

# Truy cập trang web có progress bar
driver.get("https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html")

start_button = driver.find_element(By.ID, "cricle-btn")
start_button.click()

wait = WebDriverWait(driver, 30)

try:
    while True:
        progress_element = driver.find_element(By.CLASS_NAME, "percenttext")
        percent = progress_element.text
        print(f"Tiến trình: {percent}")
        if percent == "100%":
            print("Hoàn tất!")
            break
        time.sleep(0.5)
except Exception as e:
    print("Có lỗi xảy ra:", e)

# Đóng trình duyệt
driver.quit()
