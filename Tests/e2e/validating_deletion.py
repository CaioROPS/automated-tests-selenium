from pages.loginPage import LoginPage
from pages.employeePage import DeleteEmployeePage
from pages.userPage import DeleteUserPage

def test_delete_user(driver):
    login_page = LoginPage(driver)
    login_page.login(username="Admin", password="admin123")

    create_user_page = DeleteUserPage(driver)
    create_user_page.delete_user(username="Automation")

def test_delete_employee(driver):
    login_page = LoginPage(driver)
    login_page.login(username="Admin", password="admin123")

    delete_employee_page = DeleteEmployeePage(driver)
    delete_employee_page.delete_employee(employee_name="Teste QA")