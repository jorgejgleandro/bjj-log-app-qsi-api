from sklearn.metrics import balanced_accuracy_score, recall_score, precision_score, f1_score
from model.modelo import Model

class Avaliador:

    modelo = None

    def define_modelo(self, modelo):
        self.modelo = modelo

    def avalia_modelo(self, X_test, Y_test):
        """ Faz uma predição e avalia o modelo..
        """
        predicoes = self.modelo.realiza_predicao(X_test)
        
        return balanced_accuracy_score(Y_test, predicoes)