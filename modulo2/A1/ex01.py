import pandas as pd

# Criar lista de dados
dados = [10,20,30,40]

# Criar Série
serie = pd.Series(dados, index = ['a', 'b', 'c', 'd'])
print(serie)

# Acessar elemento pelo índice
print(serie['a'])
