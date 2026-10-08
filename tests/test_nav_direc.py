import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config import USERNAME, PASSWORD, PAUSE

def test_nav_direc_flow(driver):
    print("\n--- Memulai Testing Skenario Navigasi (Maintenance, Claim, Buzz) ---")
    
    # 1 & 2. Open URL & Set Window Size (1280x672)
    login_page = LoginPage(driver)
    login_page.open()
    driver.set_window_size(1280, 672)
    print("[OK] 1-2. Open URL dan Set Window Size")

    # 3 - 6. Login ke OrangeHRM
    login_page.login(USERNAME, PASSWORD)
    print("[OK] 3-6. Berhasil Login")

    # 7 - 12. Masuk ke menu Maintenance
    main_page = MainPage(driver)

    # 13 - 22. Masuk ke menu Claim dan sub-menu-nya
    print("-> Mengakses menu Claim & Sub-menunya...")
    main_page.go_to_claim_menu()
    main_page.navigate_claim_submenus()
    time.sleep(PAUSE)

    # 23. Masuk ke menu Buzz
    print("-> Mengakses menu Buzz...")
    main_page.go_to_buzz()
    print("[OK] Skenario Navigasi Selesai!")
    
    time.sleep(PAUSE)