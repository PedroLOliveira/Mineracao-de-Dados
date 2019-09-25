import requests
from bs4 import BeautifulSoup
import time

#https://www.youtube.com/watch?v=Bg9r_yLk7VY
def check_results():
    URL = 'https://footballdatabase.com/ranking/'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    linksPaginacao = soup.find(attrs={"pagination pagination-sm"})
    for link in linksPaginacao.findAll("a"):
        URL = 'https://footballdatabase.com' + link["href"]
        print(URL)
        page = requests.get(URL, headers = headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        tabelaDeDados = soup.find(attrs={"table-responsive"})
        for linha in tabelaDeDados.findAll("tr"):
            rank = linha.findAll(attrs={"rank"})
            time = linha.find(attrs={"limittext"})
            pais = linha.find(attrs={"sm_logo-name"})
            if time is not None:
                print(rank[0].get_text() + " - " + time.get_text() + " (" + pais.get_text() + ")" + " ~ " + rank[1].get_text())
            
check_results()
#while(True):
    #check_results()
    #time.sleep(60*60)