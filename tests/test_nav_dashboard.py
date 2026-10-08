import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config import USERNAME, PASSWORD, PAUSE

def test_log_dashboard_flow(driver):
    print("\n--- Memulai Testing Skenario Log Dashboard ---")
    
    # 1 & 2. Buka URL dan Set Window Size (1280x672)
    login_page = LoginPage(driver)
    login_page.open()
    print("[OK] 1. Open URL & 2. Set Window Size 1280x672")

    # 3, 4, 5, 6, & 7. Masukkan Username, Password, dan Klik Login
    login_page.login(USERNAME, PASSWORD)
    print("[OK] 3-7. Input Credentials & Click Login button")

    # 8. Verifikasi elemen dropdown profil muncul (Tanda sukses)
    main_page = MainPage(driver)
    assert main_page.is_user_logged_in(), "Gagal: Elemen User Dropdown tidak ditemukan!"
    print("[OK] 8. Elemen .oxd-userdropdown-name berhasil ditemukan (Login Sukses)!")

    time.sleep(PAUSE)