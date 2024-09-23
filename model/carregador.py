import pandas as pd

class Carregador:

    dados = ''

    def carregar_dados(self, url: str, atributos: list):
        """ Carrega e devolve um DataFrame. 
        """        
        self.dados = pd.read_csv(url, names=atributos, header=0, skiprows=0, delimiter=',')

    def pegar_dados(self):
        return self.dados
    