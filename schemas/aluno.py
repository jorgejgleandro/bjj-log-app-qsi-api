from pydantic import BaseModel
from pydantic.functional_validators import field_validator
from typing import Optional, List
from model.aluno import Aluno
from datetime import datetime

from schemas import ComentarioSchema, SaudeParametrosViewSchema

class AlunoSchema(BaseModel):
    """ Define como um novo Aluno a ser inserido deve ser representado
    """
    nome: str = "Mateus"
    data_de_nascimento: str = "15/05/1975"
    data_de_inicio: str = "11/06/2023"
    graduacao: str = "branca"
    endereco: str = "Rua Nelson Righi, Parque dos Ipes, Jaguariuna, SP"

    @field_validator('data_de_nascimento')
    def date_validation1(cls, v):
        try:
            _ = datetime.strptime(v, "%d/%m/%Y")
            return v
        except Exception as e:
            raise ValueError('A data deve ter um formato dd/mm/yyyy')
   
    @field_validator('data_de_inicio')
    def date_validation2(cls, v):
        try:
            _ = datetime.strptime(v, "%d/%m/%Y")
            return v
        except Exception as e:
            raise ValueError('A data deve ter um formato dd/mm/yyyy')


class AlunoBuscaSchemaPorTermo(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base em um termo no nome do Aluno.
    """
    nome: str = "Mateus"

class AlunoBuscaSchemaPorNome(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do Aluno.
    """
    nome: str = "Mateus"

class AlunoBuscaSchemaPorID(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no ID do Aluno.
    """
    id: int = 1

class ListagemAlunosSchema(BaseModel):
    """ Define como uma listagem de alunos será devolvida.
    """
    alunos:List[AlunoSchema]


def apresenta_alunos(alunos: List[Aluno]):
    """ Devolve uma representação de aluno seguindo o schema definido em
        AlunoSchema.
    """
    result = []
    for aluno in alunos:
        result.append({
            "id": aluno.id,
            "nome": aluno.nome,
            "data_de_nascimento": aluno.data_de_nascimento.strftime("%d/%m/%Y"),
            "data_de_inicio": aluno.data_de_inicio.strftime("%d/%m/%Y"),
            "graduacao": aluno.graduacao,
            "endereco": aluno.endereco
        })

    return {"alunos": result}


class AlunoViewSchema(BaseModel):
    """ Define como um aluno será devolvido: aluno.
    """
    id: int = 1
    nome: str = "Mateus"
    data_de_nascimento: str = "15/05/1975"
    data_de_inicio: str = "11/06/2023"
    graduacao: str = "branca"
    endereco: str = "Rua Nelson Righi, Parque dos Ipes, Jaguariuna, SP" 
    saude_parametros: List[SaudeParametrosViewSchema] = []


class AlunoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado devolvido após uma requisição
        de remoção.
    """
    mensagem: str
    nome: str

def apresenta_aluno(aluno: Aluno):
    """ Devolve uma representação de aluno seguindo o schema definido em
        AlunoViewSchema.
    """
    return {
        "id": aluno.id,
        "nome": aluno.nome,
        "data_de_nascimento": aluno.data_de_nascimento.strftime("%d/%m/%Y"),
        "data_de_inicio": aluno.data_de_inicio.strftime("%d/%m/%Y"),        
        "graduacao": aluno.graduacao,
        "endereco": aluno.endereco
    }