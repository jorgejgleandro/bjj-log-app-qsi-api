from pydantic import BaseModel
from pydantic.functional_validators import field_validator
from typing import Optional, List
from model.saudeparametros import SaudeParametros
from datetime import datetime

from schemas import ComentarioSchema

class SaudeParametrosSchema(BaseModel):
    """ Define como um novo SaudeParametros a ser inserido deve ser representado
    """
    aluno_nome: str = "Mateus"
    age: int = 36
    sex: int = 1
    cp: int = 3
    trtbps: int	= 120
    chol: int = 130
    fbs: int = 1
    restecg: int = 1
    thalachh: int = 125
    exng: int = 1
    oldpeak: float = 4.1
    slp: int = 2
    caa: int = 3
    thall: int = 2

class SaudeParametrosViewSchema(BaseModel):
    id: int = 1
    aluno_nome: str = "Mateus"
    age: int = 36
    sex: int = 1
    cp: int = 3
    trtbps: int	= 120
    chol: int = 130
    fbs: int = 1
    restecg: int = 1
    thalachh: int = 125
    exng: int = 1
    oldpeak: float = 4.1
    slp: int = 2
    caa: int = 3
    thall: int = 2
    output: int = None


class SaudeParametrosBuscaSchemaPorNome(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no diagnostico.
    """
    aluno_nome: str = "Mateus"

class ListagemSaudeParametrosSchema(BaseModel):
    """ Define como uma listagem de parametros será devolvida.
    """
    alunos_parametros:List[SaudeParametrosSchema]


def apresenta_saude_parametros_alunos(alunos_parametros: List[SaudeParametros]):
    """ Devolve uma representação de saude parametros seguindo o schema definido em
        SaudeParametrosSchema.
    """
    result = []
    for aluno_parametros in alunos_parametros:
        result.append({
            "aluno_nome": aluno_parametros.aluno_nome,
            "age": aluno_parametros.age,
            "sex": aluno_parametros.sex,
            "cp": aluno_parametros.cp,
            "trtbps": aluno_parametros.trtbps,
            "chol": aluno_parametros.chol,
            "fbs": aluno_parametros.fbs,
            "restecg": aluno_parametros.restecg,
            "thalachh": aluno_parametros.thalachh,
            "exng": aluno_parametros.exng,
            "oldpeak": aluno_parametros.oldpeak,
            "slp": aluno_parametros.slp,
            "caa": aluno_parametros.caa,
            "thall": aluno_parametros.thall,
            "output": aluno_parametros.output
        })

    return {"alunos_parametros": result}


class SaudeParametrosDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado devolvido após uma requisição
        de remoção.
    """
    nome: str = "Mateus"

def apresenta_saude_parametros(saude_parametros: SaudeParametros):
    """ Devolve uma representação de saude parametros seguindo o schema definido em
        SaudeParametrosSchema.
    """
    return {
            "aluno_nome": saude_parametros.aluno_nome,
            "age": saude_parametros.age,
            "sex": saude_parametros.sex,
            "cp": saude_parametros.cp,
            "trtbps": saude_parametros.trtbps,
            "chol": saude_parametros.chol,
            "fbs": saude_parametros.fbs,
            "restecg": saude_parametros.restecg,
            "thalachh": saude_parametros.thalachh,
            "exng": saude_parametros.exng,
            "oldpeak": saude_parametros.oldpeak,
            "slp": saude_parametros.slp,
            "caa": saude_parametros.caa,
            "thall": saude_parametros.thall,
            "output": saude_parametros.output
    }