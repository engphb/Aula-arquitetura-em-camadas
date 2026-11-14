import dados

def cadastrar_aluno(nome):
  if nome =="":
    return "Nome inválido"

  dados.salvar_aluno(nome)
  return "Aluno cadastrado com sucesso"

def obter_alunos():
  return dados.listar_alunos()
  
  

