def es_palindromo(palabra):
    palabra = palabra.strip()
    if len(palabra) <= 1 :
        return True
    if palabra[0] == palabra[len(palabra) - 1] :
        return es_palindromo(palabra[1:len(palabra) - 1])
    else :
        return False

palabra = input("Ingrese la palabra: ")
resultado = es_palindromo(palabra)
if resultado:
    print(palabra, " es palindromo")
else: 
    print(palabra, " no es palindromo")