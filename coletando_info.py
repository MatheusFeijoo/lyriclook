from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest
import re
import string



def pega(artista, musica):

    texto1temp = artista.lower()
    texto2temp = musica.lower()
    
    texto1 = texto1temp.replace(" ","-")
    texto2 = texto2temp.replace(" ","-")

    
    url = 'https://www.vagalume.com.br/'+ texto1 +'/'+ texto2 +'.html'

    link = Request(url,headers={'User-Agent': 'Mozilla/5.0'})

    pagina = urlopen(link).read().decode('utf-8', 'ignore')

    soup = BeautifulSoup(pagina, "lxml")
    texto = soup.find(id="lyrics")
    text = texto.get_text(separator="\n")
    return text