from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

random_number = random.randint(1, 1000)
first_name = "Test" + str(random_number)
last_name = "User" + str(random_number)
username = "TestUser" + str(random_number)
id = str(random_number)

def test_create_user(login):
    wait = WebDriverWait(login, 10)
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add Employee']"))).click()

    wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(first_name)
    login.find_element(By.NAME, "lastName").send_keys(last_name)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'oxd-switch-input')]"))).click()
    
    login.find_element(By.XPATH, "(//input[contains(@class, 'oxd-input oxd-input--active')])[6]").send_keys(username)
    
    login.find_element(By.XPATH, "(//input[contains(@class, 'oxd-input oxd-input--active')])[5]").send_keys(id)

    login.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys("Teste123Teste456")
    login.find_element(By.XPATH, "(//input[@type='password'])[2]").send_keys("Teste123Teste456")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    toast = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-text--toast-title")))
    assert "Success" in toast.text, f"Mensagem esperada não encontrada. Texto atual: {toast.text}"

    time.sleep(5)