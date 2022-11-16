import pandas as pd

# Carrega os dados específico da coluna dos valores em um DataFrame
df = pd.read_html('relatorio_IN.html')[0]
valores = df[11:][[4]]
valores.columns = ["Valores"]
valores.head(20)

# Filtra somente os valores de débitos, isto é, os que contém 'D'
mask = valores.Valores.str.contains(r'D', na=True)

# Elimina os valores não numéricos e armazena em uma Series
valores_filtro = pd.to_numeric(valores[mask].Valores.str.replace(" D", '', regex=False).str.replace(".", '', regex=False).str.replace(",", '.', regex=False).str.replace(" ", '', regex=False))
valores_filtro.head(20)

# Exibe o resultado
f"Soma dos valores debitados da Imprensa Nacional: R$ {valores_filtro.sum():_.2f}".replace('.',',').replace("_", ".")