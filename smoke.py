from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait = WebDriverWait(driver, 15)
wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[normalize-space()='Dashboard']")))
print("Login berhasil, title:", driver.title)
driver.quit()