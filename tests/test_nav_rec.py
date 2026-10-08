import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config import USERNAME, PASSWORD, PAUSE

def test_nav_rec_flow(driver):
    print("\n--- Memulai Testing Skenario Navigasi Recruitment ---")
    
    # 1 & 2. Open URL & Set Window Size (1280x672)
    login_page = LoginPage(driver)
    login_page.open()
    driver.set_window_size(1280, 672)
    print("[OK] 1-2. Open URL dan Set Window Size 1280x672")

    # 3 - 7. Login ke OrangeHRM
    login_page.login(USERNAME, PASSWORD)
    print("[OK] 3-7. Berhasil Melakukan Login")

    # 8. Masuk ke Menu Recruitment
    main_page = MainPage(driver)
    print("-> Mengakses menu Recruitment...")
    main_page.go_to_recruitment()
    time.sleep(PAUSE)

    # 9 - 12. Mengakses sub-menu Vacancies
    print("-> Mengakses sub-menu Vacancies...")
    main_page.navigate_recruitment_submenus()
    print("[OK] Skenario Navigasi Recruitment Selesai Berjalan!")
    
    time.sleep(PAUSE)