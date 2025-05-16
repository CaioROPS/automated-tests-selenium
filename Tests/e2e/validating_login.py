from pages.loginPage import LoginPage

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.login(username="Admin", password="admin123")
    assert "dashboard" in driver.current_url.lower() or "orangehrm" in driver.title.lower()

def test_login_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.login(username="InvalidUser", password="admin123")
    assert "Invalid credentials" in driver.page_source

def test_login_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.login(username="Admin", password="InvalidPassword")
    assert "Invalid credentials" in driver.page_source