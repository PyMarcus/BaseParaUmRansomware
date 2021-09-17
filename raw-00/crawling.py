import requests
from bs4 import BeautifulSoup


def importaKey():
    site = 'https://tiagoemonikytta.blogspot.com/2011/02/e-amor-demais-edson-e-hudson.html?showComment=1631408182059#c7082844546179197379'
    requisicao = requests.get(site)
    bs = BeautifulSoup(requisicao.content, 'html.parser')
    frase = bs.find('p', {'class':'comment-content'}).text
    return frase.encode()

if __name__ == '__main__':
    importaKey()