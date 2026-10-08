from pages.login_page import LoginPage
from pages.main_page import MainPage
from config import USERNAME, PASSWORD

def test_login_valid_credentials(driver):
    LoginPage(driver).open().login(USERNAME, PASSWORD)
    assert MainPage(driver).header_text() == "Dashboard"
    assert driver.title == "OrangeHRM"

def test_login_invalid_credentials(driver):
    page = LoginPage(driver).open()
    page.login("Admin", "salah123")
    assert page.error_text() == "Invalid credentials"

def test_logout_functionality(logged_in):
    MainPage(logged_in).logout()
    assert "auth/login" in logged_in.current_url