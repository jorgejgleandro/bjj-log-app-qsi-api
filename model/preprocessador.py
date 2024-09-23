from sklearn.model_selection import train_test_split
import joblib
import numpy as np

class PreProcessador:

    form = ''

    def define_formulario(self, form):
        self.form = form

    def preparar_form(self):
        """ Prepara os dados recebidos do front para serem usados no modelo. """
        X_input = np.array([self.form.age, 
                            self.form.sex,
                            self.form.cp,
                            self.form.trtbps,
                            self.form.chol,
                            self.form.fbs,
                            self.form.restecg,
                            self.form.thalachh,
                            self.form.exng,
                            self.form.oldpeak,
                            self.form.slp,
                            self.form.caa,
                            self.form.thall
                        ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        X_input = X_input.reshape(1, -1)
        return X_input