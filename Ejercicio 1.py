def ejercicio_1(num):
    num_str = int(num[0])
    num_str = num_str + int(num[1])
    num_str = num_str + int(num[2])
    num_str = num_str + int(num[3])
    print(num[0], " + ", num[1], " + ", num[2], " + ", num[3], " = ", num_str)

num = input('Ingrese numero entero a 4 digitos:')
ejercicio_1(num)