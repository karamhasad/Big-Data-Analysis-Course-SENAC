import pandas as pd

df = pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep=';', encoding='latin1')

#print(df.head(5))
#print(df.describe())
#print(df.tail(5))

#Criar a variavel de data frame e juntar duas informações
df_roubo_celular_dp = df.groupby('cisp')['roubo_celular'].sum().reset_index()

#Ordenar por valor maior ao menor
df_roubo_celular_dp = df_roubo_celular_dp.sort_values(by='roubo_celular', ascending=False)

#imprimir o resultado
print(df_roubo_celular_dp)