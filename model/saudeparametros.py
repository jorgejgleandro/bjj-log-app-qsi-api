from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from  model import Base, Comentario

class SaudeParametros(Base):
    __tablename__ = 'saude_parametros'

    id = Column("pk_saude", Integer, primary_key=True)
    aluno_nome = Column(String(140))
    age = Column(Integer)
    sex = Column(String(5))
    cp = Column(Integer)
    trtbps	= Column(Integer)
    chol = Column(Integer)
    fbs	= Column(Integer)
    restecg	= Column(Integer)
    thalachh = Column(Integer)	
    exng = Column(Integer)	
    oldpeak	= Column(Float)
    slp	= Column(Integer)
    caa	= Column(Integer)
    thall= Column(Integer)
    output=Column(Integer, nullable=True)

    def __init__(self, aluno_nome:str, age:int, sex:str, cp:int, trtbps:int, chol:int, fbs:int, restecg:int, thalachh:int,exng:int, oldpeak:float, slp:int, caa:int, thall:int, output:int):
        """
        Registra os parâmetros de saude do coração do aluno

        Argumentos:
            aluno_nome = nome do aluno
            age = idade do aluno
            sex = sexo do aluno
            cp = Chest Pain type (tipo de dor no peito) - (1 = angina típica; 2 = angina átipica; 3 = dor sem angina; 0 = assintomática)
            trtbps	= Resting blood pressure in mmHg - Pressão sanguinea em repouso em mmHg
            chol = Cholestoral in mg/dl fetched via BMI sensor - Colesterol em mg/dl obtido por sensor BMI
            fbs	= Fasting blood sugar > 120 mg/dl - Nível de açúcar no sangue em jejum - (1 = Sim; 0 = Não)
            restecg	= Resting electrocardiographic results - Resultados de eletrocardiograma em repouso - (1 = normal; 2 = anormalidade na onda ST-T; 0 = hipertrofia)
            thalachh = Maximum heart rate achieved - Frequencia cardíaca máxima atingida
            exng = Exercise induced angina - Nível de angina induzida por exercício  - (1 = Sim; 0 = Náo)
            oldpeak	= ST depression induced by exercise relative to rest - Depressão de ST/ECG induzida por 
                      exercício em relação ao repouso
            slp	= Slope of the peak exercise ST segment - Inclinação do pico do segmento ST por exercício - (2 = subindo; 1 = plato; 0 = descendo)
            caa	= The number of major vessels (0-3) - Número de vasos 
            thall= A blood disorder called thalassemia - Uma disordem sanguinea chamada talassemia - (2 = normal; 1 = defeito corrigido; 3 = defeito reversível)
            output = diagnóstico  (0 = baixo risco; 1 = alto risco)
        """
        self.aluno_nome = aluno_nome
        self.age = age
        self.sex = sex             
        self.cp = cp
        self.trtbps = trtbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalachh = thalachh
        self.exng = exng
        self.oldpeak = oldpeak
        self.slp = slp
        self.caa = caa
        self.thall = thall
        self.output = output