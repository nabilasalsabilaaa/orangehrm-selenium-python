import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config import USERNAME, PASSWORD, PAUSE

def test_nav_pim_flow(driver):
    print("\n--- Memulai Testing Skenario Navigasi PIM ---")
    
    # 1 & 2. Open URL & Set Window Size (1280x672)
    login_page = LoginPage(driver)
    login_page.open()
    driver.set_window_size(1280, 672)
    print("[OK] 1-2. Open URL dan Set Window Size 1280x672")

    # 3 - 7. Login ke OrangeHRM
    login_page.login(USERNAME, PASSWORD)
    print("[OK] 3-7. Berhasil Melakukan Login")

    # 8 - 10. Masuk ke Menu PIM
    main_page = MainPage(driver)
    print("-> Mengakses menu PIM...")
    main_page.go_to_pim()
    time.sleep(PAUSE)

    # 13 - 28. Menavigasi seluruh sub-menu konfigurasi dan halaman PIM
    print("-> Menavigasi sub-menu PIM (Configuration hingga Reports)...")
    main_page.navigate_pim_submenus()
    print("[OK] Skenario Navigasi PIM Selesai Berjalan!")
    
    time.sleep(PAUSE)