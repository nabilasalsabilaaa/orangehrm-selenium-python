import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config import USERNAME, PASSWORD, PAUSE

def test_nav_time_flow(driver):
    print("\n--- Memulai Testing Skenario Navigasi Time ---")
    
    # 1 & 2. Open URL & Set Window Size (1280x672)
    login_page = LoginPage(driver)
    login_page.open()
    driver.set_window_size(1280, 672)
    print("[OK] 1-2. Open URL dan Set Window Size 1280x672")

    # 3 - 7. Login ke OrangeHRM
    login_page.login(USERNAME, PASSWORD)
    print("[OK] 3-7. Berhasil Melakukan Login")

    # 8. Masuk ke Menu Time
    main_page = MainPage(driver)
    print("-> Mengakses menu Time...")
    main_page.go_to_time()
    time.sleep(PAUSE)

    # 9 - 31. Menavigasi seluruh sub-menu Time secara berurutan
    print("-> Menavigasi sub-menu Time (Timesheets hingga Projects)...")
    main_page.navigate_time_submenus()
    print("[OK] Skenario Navigasi Time Selesai Berjalan!")
    
    time.sleep(PAUSE)