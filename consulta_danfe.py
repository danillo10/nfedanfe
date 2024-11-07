from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Caminho completo do ChromeDriver
driver_path = '/usr/local/bin/chromedriver'  # Certifique-se de que o caminho do ChromeDriver está correto
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Acesse o site
url = 'https://meudanfe.com.br/'
driver.get(url)

# Carrega as chaves já baixadas em memória
def carregar_chaves_baixadas(arquivo_ok='nfe_ok.txt'):
    try:
        with open(arquivo_ok, 'r') as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        return set()

# Salva a chave de uma nota baixada com sucesso
def salvar_chave_sucesso(chave, arquivo_ok='nfe_ok.txt'):
    with open(arquivo_ok, 'a') as f:
        f.write(f"{chave}\n")

# Remove as chaves baixadas com sucesso do arquivo nfe.txt
def atualizar_arquivo_chaves(chaves_restantes, arquivo_chaves='nfe.txt'):
    with open(arquivo_chaves, 'w') as f:
        for chave in chaves_restantes:
            f.write(f"{chave}\n")

# Carrega as chaves já baixadas uma vez
chaves_baixadas = carregar_chaves_baixadas()

# Ler o arquivo nfe.txt e processar cada chave
with open('nfe.txt', 'r') as file:
    chaves = file.read().splitlines()

chaves_restantes = chaves[:]  # Cópia das chaves que serão atualizadas no final

for chave in chaves:
    chave_acesso = chave.strip()  # Remove espaços em branco e quebras de linha

    # Verifica se a chave já foi baixada
    if chave_acesso in chaves_baixadas:
        print(f"Chave {chave_acesso} já foi baixada, pulando.")
        continue

    print(f"Processando chave: {chave_acesso}")

    # Insere a chave de acesso
    input_field = driver.find_element(By.XPATH, "//input[@placeholder='Digite a CHAVE DE ACESSO']")
    input_field.clear()  # Limpa o campo antes de inserir uma nova chave
    input_field.send_keys(chave_acesso)

    # Clica no botão "Buscar DANFE/XML"
    search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Buscar DANFE/XML')]")
    search_button.click()

    # Aguarda o redirecionamento e o carregamento da página de resultados
    time.sleep(5)

    try:
        # Tenta clicar no botão "Baixar XML" na página de resultados
        download_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Baixar XML')]")
        download_button.click()

        # Aguarda o download (ou a finalização do carregamento, se necessário)
        time.sleep(5)

        # Salva a chave como baixada com sucesso e atualiza o conjunto em memória
        salvar_chave_sucesso(chave_acesso)
        chaves_baixadas.add(chave_acesso)
        print(f"Chave {chave_acesso} baixada com sucesso.")

        # Remove a chave baixada da lista de chaves restantes
        chaves_restantes.remove(chave_acesso)
        
    except Exception as e:
        print(f"Erro ao baixar a chave {chave_acesso}: {e}")

    # Volta para a página inicial para buscar a próxima chave
    driver.get(url)
    time.sleep(2)  # Aguarda o carregamento da página inicial

# Atualiza o arquivo nfe.txt com as chaves que não foram baixadas
atualizar_arquivo_chaves(chaves_restantes)

# Fecha o navegador após processar todas as chaves
driver.quit()
