import os
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import USERNAME, PASSWORD
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    if os.getenv("HEADLESS") == "1":
        options.add_argument("--headless=new")

    grid_url = os.getenv("GRID_URL")          # kalau diisi -> jalan di Selenium Grid
    if grid_url:
        drv = webdriver.Remote(command_executor=grid_url, options=options)
    else:
        drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()

@pytest.fixture
def logged_in(driver):
    LoginPage(driver).open().login(USERNAME, PASSWORD)
    return driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        drv = item.funcargs.get("driver")
        if drv:
            extras = getattr(report, "extras", [])
            extras.append(pytest_html.extras.png(drv.get_screenshot_as_base64()))
            report.extras = extras