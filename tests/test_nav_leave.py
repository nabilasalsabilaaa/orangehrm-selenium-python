import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config import USERNAME, PASSWORD, PAUSE

def test_nav_leave_flow(driver):
    print("\n--- Memulai Testing Skenario Navigasi Leave ---")
    
    # 1 & 2. Open URL & Set Window Size (1280x672)
    login_page = LoginPage(driver)
    login_page.open()
    driver.set_window_size(1280, 672)
    print("[OK] 1-2. Open URL dan Set Window Size 1280x672")

    # 3 - 6. Login ke OrangeHRM
    login_page.login(USERNAME, PASSWORD)
    print("[OK] 3-6. Berhasil Melakukan Login")

    # 7 - 12. Hover/Lintasi Admin & PIM sebentar, lalu Klik Menu Leave (sesuai log)
    main_page = MainPage(driver)
    print("-> Mengakses menu Leave...")
    main_page.go_to_leave()
    time.sleep(PAUSE)

    # 13 - 32. Menavigasi seluruh sub-menu Leave secara berurutan
    print("-> Menavigasi sub-menu Leave (Apply hingga Assign Leave)...")
    main_page.navigate_leave_submenus()
    print("[OK] Skenario Navigasi Leave Selesai Berjalan!")
    
    time.sleep(PAUSE)