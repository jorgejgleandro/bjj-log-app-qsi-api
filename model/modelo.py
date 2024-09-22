import numpy as np
import joblib
from model.preprocessador import PreProcessador

class Model:
    
    model = ''
    
    def carrega_modelo(self, path):
        """
           Carrega um pipeline, includindo scaler e modelo
           Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra           
        """
        
        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                self.model = joblib.load(file, 'r')
        else:
            raise Exception('Formato de arquivo não suportado')
    
    def realiza_predicao(self, X_input):
        """Realiza a predição de um paciente com base no modelo treinado
        """
        diagnosis = self.model.predict(X_input)
        return diagnosis