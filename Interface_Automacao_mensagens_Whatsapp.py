import customtkinter

# Criar e configurar a janela 
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x150") # definindo o tamanho da janela


# Criar os botoes, textos e outros elementos
titulo = customtkinter.CTkLabel(janela, text="Automação do Whatsapp", font=("",20)) # "" usando a fonte padrao, 20 tamanho do pixel
texto_botão = customtkinter.CTkLabel(janela, text="Pressione o botão para disparar as mensages:")

def Executar_automacao():
    print("Executando..")

    # script1.py (Python 3)
    #with open(r"C:\Users\Everson\Desktop\PAMELA\GIT_PROJETOS\Automacao_mensagens_Whatsapp.py") as f:
    #    code = f.read()
    #    exec(code)
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    import time
    import pandas as pd
    import urllib.parse  # Import para URL encoding

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
        mensagem_cod1 = f"{mensagem}"
        mensagem_codificada = urllib.parse.quote(mensagem_cod1)

    # Cria a URL do WhatsApp com o número do telefone
        url = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem_codificada}"

    # Navega para a URL
        driver.get(url)

    # Aguarda um pouco para garantir que a página carregue completamente
        time.sleep(10)  # Ajuste o tempo conforme necessário

    # Pressiona Enter para enviar a mensagem
        input_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p')
        input_box.send_keys(Keys.ENTER)

        time.sleep(5)

        print("Mensagem enviada com sucesso!")


    




















botao_executar = customtkinter.CTkButton(janela, text="Iniciar", command=Executar_automacao)

# Colocar todos os elementos na tela 
titulo.pack(padx=10, pady=10)
texto_botão.pack(padx=10, pady=10)
botao_executar.pack(padx=10, pady=10)


janela.mainloop()