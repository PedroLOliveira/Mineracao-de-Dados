import requests
from bs4 import BeautifulSoup
import time

#https://www.youtube.com/watch?v=Bg9r_yLk7VY
def check_results():
    URL = 'https://www.ogol.com.br/edition.php?id_edicao=80007'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    faseGrupos = ''
    grupos = soup.find(id="edition_table")
    for grupo in grupos.findAll(attrs={"column_300"}):
        faseGrupos += grupo.a.get_text() + " "
        faseGrupos += grupo.a["href"] + "  "

    faseFinal = ''
    for jogo in soup.findAll(attrs={"arvore_cxjogo_new"}):
        resultado=''
        for equipe in jogo.findAll(attrs={"arvore_cxjogo_equipa"}):
            resultado += equipe.find(attrs={"text"}).get_text() + " "
            resultado += equipe.find(attrs={"arvore_cxjogo_equipa_res"}).get_text() + "  "
        faseFinal += resultado + "    "

    print ("Fase de Grupos: " + faseGrupos + " ")
    print ("")
    print ("Fase Final: " + faseFinal + " ")

check_results()
#while(True):
    #check_results()
    #time.sleep(60*60)