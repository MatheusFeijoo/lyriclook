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
import regex as re


def remove_punctuation(text):
    punctuations = '''!()-[];:'",.?#$%^&*_~'''
    no_punct = ""
    for char in text:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct


def pega(artist, music):

    texto1low = artist.lower()
    texto2low = music.lower()
    
    texto1temp = remove_punctuation(texto1low)
    texto2temp = remove_punctuation(texto2low)

    texto1 = texto1temp.replace(" ","-")
    texto2 = texto2temp.replace(" ","-")

    url = 'https://www.vagalume.com.br/'+ texto1 +'/'+ texto2 +'.html'
    print(url)

    link = Request(url,headers={'User-Agent': 'Mozilla/5.0'})

    pagina = urlopen(link).read().decode('utf-8', 'ignore')

    soup = BeautifulSoup(pagina, "lxml")
    texto = soup.find(id="lyrics")
    text = texto.get_text(separator="\n")
    
    with open("savedData.txt", "a") as f:
        f.write(texto1 + ',' + texto2 + ',' + url + '\n') 
        f.close() 
    
    return text


print("Search is working")
    