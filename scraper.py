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
    for val in soup.findAll(attrs={"zztable stats"}):
        faseGrupos += val.get_text() + " "

    faseFinal = ''
    for val in soup.findAll(attrs={"arvore_cxjogo_new"}):
        faseFinal += val.get_text() + " "

    print ("Fase de Grupos: " + faseGrupos + " ")
    print ("")
    print ("Fase Final: " + faseFinal + " ")

check_results()
#while(True):
    #check_results()
    #time.sleep(60*60)