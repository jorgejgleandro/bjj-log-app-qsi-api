from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from  model import Base, Comentario

class Aluno(Base):
    __tablename__ = 'aluno'

    id = Column("pk_aluno", Integer, primary_key=True)
    nome = Column(String(140), unique=True)    
    data_de_nascimento = Column(DateTime)
    data_de_inicio = Column(DateTime)
    graduacao = Column(String(140))
    endereco = Column(String(300))

    def __init__(self, nome:str, graduacao:str, data_de_nascimento:str, data_de_inicio:str, endereco:str):
        """
        Cadastra um Auno

        Argumentos:
            nome: nome do aluno.
            data de nascimento: data de nascimento do aluno.
            data de inicio: data da primeira aula do aluno
            graduacao: cor da faixa do aluno
            endereco: residencia do aluno
        """
        self.nome = nome
        self.data_de_nascimento = datetime.strptime("%s" % data_de_nascimento, "%d/%m/%Y")
        self.data_de_inicio = datetime.strptime("%s" % data_de_inicio, "%d/%m/%Y")             
        self.graduacao = graduacao
        self.endereco = endereco