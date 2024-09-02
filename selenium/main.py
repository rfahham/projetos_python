from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

path = os.path.join(os.getcwd(), 'chromedriver')

service = Service(executable_path=path)

driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get('https://www.alura.com.br')

input("Pressione enter para sair")

driver.quit()
