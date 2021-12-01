def caracteres_unicos(cadena):
    unicos = {}
    for i in cadena:
        unicos[i] = unicos.get(i, 0) + 1
    print(unicos)
    unicos = {k:v for (k,v) in unicos.items() if v<2}
    return unicos.keys()

unicos = caracteres_unicos('hola mundo')
print(unicos)