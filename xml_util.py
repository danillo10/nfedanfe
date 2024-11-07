from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Caminho completo do ChromeDriver
driver_path = '/usr/local/bin/chromedriver'

# Inicialize o WebDriver usando Service
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Acesse o site
url = 'https://meudanfe.com.br/'
driver.get(url)

# Aguarda a página carregar
time.sleep(2)

# Insira a chave de acesso
chave_acesso = '31240852279212000153550010000010261897822760'  # Substitua pela sua chave de acesso
input_field = driver.find_element(By.XPATH, "//input[@placeholder='Digite a CHAVE DE ACESSO']")
input_field.send_keys(chave_acesso)

# Clique no botão "Buscar DANFE/XML"
search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Buscar DANFE/XML')]")
search_button.click()

# Aguarde o redirecionamento e o carregamento da página de resultados
time.sleep(5)

# Clique no botão "Baixar XML" na página de resultados
download_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Baixar XML')]")
download_button.click()

# Aguarde o download (ou a finalização do carregamento, se necessário)
time.sleep(5)

# Fecha o navegador
driver.quit()
