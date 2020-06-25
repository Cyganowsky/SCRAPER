import requests 
from bs4 import BeautifulSoup

def my_url():
    URL = 'https://www.ebay.com/itm/Milwaukee-M18-FUEL-NAILER-15G-FNSH-Tool-Only-2743-80-Recon/283208388793?_trkparms=pageci%3Ac0d3201e-b706-11ea-8cb6-74dbd18096af%7Cparentrq%3Aec757c5c1720aa16b7c551c3ffff5dec%7Ciid%3A1'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    page = requests.get(URL, headers=headers)


    soup = BeautifulSoup(page.content, 'html.parser')


    slownik=[]
    
    comp={
        "title": soup.find(id="itemTitle").text,
        "price": soup.find(id="prcIsum").text,
        }
    slownik.append(comp)
    print(slownik) #tylko do wyświetlenia w terminalu 
    return slownik
my_url()
