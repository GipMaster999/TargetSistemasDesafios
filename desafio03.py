import json

# Lê o arquivo JSON com a tabela de faturamento
with open('dados.json') as json_file:
    tabela = json.load(json_file)

# Calcula o dia com maior e menor faturamento
maior_faturamento = max(tabela, key=lambda x: x['valor'])
menor_faturamento = min(tabela, key=lambda x: x['valor'])

print('Dia com maior faturamento:', maior_faturamento['dia'])
print('Dia com menor faturamento:', menor_faturamento['dia'])

# Calcula a média mensal de faturamento, excluindo os dias sem faturamento
valores = [d['valor'] for d in tabela if d['valor'] > 0]
media_mensal = sum(valores) / len(valores)

# Mostra os dias acima da média mensal, excluindo os dias sem faturamento
dias_acima_media = [d['dia'] for d in tabela if d['valor'] > media_mensal]
print('Dias acima da média mensal:', dias_acima_media)
