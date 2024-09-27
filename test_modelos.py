from model import *
import pytest
import pathlib

# Para executar digite no terminal, dentro do ambiente: pytest -v test_modelos.py

# Instanciação das Classes
carregadorX = Carregador()
carregadorY = Carregador()
modelo = Model()
avaliador = Avaliador()

# Rótulos das Características
colunas_x = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs','restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall']
colunas_y = ['output']

# Dados
url_X_dados = "./MachineLearning/data/X_test_dataset_heart.csv"
url_Y_dados = "./MachineLearning/data/y_test_dataset_heart.csv"

# Carga dos dados
carregadorX.carregar_dados(url_X_dados, colunas_x)
X = carregadorX.pegar_dados()

carregadorY.carregar_dados(url_Y_dados, colunas_y)
Y = carregadorY.pegar_dados()

# Parâmetros para teste
limiar = 0.83
models_paths = pathlib.Path('./MachineLearning/models/')
models_files = models_paths.glob("*.pkl")
models_list = [(str(model_file), limiar) for model_file in models_files]

# Método para testar iterativamente todos os modelos treinados no diretório modelos
# O nome do método a ser testado necessita começar com "test_"

@pytest.mark.parametrize("model_path, expected", models_list)
def test_models(model_path, expected):
    # Importando o modelo
    modelo = Model()
    modelo.define_caminho(model_path)
    modelo.carrega_modelo()

    # Obtendo as métricas da Regressão Logística
    avaliador = Avaliador()
    avaliador.define_modelo(modelo)
    acuracia = avaliador.avalia_modelo(X, Y)
    assert acuracia >= expected