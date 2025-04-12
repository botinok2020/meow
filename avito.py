import requests      # Библиотека для отправки запросов
import re
import numpy as np   # Библиотека для матриц, векторов и линала
import pandas as pd  # Библиотека для табличек
import time          # Библиотека для тайм-менеджмента
from bs4 import BeautifulSoup

url = 'https://www.avito.ru/novosibirsk/kvartiry/sdam/na_dlitelnyy_srok'

def datall() -> str:
    response = requests.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")

    idu = []
    id = []
    lol = []

    idu = soup.findAll('div', class_ = 'iva-item-root-Se7z4 photo-slider-slider-ZccM3 iva-item-gallery-nEww5 iva-item-redesign-H4ow9 iva-item-responsive-GCo6h iva-item-xl-QXiZ1 items-item-kllqq items-galleryItem-o_Et0 js-catalog-item-enum')
    for data in idu:
        if data.find('div', itemprop = 'id') is not None:
            id.append(data.text)

    lol = soup.find_all('div')

    nameu = []
    name = []

    nameu = soup.findAll('a', class_ = 'styles-module-root-m3BML styles-module-root_noVisited-HHF0s')
    for data in nameu:
        if data.find('h3', itemprop = 'name') is not None:
            name.append(data.text)

    priceu = []
    price = []

    priceu = soup.findAll('strong', class_ = 'styles-module-root-LEIrw')
    for data in priceu:
        if data.find('span'):
            price.append(data.text)

    ssylkau = []
    ssylka = []

    ssylkau = soup.findAll('a', class_ = 'styles-module-root-m3BML styles-module-root_noVisited-HHF0s')
    for link in ssylkau:
        ssylka.append(link.get('href'))

    print(len(id))
    print(idu)
    # print(str(id[0]))
    # print(str(id[1]))
    # print(str(id[2]))
    print(name[0])
    print(name[1])
    print(name[2])
    print(ssylka[0])
    print(ssylka[1])
    print(ssylka[2])

    photou = []
    photo = []

    photou  = soup.findAll('img', class_ = 'photo-slider-image-xjG6U')
    for item in photou:
        photo.append(item.get('src'))

    baba = []
    baba.append(name[0])
    baba.append(price[0])
    baba.append(ssylka[1])

    a = ('Имя: %s \n' % str(baba[0]) + 'Цена: %s \n' % str(baba[1]) + 'Ссылка: https://www.avito.ru%s \n' % str(baba[2]))

    return a
