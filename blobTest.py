from os import link
import requests  as re
from bs4 import BeautifulSoup
import os
url = 'https://www.vipleiloes.com.br/Veiculos/DetalharVeiculo/ca4db281-aeb2-43aa-b933-2b8ace491d65'
site = re.get(url)
soup = BeautifulSoup(site.content, 'html.parser')
fotos = soup.find('img',class_="dtp-imgactive")['src']
with open(fotos.replace(' ','-').replace('/',','), 'wb')as f:
    img=re.get(fotos)
    f.write(img.content)
print(fotos)
print('terminado')