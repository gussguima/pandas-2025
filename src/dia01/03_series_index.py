# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39
]

series_idades = pd.Series(idades)

# %%
# iloc puxa a posição na série ao invés de puxar o indice
series_idades.iloc[0]
# %%
indexs = [
"Téo", "Maria", "Jose", "Luis", "Ana",
"Nah", "Dani", "Mah", "Fer", "Nanda",
"Naty", "Nih", "Pedro", "Kozato", "Kozato"
]

series_idades = pd.Series(idades, index=indexs)
series_idades["Kozato"]