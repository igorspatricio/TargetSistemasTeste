import json


def RetirarDiasDeFaturamentoMaiorMedia(faturamentoDeUmMes):
    media = 0
    diasDeFaturamento = 0
    for faturamento in faturamentoDeUmMes:
        if faturamento['valor'] > 0:
            media += faturamento['valor']
            diasDeFaturamento += 1
    media /= diasDeFaturamento

    diasDeFaturamentoMaiorMedia = 0
    for faturamento in faturamentoDeUmMes:
        if faturamento['valor'] > media:
            diasDeFaturamentoMaiorMedia += 1

    return diasDeFaturamentoMaiorMedia

#--------------------------------------------------------------------------------#

def getMaxMin(listaFatuamento):
    maior = listaFatuamento[0]['valor']
    menor = listaFatuamento[0]['valor']

    #caso o primero faturamento seja 0 devido a feriado/fim de semana
    i = 1
    while(menor == 0):
        menor = listaFatuamento[i]['valor']

    for faturamento in listaFatuamento:
        if faturamento['valor'] > maior:
            maior = faturamento['valor']

        if faturamento['valor'] < menor and faturamento['valor'] > 0:
            menor = faturamento['valor']

    return (menor, maior)

#--------------------------------------------------------------------------------#

with open("dados.json") as dados:
    faturamentoDeUmMes = json.load(dados)

maior, menor = getMaxMin(faturamentoDeUmMes)
diasDeFaturamentoMaiorMedia = RetirarDiasDeFaturamentoMaiorMedia(faturamentoDeUmMes)


print("Maior Faturamento:  ", maior)
print("Menor Faturamento: ", menor)
print("Numero de dias em que o faturamento foi maior que a media: ", diasDeFaturamentoMaiorMedia)
