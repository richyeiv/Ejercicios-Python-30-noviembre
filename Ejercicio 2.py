num1 = input('Ingrese el 1er número:')
num2 = input('Ingrese el 2do número:')
num3 = input('Ingrese el 3er número:')

num_min = min(num1, num2, num3)
num_max = max(num1, num2, num3)
num_med = int(num1) + int(num2) + int(num3) - int(num_min) - int(num_max)
print(num_min, ", ", num_med, ", ", num_max)
