'''
Este ejercicio determina si un numero es primo
'''

numero = int(input("Ingrese el maximo: "))
primo = True

#Si es menor o igual a 1, entonces no es primo
if numero < 2:
    primo = False
else:
    '''
    si un número es primo o compuesto basta con dividirlo por los números primos menores que él hasta llegar a un cociente igual o menor que el divisor.
    Si ninguna de estas divisiones es exacta, el número es primo.
    Si alguna de las divisiones es exacta el número es compuesto y podemos interrumpir el proceso.
    '''
    for i in range(2, numero):
        if (numero % i) == 0:
            primo = False
            break

if primo:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
