import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config import USERNAME, PASSWORD, PAUSE

def test_nav_info_flow(driver):
    print("\n--- Memulai Testing Skenario Navigasi My Info ---")
    
    # 1 & 2. Open URL & Set Window Size (1280x672)
    login_page = LoginPage(driver)
    login_page.open()
    driver.set_window_size(1280, 672)
    print("[OK] 1-2. Open URL dan Set Window Size 1280x672")

    # 3 - 7. Login ke OrangeHRM
    login_page.login(USERNAME, PASSWORD)
    print("[OK] 3-7. Berhasil Melakukan Login")

    # 8. Masuk ke Menu My Info
    main_page = MainPage(driver)
    print("-> Mengakses menu My Info...")
    main_page.go_to_my_info()
    time.sleep(PAUSE)

    # 9 - 23. Menavigasi seluruh sub-tab profil My Info dengan scrolling
    print("-> Menavigasi sub-tab My Info (Contact Details hingga Memberships)...")
    main_page.navigate_my_info_tabs()
    print("[OK] Skenario Navigasi My Info Selesai Berjalan!")
    
    time.sleep(PAUSE)