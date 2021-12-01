def humano_a_perro(edad):
    edad_humano = int(edad)
    edad_perro = 0
    PERRO_JOVEN = 10.5
    PERRO_ADULTO = 4

    if edad_humano <= 0:
        print('La edad debe ser mayor a 0')
        return

    if edad_humano <=2:
        edad_perro = edad_humano * PERRO_JOVEN
        return edad_perro
    
    else:
        edad_perro = PERRO_JOVEN * 2
        edad_perro = edad_perro + (edad_humano - 2) * PERRO_ADULTO
        return edad_perro
    return NULL

def test_humano_a_perro():
    assert humano_a_perro(10) == 53

edad = input('Introduzc la edad: ')
edad_calculada = humano_a_perro(edad)
print("La edad del perro es: ", edad_calculada)