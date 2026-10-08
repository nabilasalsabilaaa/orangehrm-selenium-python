import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config import USERNAME, PASSWORD, PAUSE

def test_nav_admin_flow(driver):
    print("\n--- Memulai Testing Skenario Navigasi Admin ---")
    
    # 1 & 2. Open URL & Set Window Size 
    login_page = LoginPage(driver)
    login_page.open()
    driver.set_window_size(1280, 672)
    print("[OK] 1-2. Open URL dan Set Window Size 1280x672")

    # 3 - 6. Login ke OrangeHRM
    login_page.login(USERNAME, PASSWORD)
    print("[OK] 3-6. Berhasil melakukan Login")

    # 7. Masuk ke Menu Admin
    main_page = MainPage(driver)
    main_page.open_admin_menu()
    print("[OK] 7. Membuka Menu Admin")
    time.sleep(PAUSE)

    # 8 - 15. Navigasi Sub-menu Job (Job Titles, Pay Grades, Employment Status, Work Shifts)
    print("-> Menavigasi Sub-menu Job...")
    main_page.navigate_job_dropdown("Job Titles")
    time.sleep(PAUSE)
    
    main_page.navigate_job_dropdown("Pay Grades")
    time.sleep(PAUSE)

    main_page.navigate_job_dropdown("Employment Status")
    time.sleep(PAUSE)

    main_page.navigate_job_dropdown("Work Shifts")
    time.sleep(PAUSE)

    # 36 - 39. Navigasi Konfigurasi (Email Configuration)
    print("-> Menavigasi Menu Configuration...")
    main_page.navigate_configuration_menu()
    print("[OK] 39. Email Configuration berhasil dibuka")
    
    time.sleep(PAUSE)