from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TIMEOUT

class MainPage:
    HEADER = (By.XPATH, "//h6[contains(@class,'oxd-topbar-header-breadcrumb')]")
    PROFILE = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    LOGOUT = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def header_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.HEADER)).text

    def open_menu(self, name):
        locator = (By.XPATH, f"//a[contains(@class,'oxd-main-menu-item')]//span[normalize-space()='{name}']")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    DROPDOWN_JOB = (By.XPATH, "//span[normalize-space()='Job']")
    MENU_JOB_TITLES = (By.XPATH, "//a[normalize-space()='Job Titles']")

    def go_to_job_titles(self):
        """Fungsi untuk mengklik sub-menu Job Titles"""
        job_dropdown = self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_JOB))
        job_dropdown.click()
        
        job_titles_option = self.wait.until(EC.element_to_be_clickable(self.MENU_JOB_TITLES))
        job_titles_option.click()
        return self
    
    USER_DROPDOWN_NAME = (By.CSS_SELECTOR, ".oxd-userdropdown-name")

    def is_user_logged_in(self):
        """Memverifikasi elemen user dropdown muncul (tanda login sukses)"""
        element = self.wait.until(EC.presence_of_element_located(self.USER_DROPDOWN_NAME))
        return element.is_displayed()
    
    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT)).click()
        
    MENU_ADMIN = (By.CSS_SELECTOR, ".oxd-main-menu-item-wrapper:nth-child(1) .oxd-text")
    TOPBAR_JOB = (By.XPATH, "//span[normalize-space()='Job']")
    JOB_TITLES = (By.XPATH, "//a[normalize-space()='Job Titles']")
    PAY_GRADES = (By.XPATH, "//a[normalize-space()='Pay Grades']")
    EMPLOYMENT_STATUS = (By.XPATH, "//a[normalize-space()='Employment Status']")
    WORK_SHIFTS = (By.XPATH, "//a[normalize-space()='Work Shifts']")
    
    TOPBAR_ORGANIZATION = (By.XPATH, "//span[normalize-space()='Organization']")
    TOPBAR_QUALIFICATIONS = (By.XPATH, "//span[normalize-space()='Qualifications']")
    TOPBAR_CONFIG = (By.XPATH, "//span[normalize-space()='Configuration']")
    EMAIL_CONFIG = (By.XPATH, "//a[normalize-space()='Email Configuration']")

    def open_admin_menu(self):
        """Langkah 7: Klik menu Admin"""
        admin_menu = self.wait.until(EC.element_to_be_clickable(self.MENU_ADMIN))
        admin_menu.click()
        return self

    def navigate_job_dropdown(self, option_name):
        """Menangani navigasi di bawah dropdown Job (Job Titles, Pay Grades, dll)"""
        job_tab = self.wait.until(EC.element_to_be_clickable(self.TOPBAR_JOB))
        job_tab.click()
        
        if option_name == "Job Titles":
            self.wait.until(EC.element_to_be_clickable(self.JOB_TITLES)).click()
        elif option_name == "Pay Grades":
            self.wait.until(EC.element_to_be_clickable(self.PAY_GRADES)).click()
        elif option_name == "Employment Status":
            self.wait.until(EC.element_to_be_clickable(self.EMPLOYMENT_STATUS)).click()
        elif option_name == "Work Shifts":
            self.wait.until(EC.element_to_be_clickable(self.WORK_SHIFTS)).click()
        return self

    def navigate_configuration_menu(self):
        """Menangani navigasi ke Configuration -> Email Configuration"""
        config_tab = self.wait.until(EC.element_to_be_clickable(self.TOPBAR_CONFIG))
        config_tab.click()
        email_conf = self.wait.until(EC.element_to_be_clickable(self.EMAIL_CONFIG))
        email_conf.click()
        return self

    MENU_MAINTENANCE = (By.LINK_TEXT, "Maintenance")
    MENU_CLAIM = (By.LINK_TEXT, "Claim")
    MENU_BUZZ = (By.LINK_TEXT, "Buzz")
    
    CLAIM_CONFIG_TAB = (By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item'][normalize-space()='Configuration']")
    EXPENSE_TYPES = (By.LINK_TEXT, "Expense Types")
    MY_CLAIMS = (By.LINK_TEXT, "My Claims")
    ASSIGN_CLAIM = (By.LINK_TEXT, "Assign Claim")

    def go_to_maintenance(self):
        """Scroll dan klik menu Maintenance"""
        self.driver.execute_script("window.scrollTo(0, 300);")
        maintenance = self.wait.until(EC.element_to_be_clickable(self.MENU_MAINTENANCE))
        maintenance.click()
        return self

    def go_to_claim_menu(self):
        """Klik menu Claim"""
        claim = self.wait.until(EC.element_to_be_clickable(self.MENU_CLAIM))
        claim.click()
        return self

    def navigate_claim_submenus(self):
        """Navigasi di dalam menu Claim (Configuration -> Expense Types, My Claims, Assign Claim)"""
        config_tab = self.wait.until(EC.element_to_be_clickable(self.CLAIM_CONFIG_TAB))
        config_tab.click()
        expense_option = self.wait.until(EC.element_to_be_clickable(self.EXPENSE_TYPES))
        expense_option.click()
        
        my_claims = self.wait.until(EC.element_to_be_clickable(self.MY_CLAIMS))
        my_claims.click()

        assign_claim = self.wait.until(EC.element_to_be_clickable(self.ASSIGN_CLAIM))
        assign_claim.click()
        return self

    def go_to_buzz(self):
        """Klik menu Buzz"""
        buzz = self.wait.until(EC.element_to_be_clickable(self.MENU_BUZZ))
        buzz.click()
        return self

    MENU_MY_INFO = (By.LINK_TEXT, "My Info")
    SUB_CONTACT_DETAILS = (By.LINK_TEXT, "Contact Details")
    SUB_EMERGENCY_CONTACTS = (By.LINK_TEXT, "Emergency Contacts")
    SUB_DEPENDENTS = (By.LINK_TEXT, "Dependents")
    SUB_IMMIGRATION = (By.LINK_TEXT, "Immigration")
    SUB_JOB = (By.LINK_TEXT, "Job")
    SUB_SALARY = (By.LINK_TEXT, "Salary")
    SUB_REPORT_TO = (By.LINK_TEXT, "Report-to")
    SUB_PERSONAL_DETAILS = (By.LINK_TEXT, "Personal Details")
    SUB_QUALIFICATIONS = (By.LINK_TEXT, "Qualifications")
    SUB_MEMBERSHIPS = (By.LINK_TEXT, "Memberships")

    def go_to_my_info(self):
        """Klik menu My Info di sidebar"""
        my_info_menu = self.wait.until(EC.element_to_be_clickable(self.MENU_MY_INFO))
        my_info_menu.click()
        return self

    def navigate_my_info_tabs(self):
        """Menavigasi seluruh sub-tab di dalam menu My Info beserta aksi scroll"""
        # 9. Contact Details
        self.wait.until(EC.element_to_be_clickable(self.SUB_CONTACT_DETAILS)).click()
        self.driver.execute_script("window.scrollTo(0, 100);")
        
        # 11. Emergency Contacts
        self.wait.until(EC.element_to_be_clickable(self.SUB_EMERGENCY_CONTACTS)).click()
        
        # 12. Dependents
        self.wait.until(EC.element_to_be_clickable(self.SUB_DEPENDENTS)).click()
        self.driver.execute_script("window.scrollTo(0, 150);")
        
        # 14. Immigration
        self.wait.until(EC.element_to_be_clickable(self.SUB_IMMIGRATION)).click()
        self.driver.execute_script("window.scrollTo(0, 200);")
        
        # 16. Job
        self.wait.until(EC.element_to_be_clickable(self.SUB_JOB)).click()
        
        # 17. Salary
        self.wait.until(EC.element_to_be_clickable(self.SUB_SALARY)).click()
        
        # 18. Report-to
        self.wait.until(EC.element_to_be_clickable(self.SUB_REPORT_TO)).click()
        
        # 19. Personal Details
        self.wait.until(EC.element_to_be_clickable(self.SUB_PERSONAL_DETAILS)).click()
        
        # 21. Qualifications
        self.wait.until(EC.element_to_be_clickable(self.SUB_QUALIFICATIONS)).click()
        self.driver.execute_script("window.scrollTo(0, 250);")
        
        # 23. Memberships
        self.wait.until(EC.element_to_be_clickable(self.SUB_MEMBERSHIPS)).click()
        return self
    
    # Lokator untuk modul Leave & Sub-menunya
    MENU_LEAVE = (By.XPATH, "//span[normalize-space()='Leave']")
    SUB_APPLY = (By.XPATH, "//nav[@class='oxd-topbar-body-nav']//a[normalize-space()='Apply']")
    SUB_MY_LEAVE = (By.XPATH, "//nav[@class='oxd-topbar-body-nav']//a[normalize-space()='My Leave']")
    
    TAB_ENTITLEMENTS = (By.XPATH, "//span[normalize-space()='Entitlements']")
    SUB_EMP_ENTITLEMENTS = (By.XPATH, "//ul[@class='oxd-dropdown-menu']//a[normalize-space()='Employee Entitlements']")
    SUB_MY_ENTITLEMENTS = (By.XPATH, "//ul[@class='oxd-dropdown-menu']//a[normalize-space()='My Entitlements']")
    SUB_MY_LEAVE_USAGE_REPORT = (By.XPATH, "//ul[@class='oxd-dropdown-menu']//a[contains(text(), 'Usage Report')]")
    
    TAB_CONFIGURE = (By.XPATH, "//span[normalize-space()='Configure']")
    SUB_LEAVE_TYPES = (By.XPATH, "//ul[@class='oxd-dropdown-menu']//a[normalize-space()='Leave Types']")
    SUB_WORK_WEEK = (By.XPATH, "//ul[@class='oxd-dropdown-menu']//a[normalize-space()='Work Week']")
    SUB_HOLIDAYS = (By.XPATH, "//ul[@class='oxd-dropdown-menu']//a[normalize-space()='Holidays']")
    
    SUB_LEAVE_LIST = (By.XPATH, "//nav[@class='oxd-topbar-body-nav']//a[normalize-space()='Leave List']")
    SUB_ASSIGN_LEAVE = (By.XPATH, "//nav[@class='oxd-topbar-body-nav']//a[normalize-space()='Assign Leave']")
    
    def go_to_leave(self):
        """Klik menu Leave di sidebar"""
        leave_menu = self.wait.until(EC.element_to_be_clickable(self.MENU_LEAVE))
        leave_menu.click()
        return self
    
    def navigate_leave_submenus(self):
        """Menavigasi seluruh sub-menu dalam modul Leave secara aman"""
        
        # 13. Apply
        self.wait.until(EC.element_to_be_clickable(self.SUB_APPLY)).click()
        
        # 14. My Leave
        self.wait.until(EC.element_to_be_clickable(self.SUB_MY_LEAVE)).click()
        
        # --- Menu Entitlements ---
        entitlements_tab = self.wait.until(EC.element_to_be_clickable(self.TAB_ENTITLEMENTS))
        entitlements_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_EMP_ENTITLEMENTS)).click()
        
        entitlements_tab = self.wait.until(EC.element_to_be_clickable(self.TAB_ENTITLEMENTS))
        entitlements_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_MY_ENTITLEMENTS)).click()
        
        # --- Menu Reports (Tab ke-4) ---
        report_tab = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(4) > .oxd-topbar-body-nav-tab-item")))
        report_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_MY_LEAVE_USAGE_REPORT)).click()
        
        # --- Menu Configure ---
        config_tab = self.wait.until(EC.element_to_be_clickable(self.TAB_CONFIGURE))
        config_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_LEAVE_TYPES)).click()
        
        config_tab = self.wait.until(EC.element_to_be_clickable(self.TAB_CONFIGURE))
        config_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_WORK_WEEK)).click()
        
        config_tab = self.wait.until(EC.element_to_be_clickable(self.TAB_CONFIGURE))
        config_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_HOLIDAYS)).click()
        
        # 31. Leave List
        self.wait.until(EC.element_to_be_clickable(self.SUB_LEAVE_LIST)).click()
        
        # 32. Assign Leave
        self.wait.until(EC.element_to_be_clickable(self.SUB_ASSIGN_LEAVE)).click()
        
        return self
    
    # Lokator Modul Performance & Sub-menunya
    MENU_PERFORMANCE = (By.LINK_TEXT, "Performance")
    PERF_TAB_CONFIGURE = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(1) > .oxd-topbar-body-nav-tab-item")
    SUB_KPIS = (By.LINK_TEXT, "KPIs")
    SUB_TRACKERS = (By.LINK_TEXT, "Trackers")
    PERF_TAB_MANAGE_REVIEWS = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(2) > .oxd-topbar-body-nav-tab-item")
    SUB_MY_REVIEWS = (By.LINK_TEXT, "My Reviews")
    SUB_EMPLOYEE_REVIEWS = (By.LINK_TEXT, "Employee Reviews")
    SUB_MY_TRACKERS = (By.LINK_TEXT, "My Trackers")
    PERF_TAB_REPORT = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(4)")

    def go_to_performance(self):
        """Klik menu Performance di sidebar"""
        perf_menu = self.wait.until(EC.element_to_be_clickable(self.MENU_PERFORMANCE))
        perf_menu.click()
        return self

    def navigate_performance_submenus(self):
        """Menavigasi seluruh sub-menu dalam modul Performance secara berurutan dan aman"""
        
        # 10. Configure -> KPIs
        config_tab = self.wait.until(EC.element_to_be_clickable(self.PERF_TAB_CONFIGURE))
        config_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_KPIS)).click()
        
        # 12. Trackers 
        config_tab = self.wait.until(EC.element_to_be_clickable(self.PERF_TAB_CONFIGURE))
        config_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_TRACKERS)).click()

        # 14. My Reviews
        manage_tab = self.wait.until(EC.element_to_be_clickable(self.PERF_TAB_MANAGE_REVIEWS))
        manage_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_MY_REVIEWS)).click()
        
        # 18. Employee Reviews (Cari ulang tab Manage Reviews)
        manage_tab = self.wait.until(EC.element_to_be_clickable(self.PERF_TAB_MANAGE_REVIEWS))
        manage_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_EMPLOYEE_REVIEWS)).click()
        
        # 19 - 22. My Trackers
        self.wait.until(EC.element_to_be_clickable(self.SUB_MY_TRACKERS)).click()
        
        # 23. Tab Report (Tab ke-4)
        report_tab = self.wait.until(EC.element_to_be_clickable(self.PERF_TAB_REPORT))
        report_tab.click()
        
        return self
    
    # Lokator Modul PIM & Sub-menunya
    MENU_PIM = (By.XPATH, "//span[normalize-space()='PIM']")
    PIM_TAB_CONFIG = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab.--parent > .oxd-topbar-body-nav-tab-item")
    SUB_CUSTOM_FIELDS = (By.LINK_TEXT, "Custom Fields")
    SUB_DATA_IMPORT = (By.LINK_TEXT, "Data Import")
    SUB_REPORTING_METHODS = (By.LINK_TEXT, "Reporting Methods")
    SUB_TERMINATION_REASONS = (By.LINK_TEXT, "Termination Reasons")
    SUB_EMPLOYEE_LIST = (By.LINK_TEXT, "Employee List")
    SUB_ADD_EMPLOYEE = (By.LINK_TEXT, "Add Employee")
    SUB_REPORTS = (By.LINK_TEXT, "Reports")

    def go_to_pim(self):
        """Klik menu PIM di sidebar"""
        pim_menu = self.wait.until(EC.element_to_be_clickable(self.MENU_PIM))
        pim_menu.click()
        return self

    def navigate_pim_submenus(self):
        """Menavigasi seluruh sub-menu dalam modul PIM secara berurutan"""
        # 1. Custom Fields
        config_tab = self.wait.until(EC.element_to_be_clickable(self.PIM_TAB_CONFIG))
        config_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_CUSTOM_FIELDS)).click()
        
        # 2. Data Import (Buka ulang dropdown Configuration)
        config_tab = self.wait.until(EC.element_to_be_clickable(self.PIM_TAB_CONFIG))
        config_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_DATA_IMPORT)).click()
        
        # 3. Reporting Methods (Buka ulang dropdown Configuration)
        config_tab = self.wait.until(EC.element_to_be_clickable(self.PIM_TAB_CONFIG))
        config_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_REPORTING_METHODS)).click()
        
        # 4. Termination Reasons (Buka ulang dropdown Configuration)
        config_tab = self.wait.until(EC.element_to_be_clickable(self.PIM_TAB_CONFIG))
        config_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_TERMINATION_REASONS)).click()

        # Employee List
        self.wait.until(EC.element_to_be_clickable(self.SUB_EMPLOYEE_LIST)).click()
        
        # Add Employee
        self.wait.until(EC.element_to_be_clickable(self.SUB_ADD_EMPLOYEE)).click()
        
        # Reports
        self.wait.until(EC.element_to_be_clickable(self.SUB_REPORTS)).click()
        
        return self
    
    # Lokator Modul Recruitment & Sub-menunya (Berdasarkan indeks ke-5 di sidebar)
    MENU_RECRUITMENT = (By.CSS_SELECTOR, ".oxd-main-menu-item-wrapper:nth-child(5) .oxd-text")
    SUB_VACANCIES = (By.LINK_TEXT, "Vacancies")

    def go_to_recruitment(self):
        """Klik menu Recruitment di sidebar"""
        rec_menu = self.wait.until(EC.element_to_be_clickable(self.MENU_RECRUITMENT))
        rec_menu.click()
        return self

    def navigate_recruitment_submenus(self):
        """Menavigasi sub-menu dalam modul Recruitment (Vacancies)"""
        vacancies_menu = self.wait.until(EC.element_to_be_clickable(self.SUB_VACANCIES))
        vacancies_menu.click()
        return self
    
    # Lokator Modul Time & Sub-menunya
    MENU_TIME = (By.LINK_TEXT, "Time")
    TIME_TAB_TIMESHEETS = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(1) > .oxd-topbar-body-nav-tab-item")
    SUB_MY_TIMESHEETS = (By.LINK_TEXT, "My Timesheets") 
    SUB_EMPLOYEE_TIMESHEETS = (By.LINK_TEXT, "Employee Timesheets")
    TIME_TAB_ATTENDANCE = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(2) > .oxd-topbar-body-nav-tab-item")
    SUB_MY_RECORDS = (By.LINK_TEXT, "My Records")
    SUB_PUNCH_IN_OUT = (By.LINK_TEXT, "Punch In/Out")
    SUB_EMPLOYEE_RECORDS = (By.LINK_TEXT, "Employee Records")
    SUB_ATT_CONFIG = (By.LINK_TEXT, "Configuration")
    TIME_TAB_REPORTS = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(3) > .oxd-topbar-body-nav-tab-item")
    SUB_PROJECT_REPORTS = (By.LINK_TEXT, "Project Reports")
    SUB_EMPLOYEE_REPORTS = (By.LINK_TEXT, "Employee Reports")
    SUB_ATTENDANCE_SUMMARY = (By.LINK_TEXT, "Attendance Summary")
    TIME_TAB_PROJECT_INFO = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(4) > .oxd-topbar-body-nav-tab-item")
    SUB_PROJECTS = (By.LINK_TEXT, "Projects")

    def go_to_time(self):
        """Klik menu Time di sidebar"""
        time_menu = self.wait.until(EC.element_to_be_clickable(self.MENU_TIME))
        time_menu.click()
        return self

    def navigate_time_submenus(self):
        """Menavigasi seluruh sub-menu dalam modul Time secara berurutan"""
        
        # 10. My Timesheets
        ts_tab = self.wait.until(EC.element_to_be_clickable(self.TIME_TAB_TIMESHEETS))
        ts_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_MY_TIMESHEETS)).click()
        
        # 12. Employee Timesheets (Buka ulang dropdown Timesheets)
        ts_tab = self.wait.until(EC.element_to_be_clickable(self.TIME_TAB_TIMESHEETS))
        ts_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_EMPLOYEE_TIMESHEETS)).click()
        
        # 15. My Records
        att_tab = self.wait.until(EC.element_to_be_clickable(self.TIME_TAB_ATTENDANCE))
        att_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_MY_RECORDS)).click()
        
        # 17. Punch In/Out (Buka ulang dropdown Attendance)
        att_tab = self.wait.until(EC.element_to_be_clickable(self.TIME_TAB_ATTENDANCE))
        att_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_PUNCH_IN_OUT)).click()
        
        # 19. Employee Records (Buka ulang dropdown Attendance)
        att_tab = self.wait.until(EC.element_to_be_clickable(self.TIME_TAB_ATTENDANCE))
        att_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_EMPLOYEE_RECORDS)).click()
        
        # 21. Configuration (Buka ulang dropdown Attendance)
        att_tab = self.wait.until(EC.element_to_be_clickable(self.TIME_TAB_ATTENDANCE))
        att_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_ATT_CONFIG)).click()
        
        # 23. Project Reports
        rep_tab = self.wait.until(EC.element_to_be_clickable(self.TIME_TAB_REPORTS))
        rep_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_PROJECT_REPORTS)).click()
        
        # 25. Employee Reports (Buka ulang dropdown Reports)
        rep_tab = self.wait.until(EC.element_to_be_clickable(self.TIME_TAB_REPORTS))
        rep_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_EMPLOYEE_REPORTS)).click()
        
        # 27. Attendance Summary (Buka ulang dropdown Reports)
        rep_tab = self.wait.until(EC.element_to_be_clickable(self.TIME_TAB_REPORTS))
        rep_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_ATTENDANCE_SUMMARY)).click()

        # 31. Projects
        proj_tab = self.wait.until(EC.element_to_be_clickable(self.TIME_TAB_PROJECT_INFO))
        proj_tab.click()
        self.wait.until(EC.element_to_be_clickable(self.SUB_PROJECTS)).click()
        
        return self