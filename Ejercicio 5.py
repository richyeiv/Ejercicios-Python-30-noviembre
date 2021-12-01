def horoscopo_chino(año_nacimiento):
    año = int(año_nacimiento)
    if (año - 2000) % 12 == 0:
        sign = 'Dragón'
    elif (año - 2000) % 12 == 1:
        sign = 'Serpiente'
    elif (año - 2000) % 12 == 2:
        sign = 'Caballo'
    elif (año - 2000) % 12 == 3:
        sign = 'Oveja'
    elif (año - 2000) % 12 == 4:
        sign = 'Mono'
    elif (año - 2000) % 12 == 5:
        sign = 'Gallo'
    elif (año - 2000) % 12 == 6:
        sign = 'Perro'
    elif (año - 2000) % 12 == 7:
        sign = 'Puerco'
    elif (año - 2000) % 12 == 8:
        sign = 'Rata'
    elif (año - 2000) % 12 == 9:
        sign = 'Buey'
    elif (año - 2000) % 12 == 10:
        sign = 'Tigre'
    else:
        sign = 'Liebre'

    return sign

año = input('Introduzca su año de nacimiento: ')
animal = horoscopo_chino(año)
print("Su animal es: " + animal)