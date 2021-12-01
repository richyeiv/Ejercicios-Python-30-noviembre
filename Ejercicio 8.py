import random
def loteria():
    numeros = []
    while True:
        if len(numeros) == 6:
            numeros = sorted(numeros)
            break
        generado = random.randint(1, 49)
        if generado not in numeros:
            numeros.append(generado)
    return numeros

numeros = loteria()
print('Los numeros son: ', numeros)
