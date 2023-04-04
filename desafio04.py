valores = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}

# Cálculo do valor total mensal
valor_total = sum(valores.values())

# Cálculo do percentual de representação de cada estado
percentuais = {}
for estado, valor in valores.items():
    percentuais[estado] = (valor / valor_total) * 100

# Impressão dos resultados
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')
