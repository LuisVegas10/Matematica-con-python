'''
Este ejercicio determina si un numero ingresado por consola es primo.
'''

number = int(input("Ingrese el numero: "))
isPrime = True

# DONE: Si es menor o igual a 1, entonces no es primo
if number < 2:
    isPrime = False
else:
    '''
    si un número es primo o compuesto basta con dividirlo por los números primos menores que él hasta llegar a un cociente igual o menor que el divisor. 
    Si ninguna de estas divisiones es exacta, el número es primo.
    Si alguna de las divisiones es exacta el número es compuesto y podemos interrumpir el proceso.
    '''
    for i in range(2, number):
        if (number % i) == 0:
            isPrime = False
            break

if isPrime:
    print(f"El numero {number} es primo")
else:
    print(f"El numero {number} no es primo")
