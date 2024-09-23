from model import *

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_X_dados = "./MachineLearning/data/X_test_dataset_heart.csv"
url_Y_dados = "./MachineLearning/data/Y_test_dataset_heart.csv"

colunas_x = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs','restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall']
colunas_y = ['output']

# Carga dos dados
X = carregador.carregar_dados(url_X_dados, colunas_x).values
Y = carregador.carregar_dados(url_Y_dados, colunas_y).values

    
# Método para testar o melhor modelo de Regressão Logística a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_modelo_best():  
    # Importando o modelo de regressão logística
    model_path = './MachineLearning/models/final_best_model_heart.pkl'
    modelo_best = Model()
    modelo_best.define_caminho(model_path)
    modelo_best.carrega_modelo()

    # Obtendo as métricas da Regressão Logística
    avaliador = Avaliador()
    avaliador.define_modelo(modelo_best)
    acuracia_best = avaliador.avalia_modelo(X, Y)
    
    # Testando as métricas da Regressão Logística 
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_best >= 0.78 
    # assert recall_lr >= 0.5 
    # assert precisao_lr >= 0.5 
    # assert f1_lr >= 0.5 
 
# # Método para testar modelo KNN a partir do arquivo correspondente
# def test_modelo_knn():
#     # Importando modelo de KNN
#     knn_path = './MachineLearning/models/diabetes_knn.pkl'
#     modelo_knn = Model.carrega_modelo(knn_path)

#     # Obtendo as métricas do KNN
#     acuracia_knn = Avaliador.avaliar(modelo_knn, X, y)
    
#     # Testando as métricas do KNN
#     # Modifique as métricas de acordo com seus requisitos
#     assert acuracia_knn >= 0.78
#     # assert recall_knn >= 0.5 
#     # assert precisao_knn >= 0.5 
#     # assert f1_knn >= 0.5 
    
# # Método para testar pipeline Random Forest a partir do arquivo correspondente
# def test_modelo_rf():
#     # Importando pipeline de Random Forest
#     rf_path = './MachineLearning/pipelines/rf_diabetes_pipeline.pkl'
#     modelo_rf = Pipeline.carrega_pipeline(rf_path)

#     # Obtendo as métricas do Random Forest
#     acuracia_rf = Avaliador.avaliar(modelo_rf, X, y)
    
#     # Testando as métricas do Random Forest
#     # Modifique as métricas de acordo com seus requisitos
#     assert acuracia_rf >= 0.78
#     # assert recall_rf >= 0.5 
#     # assert precisao_rf >= 0.5 
#     # assert f1_rf >= 0.5