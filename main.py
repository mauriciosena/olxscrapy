import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

item = input("Digite o que você quer buscar...")
state = "ba"
url = "https://www.olx.com.br/estado-" + state + "?q=" + item
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

response = requests.get(url, headers=headers)

print(response)
soup = BeautifulSoup(response.content, "html.parser")

titles = soup.find_all("h2", class_="kgl1mq-0 eFXRHn sc-ifAKCX iUMNkO")
prices = soup.find_all("span", class_="m7nrfa-0 eJCbzj sc-ifAKCX jViSDP")
link, data = [], []
length = ""

#Pega o link de cada anúncio em tela
for l in soup.findAll('a', {'data-lurker-detail': 'list_id'}):
     link.append(l["href"])

#Pega o link do último anúncio
for l in soup.findAll('a', {'data-lurker-detail': 'last_page'}):
     length = l["href"]

length.replace(url, "")
print(length) #PRECISA REMOVER O VALOR DE O= E FAZER UMA BUSCA RECURSIVA ATÉ O FINAL, CONCATENANDO NO DATAFRAME

#faz append em um array para transformar em dataframe
for i in range(len(titles)):
    data.append({"title": titles[i].text, "price": prices[i].text, "link": link[i]})

df = pd.DataFrame(data)

try:
    os.remove("olx_data.csv")
    df.to_csv("olx_data.csv", index=False)
    print("Arquivo anterior removido e gerado um novo csv!")
except:
    df.to_csv("olx_data.csv", index=False)
    print("Gerado um novo csv!")


def check_search_length():
    pass
