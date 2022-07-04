def isfat(numero):
    if numero == 1 or numero == 0:
        print("O numero {} pertence a sequencia de Fibonacci!".format(numero))
        return True

    fibo1 = 0
    fibo2 = 1 
    while(numero > fibo2):
        auxiliar = fibo2
        fibo2 = fibo2 + fibo1 
        fibo1 = auxiliar

        if numero == fibo2:
            print("O numero {} pertence a sequencia de Fibonacci!".format(numero))
            return True  
    
    print("Numero {} não pertence a sequencia de Fibonacci!".format(numero))
    return False

while True:
    try:
        numeroTestar = int(input("Insira um numero: "))
        break
    except:
        print("Entrada invalida")

isfat(numeroTestar)

        