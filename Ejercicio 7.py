def es_bisiesto(año):
    if año % 400 == 0:
        return True
    if año % 100 == 0:
        return False
    if año % 4 == 0:
        return True
    return False

def dias_en_mes(mes, año):
    mes = int(mes)
    año = int(año)
    if mes in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if mes == 2:
        if es_bisiesto(año):
            return 29
        return 28
    return 30

mes = input("mes: ")
año = input("año: ")
print(dias_en_mes(mes, año)) 