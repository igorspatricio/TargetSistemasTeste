import json

with open("faturamentoEstados.json") as dados:
    faturamentoEstados = json.load(dados)


faturamentoTotal = 0
for faturamento in faturamentoEstados:
    faturamentoTotal += faturamento['valor']

a = 0
for faturamento in faturamentoEstados:
    porcentagemFaturamento = (faturamento['valor']*100) / faturamentoTotal
    print("{0}:{1}%".format(faturamento['estado'], round(porcentagemFaturamento, 2)))

