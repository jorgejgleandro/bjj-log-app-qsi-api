import numpy as np
import joblib
from model.preprocessador import PreProcessador

class Model:

    path = ''
    
    def __init__(self, path:str):
        """
        Inicializa Modelo

        Argumentos:
            path: localização do arquivo do modelo no sistema de arquivos.
            X_input: entrada
        """
        self.path = path
    
    def carrega_modelo(self):
        """
           Carrega um pipeline, includindo scaler e modelo
           Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra           
        """
        
        if self.path.endswith('.pkl'):
            with open(self.path, 'rb') as file:
                self.model = joblib.load(file, 'r')
        else:
            raise Exception('Formato de arquivo não suportado')
    
    def realiza_predicao(self, X_input):
        """Realiza a predição de um paciente com base no modelo treinado
        """
        output = int(self.model.predict(X_input)[0])
        return output