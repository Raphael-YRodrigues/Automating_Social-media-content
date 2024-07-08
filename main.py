from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import pyautogui as pygui
import csv

# Configurações do driver e inicialização
def initiate_driver():
    chrome_options = Options() 
    arguments = ['--lang=en', '--window-size=1000,780', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    # Configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Desabilitar confirmação de dowload
        'dowload.prompt_for_dowload': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos dowloads
        'profile.default_content_setting_values.automatic_dowloads': 1
    })
    
    # Inicializa o Webdriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

# Randomizar a velocidade de digitação
def natural_text(text,element):
    for character in text:
        element.send_keys(character)
        sleep(random.randint(1,5)/30)

# Opens chat gpt and copies text
def prompting_chatgpt():
    pygui.press("Win")
    sleep(1)
    pygui.write("Chrome")
    sleep(1)
    pygui.press("Enter")
    sleep(10)
    pygui.hotkey("ctrl", "shift", "n")
    sleep(5)
    pygui.write("https://chatgpt.com/")
    sleep(1)
    pygui.press("Enter")
    sleep(5)
    pygui.press("f11")
    sleep(5)
    pygui.write(prompt)
    sleep(1)
    pygui.press("Enter")
    sleep(15)
    pygui.hotkey("ctrl", "shift", "c")
    sleep(1)
    pygui.press("f11")
    sleep(1)
    pygui.hotkey("ctrl", "w")
    sleep(1)
    pygui.hotkey("ctrl", "w")

# Read credentials from CSV file
def get_credentials_from_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        credentials = next(csv_reader)
        return credentials['email'], credentials['password']
csv_file_path = 'credentials.csv'
# Get the email and password from the CSV file
email, password = get_credentials_from_csv(csv_file_path)

# Inicia o driver
driver = initiate_driver()

# Define o prompt
prompt = "Write a single inpirational quote about 'automation'. Be playful, informal and fun and do not add any other line of text besides the quote. Escreva em portugues-br"

# Executa o script para copiar o texto do chat gpt
prompting_chatgpt()

# Navega para uma URL
driver.get("https://www.linkedin.com/login/pt")

# Preenche o campo de email
email_camp = driver.find_element(By.ID, "username")
natural_text(email, email_camp)

# Preenche o campo de senha
password_camp = driver.find_element(By.ID, "password")
natural_text(password, password_camp)

sleep(1)
# Clica no botão de Entrar
login_button = driver.find_element(By.XPATH, "//button[@class='btn__primary--large from__button--floating']")
driver.execute_script('arguments[0].click()', login_button)

sleep(10)
# Campo publicação na página inicial
post_camp_button = driver.find_element(
    By.XPATH, "//*[@class='artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view share-box-feed-entry__trigger']")
driver.execute_script('arguments[0].click()', post_camp_button)

sleep(5)
# Clica para digitar e digita o texto da publicação
post_camp = driver.find_element(By.XPATH, "//*[@class='ql-editor ql-blank']")
pygui.hotkey("ctrl", "v")

sleep(1)
# Clica em publicar
post_button = driver.find_element(
    By.XPATH, "//*[@class='share-actions__primary-action artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")
driver.execute_script('arguments[0].click()', post_button)


input("")
driver.close()