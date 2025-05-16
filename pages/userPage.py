from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CreateUserPage:
    def __init__(self, driver):
        self.driver = driver

    def create_user(self, username= "Automation", employee_name= "Test User", password= "Teste123Teste456", confirm_password= "Teste123Teste456"):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.element_to_be_clickable((By.XPATH, "(//li[@class= 'oxd-main-menu-item-wrapper'])[1]"))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button > .oxd-icon"))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'oxd-select-text oxd-select-text--active'])[1]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'oxd-select-option'])[2]"))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder= 'Type for hints...']"))).send_keys(employee_name)
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class= 'oxd-autocomplete-option'])[1]"))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'oxd-select-text oxd-select-text--active'])[2]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'oxd-select-option'])[2]"))).click()

        wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@class= 'oxd-input oxd-input--active'])[2]"))).send_keys(username)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//input[(@type= 'password')])[1]"))).send_keys(password)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//input[(@type= 'password')])[2]"))).send_keys(confirm_password)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        toast = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-text--toast-title")))
        assert "Success" in toast.text, f"Mensagem esperada não encontrada. Texto atual: {toast.text}"
        time.sleep(2)

class DeleteUserPage:
    def __init__(self, driver):
        self.driver = driver

    def delete_user(self, username= "Automation"):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.element_to_be_clickable((By.XPATH, "(//li[@class= 'oxd-main-menu-item-wrapper'])[1]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@class, 'oxd-input oxd-input--active')])[2]"))).send_keys(username)
        
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        time.sleep(2)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button']//i[@class='oxd-icon bi-trash']"))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class= 'oxd-icon bi-trash oxd-button-icon']"))).click()

        toast = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-text--toast-title")))
        assert "Success" in toast.text, f"Mensagem esperada não encontrada. Texto atual: {toast.text}" 
        time.sleep(2)  