from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_create_employee(login, user_data):
    wait = WebDriverWait(login, 10)
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//li[@class= 'oxd-main-menu-item-wrapper'])[2]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class= 'oxd-icon bi-plus oxd-button-icon']"))).click()

    wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(user_data["first_name"])
    wait.until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys(user_data["last_name"])

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    toast = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-text--toast-title")))
    assert "Success" in toast.text, f"Mensagem esperada não encontrada. Texto atual: {toast.text}"

    time.sleep(2)

def test_create_user(login, user_data):
    wait = WebDriverWait(login, 10)
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//li[@class= 'oxd-main-menu-item-wrapper'])[1]"))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button > .oxd-icon"))).click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'oxd-select-text oxd-select-text--active'])[1]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'oxd-select-option'])[2]"))).click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder= 'Type for hints...']"))).send_keys("Test User")
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class= 'oxd-autocomplete-option'])[1]"))).click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'oxd-select-text oxd-select-text--active'])[2]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'oxd-select-option'])[2]"))).click()

    WebDriverWait(login, 5).until(EC.presence_of_element_located((By.XPATH, "(//input[@class= 'oxd-input oxd-input--active'])[2]"))).send_keys(user_data["username"])
    login.find_element(By.XPATH, "(//input[(@type= 'password')])[1]").send_keys("Teste123Teste456")
    login.find_element(By.XPATH, "(//input[(@type= 'password')])[2]").send_keys("Teste123Teste456")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    toast = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-text--toast-title")))
    assert "Success" in toast.text, f"Mensagem esperada não encontrada. Texto atual: {toast.text}"

    time.sleep(2)

def test_delete_user(login, user_data):
    wait = WebDriverWait(login, 10)
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//li[@class= 'oxd-main-menu-item-wrapper'])[1]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@class, 'oxd-input oxd-input--active')])[2]"))).send_keys(user_data["username"])
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button']//i[@class='oxd-icon bi-trash']"))).click()

    WebDriverWait(login, 5).until(EC.element_to_be_clickable((By.XPATH, "//i[@class= 'oxd-icon bi-trash oxd-button-icon']"))).click()

    toast = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-text--toast-title")))
    assert "Success" in toast.text, f"Mensagem esperada não encontrada. Texto atual: {toast.text}" 

    time.sleep(2)

def test_delete_employee(login):
    wait = WebDriverWait(login, 10)
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//li[@class= 'oxd-main-menu-item-wrapper'])[2]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder= 'Type for hints...'])[1]"))).send_keys("Test User")
    WebDriverWait(login, 5).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'oxd-autocomplete-option'])[1]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button']//i[@class='oxd-icon bi-trash']"))).click()

    WebDriverWait(login, 5).until(EC.element_to_be_clickable((By.XPATH, "//i[@class= 'oxd-icon bi-trash oxd-button-icon']"))).click()

    toast = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-text--toast-title")))
    assert "Success" in toast.text, f"Mensagem esperada não encontrada. Texto atual: {toast.text}" 

    time.sleep(2)