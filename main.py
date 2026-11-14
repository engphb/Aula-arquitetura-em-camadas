import negocio

while True:
  print("\n1 - Cadastrar aluno")
  print("2 - Listar alunos")
  print("3 - Sair")

  op = input("\nDigite a opção desejada:")
  if op=="1":
     nome = input("Digite o nome do aluno: ")
     print(negocio.cadastrar_aluno(nome))
  
  elif op=="2":
    lista =  negocio.obter_alunos()
    print("Alunos:", lista)

  elif op=="3":
    print("Encerrando...")
    break