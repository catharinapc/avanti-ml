# Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

import pandas as pd

# Criando um DataFrame de exemplo com valores ausentes (NaN)
data = {'coluna_A': [1, 2, None, 4, 5],
        'coluna_B': ['A', None, 'C', None, 'E'],
        'coluna_C': [10.5, None, 30.2, 40.1, None]}

df = pd.DataFrame(data)

# Verificar valores ausentes no DataFrame
valores_ausentes = df.isna()
print("Valores ausentes no DataFrame:\n", valores_ausentes)

# Verificar valores ausentes em uma coluna específica
coluna_valores_ausentes = df['coluna_A'].isna()
print("\nValores ausentes na coluna_A:\n", coluna_valores_ausentes)

# Preencher valores ausentes em todo o DataFrame com um valor padrão
df_preenchido = df.fillna(0)  # Substitui NaN por 0
print("\nDataFrame com valores ausentes preenchidos:\n", df_preenchido)

# Preencher valores ausentes em uma coluna específica com um valor específico
df['coluna_B'] = df['coluna_B'].fillna('Desconhecido')
print("\nDataFrame após preenchimento da coluna_B:\n", df)