# %% 
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]
indexs = [
"Téo", "Maria", "Jose", "Luis", "Ana",
"Nah", "Dani", "Mah", "Fer", "Nanda",
"Naty", "Nih", "Pedro", "Kozato", "Kozato"
]
series_idades = pd.Series(idades)

# iloc consulta a posição na série ao invés do indíce
series_idades.iloc[0]
# alterando o indíce padrão para a lista indexs
series_idades = pd.Series(idades, index=indexs)
#o .loc consulta o indíce: series_idades.loc[0] == series_idades[0]