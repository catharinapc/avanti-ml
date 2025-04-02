#  Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

import pandas as pd

# Leitura do arquivo CSV para um DataFrame
dataframeExemplo = pd.read_csv('caminho/para/o/arquivo.csv')

# Onde dentro do .head() se coloco o numero de linhas desejados é o numero de linhas a serem exibidas
dataframeExemplo.head(7)

#Ou dessa forma caso não esteja sendo utilizado um ambiente interativo
print(dataframeExemplo.head(7))
