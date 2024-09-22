from schemas.comentario import ComentarioSchema

from schemas.saude_parametros import SaudeParametrosSchema, SaudeParametrosViewSchema, SaudeParametrosBuscaSchemaPorNome, ListagemSaudeParametrosSchema, \
                            SaudeParametrosDelSchema, \
                            apresenta_saude_parametros_alunos, apresenta_saude_parametros

from schemas.tecnica import TecnicaSchema, TecnicaBuscaSchemaPorID, TecnicaBuscaSchemaPorNome, TecnicaBuscaSchemaPorTermo, TecnicaViewSchema, \
                            ListagemTecnicasSchema, TecnicaPathSchema, TecnicaBodySchema, TecnicaDelSchema, \
                            apresenta_tecnica, apresenta_tecnicas
                            
from schemas.aluno import   AlunoSchema, AlunoBuscaSchemaPorID, AlunoBuscaSchemaPorNome, AlunoBuscaSchemaPorTermo, AlunoViewSchema, \
                            ListagemAlunosSchema, AlunoDelSchema, \
                            apresenta_aluno, apresenta_alunos

from schemas.error import ErrorSchema
