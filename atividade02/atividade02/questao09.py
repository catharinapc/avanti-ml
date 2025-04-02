#Utilizando pandas, como selecionar uma coluna específica e filtrar linhas  em um “DataFrame” com base em uma condição?

import pandas as pd

# Criando um exemplo de DataFrame
data = {'coluna_A': [5, 15, 20, 8, 30],
        'coluna_B': [1, 12, 18, 7, 25],
        'coluna_C': ['A', 'B', 'C', 'D', 'E']}

df = pd.DataFrame(data)

# Selecionar uma coluna específica
coluna_selecionada = df['coluna_A']
print(coluna_selecionada.head())

# Filtrar linhas com base em uma condição
linhas_filtradas = df[df['coluna_A'] > 10]
print(linhas_filtradas)

# Filtrar e selecionar uma coluna específica ao mesmo tempo
resultado = df.loc[df['coluna_B'] > 10, 'coluna_C']
print(resultado)

