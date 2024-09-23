from model import *
import pytest
import pathlib

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregadorX = Carregador()
carregadorY = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_X_dados = "./MachineLearning/data/X_test_dataset_heart.csv"
url_Y_dados = "./MachineLearning/data/y_test_dataset_heart.csv"

colunas_x = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs','restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall']
colunas_y = ['output']

# Carga dos dados
carregadorX.carregar_dados(url_X_dados, colunas_x)
X = carregadorX.pegar_dados()

carregadorY.carregar_dados(url_Y_dados, colunas_y)
Y = carregadorY.pegar_dados()
    
limiar = 0.83
models_paths = pathlib.Path('./MachineLearning/models/')
models_paths_files = models_paths.glob("*.pkl")
models_paths_list = [(str(model_path), limiar) for model_path in models_paths_files]

# Método para testar iterativamente todos os modelos treinados no diretório modelos
# O nome do método a ser testado necessita começar com "test_"

@pytest.mark.parametrize("model_path, expected", models_paths_list)
def test_models(model_path, expected):
    # Importando o modelo
    print(model_path)
    modelo = Model()
    modelo.define_caminho(model_path)
    modelo.carrega_modelo()

    # Obtendo as métricas da Regressão Logística
    avaliador = Avaliador()
    avaliador.define_modelo(modelo)
    acuracia = avaliador.avalia_modelo(X, Y)
    assert acuracia >= expected