from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Inicializa o driver do Chrome
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://web.whatsapp.com") # Abre o WhatsApp Web

    # Espera o usuário escanear o QR Code (aguarda 15 segundos)
print("Aguarde enquanto você escaneia o QR Code no WhatsApp Web...")
time.sleep(15)  # Ajuste o tempo conforme necessário

  
# Ler a planilha do Excel
planilha = pd.read_excel(r'C:\Users\Everson\Desktop\PAMELA\GIT_PROJETOS\Planilha_de_agendamentos.xlsx')  # Substitua pelo caminho do seu arquivo Excel

print(planilha)

for index, row in planilha.iterrows():
    numero = row['numero']
    mensagem = row['mensagem']

# Cria a URL do WhatsApp com o número do telefone
    url = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"

# Navega para a URL
    driver.get(url)

# Aguarda um pouco para garantir que a página carregue completamente
    time.sleep(10)  # Ajuste o tempo conforme necessário

# Pressiona Enter para enviar a mensagem
    input_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p')
    input_box.send_keys(Keys.ENTER)

    time.sleep(5)

    print("Mensagem enviada com sucesso!")


