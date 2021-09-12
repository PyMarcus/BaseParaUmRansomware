import os 
import shutil

lista_extensoes = [
    '.png', '.jpg', '.jpeg', '.img'
]
lista_arquivos = []
lista_filtro = []

"""def findFile(caminho):
    #Pega o nome do arquivo
    palavras = caminho.split('/') # separa pelas /
    tamanho = len(palavras)
    arquivo = palavras[tamanho - 1]
    return arquivo
"""


class FindDir:
    global lista_arquivos
    global lista_filtro 

    """""""""""""""""""""""""""""""""""""""""""""""""""
    Encontra os arquivos do computador e os criptografa
    """""""""""""""""""""""""""""""""""""""""""""""""""

    def __init__(self, parametro='/home/mvra/Downloads'):
        self.parametro = parametro

    def find_dir(self):
        i = 0
        dic = {}
        listaPaths = list()
        os.chdir(self.parametro)
        path = os.walk(self.parametro)
        caminho = list(path)[0][0] + '/'
        for arquivos in os.listdir(caminho):
            if os.path.isdir(arquivos):
                for caminh in os.listdir(arquivos):
                    if os.path.isdir(arquivos):
                        dic.setdefault(arquivos, caminh)
            elif os.path.isfile(arquivos):
                lista_arquivos.append(arquivos)
        # formando o caminho:
        for file in lista_arquivos:
            listaPaths.append(caminho + file)
        for k, v in dic.items():
            listaPaths.append(caminho + k + '/' + v)
        
        for itens in listaPaths:
            for extensoes in lista_extensoes:
                if extensoes in itens:
                    lista_filtro.append(itens)
        return lista_filtro


if __name__ == '__main__':
    classe = FindDir()
    print(classe.find_dir())
