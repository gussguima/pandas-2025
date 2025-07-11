# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]
nomes = [
"Téo", "Maria", "Jose", "Luis", "Ana",
"Nah", "Dani", "Mah", "Fer", "Nanda",
"Naty", "Nih", "Pedro", "Kozato", "Kozato"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%
df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes

# %%
df["nomes"] # consulta uma coluna no dataframe
df.iloc[0] # consulta uma linha no dataframe retornando uma series
df.iloc[0]["nomes"] # consulta o indice da serie que foi retornada no .iloc[0]
df.iloc[-1]["idades"] # consulta o indice da serie que foi retornada no .iloc[0]
