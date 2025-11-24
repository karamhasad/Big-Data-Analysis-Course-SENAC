import pandas as pd
df = pd.read_csv('ClassicDisco.csv')

for i, coluna in enumerate(df.columns, start = 1):
    print(f"{i} coluna: {coluna}")