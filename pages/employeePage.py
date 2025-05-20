from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CreateEmployeePage:
    def __init__(self, driver):
        self.driver = driver

    def create_employee(self, first_name, last_name):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//li[@class= 'oxd-main-menu-item-wrapper'])[2]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class= 'oxd-icon bi-plus oxd-button-icon']"))).click()

        wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(first_name)
        wait.until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(last_name)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        toast = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-text--toast-title")))
        assert "Success" in toast.text, f"Mensagem esperada não encontrada. Texto atual: {toast.text}"
        time.sleep(2)

class DeleteEmployeePage:
    def __init__(self, driver):
        self.driver = driver

    def delete_employee(self, employee_name = "Test User"):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.element_to_be_clickable((By.XPATH, "(//li[@class= 'oxd-main-menu-item-wrapper'])[2]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder= 'Type for hints...'])[1]"))).send_keys(employee_name)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'oxd-autocomplete-option'])[1]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button']//i[@class='oxd-icon bi-trash']"))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class= 'oxd-icon bi-trash oxd-button-icon']"))).click()

        toast = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-text--toast-title")))
        assert "Success" in toast.text, f"Mensagem esperada não encontrada. Texto atual: {toast.text}" 
        time.sleep(2)