#dados = {}
aluno = {"nome": "Ana", "idade":16, "nota":9.0}
print(aluno["nome"]) # Ana


# #adicionar um valor a um item da lista
# aluno["nota"]= 9.5
# print(aluno["nota"])

# print(aluno.keys())
# print(aluno.values())
# print(aluno.items())

# #verificar se uma chave existe dentro de um dicionario
# if "nome" in aluno:
#     print('Aluno encontrado')

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")