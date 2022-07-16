# This is a sample Python script.

#instalando as bibliotecas

import pandas as pd
import requests  # acessar sites
from bs4 import BeautifulSoup  # organiza as informacoes da internet
import matplotlib.pyplot as plt


# vamos acessar um site usando python

# defina o url

url = 'https://coinmarketcap.com/'

#requisicao - acessar o site

webpage = requests.get(url=url)

# ve a pag da internet
pagina = BeautifulSoup(webpage.text, 'html.parser')

# pegar a tabela com as criptomoedas

tabela = pagina.find('table',attrs={'class': 'h7vnx2-2 czTsgW cmc-table'}).find_all('a',attrs={'class': 'cmc-link'})
print(tabela)



























