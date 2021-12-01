def es_vocal(letra):
    x = letra[0]
    vocales = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]
    y = [89, 121]
    ñ = [164, 165]

    if(ord(x) in y):
        print('>> A veces "Y" es una vocal y a veces una consonante')
    elif(ord(x) in vocales):
        print('>> El caracter es una vocal')
    elif((ord(x) >= 97 and ord(x) <= 122) or (ord(x) >= 65 and ord(x) <= 90) or (ord(x) in ñ)):
        print('>> El caracter es una consonante')

letra = input('ingrese una letra: ')
es_vocal(letra)