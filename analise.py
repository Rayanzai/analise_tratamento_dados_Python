import pandas as pd
import plotly.express as px

#abrindo e lendo tabela de dados
df = pd.read_csv('telecom_users.csv')
#Tratando a base de dados
df = df.drop(['Unnamed: 0'], axis = 1) 

#transformando a coluna TOTALGASTO para float e transformando erros em NaN
df['TotalGasto'] = pd.to_numeric(df['TotalGasto'], errors='coerce')

#Remove a coluna que está totalmente vazia "CODIGO"
df = df.dropna(how='all', axis = 1)

#Remove a linha que tem um item vazio
df = df.dropna(how='any', axis = 0)

print(df.info())

#Visualizar quantos cancelaram ou não cancelaram...26%?
print(df['Churn'].value_counts())
#transforma em porcentagem
print(df['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

############### CRIAÇÃO DOS GRÁFICOS

for coluna in df.columns:
    if coluna != "custumerID":
        #cria o gráfico
        grafico = px.histogram(df, x=coluna, color='Churn', text_auto=True)

        #exibe o gráfico
        grafico.show()

######### ANÁLISE DOS GRÁFICOS GERADOS
