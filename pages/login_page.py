from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, TIMEOUT

class LoginPage:
    # URL dan Lokator Elemen
    URL = BASE_URL + "/web/index.php/auth/login"
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR = (By.CSS_SELECTOR, ".oxd-alert-content-text")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def open(self):
        """Membuka halaman login dan mengatur ukuran window sesuai log (1280x672)"""
        self.driver.get(self.URL)
        self.driver.set_window_size(1280, 672)
        return self

    def login(self, username, password):
        """Melakukan proses input username, password, dan klik tombol login"""
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()
        return self

    def error_text(self):
        """Mengambil teks pesan error jika login gagal"""
        return self.wait.until(EC.visibility_of_element_located(self.ERROR)).text