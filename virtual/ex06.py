import pandas as pd
df = pd.read_csv('ClassicDisco.csv')

filtro=df['Year']
print(filtro)