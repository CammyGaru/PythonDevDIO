import pandas as pd

df = pd.read_csv(r"C:\Users\cgaruche\PycharmProjects\pythonProjectDIO\pythonPandas\star_wars_character_dataset.csv")


# Exibir as 5 primeiras linhas
print(df.head())

# Exibir linhas e colunas
print(df.shape)

# Exibir colunas
print(df.dtypes)

# Exibir as ultimas linhas
print(df.tail())

# Exibir as decrições e estáticas dos dados
print(df.describe())

# Exibir apenas o que tem em cada coluna
print(df["starships"].unique())

# Agrupar quantas Starships tem por nome
print(df.groupby("starships")["name"].nunique())

