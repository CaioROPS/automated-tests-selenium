from pages.loginPage import LoginPage
from pages.employeePage import CreateEmployeePage
from pages.userPage import CreateUserPage

def test_create_employee(driver):
    login_page = LoginPage(driver)
    login_page.login(username="Admin", password="admin123")

    create_employee_page = CreateEmployeePage(driver)
    create_employee_page.create_employee(first_name="Teste", last_name="QA")

def test_create_user(driver):
    login_page = LoginPage(driver)
    login_page.login(username="Admin", password="admin123")

    create_user_page = CreateUserPage(driver)
    create_user_page.create_user(username="Automation", employee_name="Teste QA", password="Teste123Teste456", confirm_password="Teste123Teste456")