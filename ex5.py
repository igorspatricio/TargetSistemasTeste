def invertString(string):
    stringInvertida = ''
    for indice in range(len(string)):
        stringInvertida = stringInvertida + string[(indice+1) * (-1)]
    return stringInvertida

string = input("Insira uma string: ")
print(invertString(string))
print(string[-1::-1])
