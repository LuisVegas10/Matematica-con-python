'''
Este ejercicio pide un numero al usuario por consola, y determina de 2 a dicho numero, cuanto son primos
'''

numbers = int(input("Ingrese un numero entero positivos: "))
listPrime = []

if numbers >= 2:
    # Done: Ciclo que determina si cada numero es primo o no, si es primo se agrega a la lista
    for i in range(numbers + 1):
        dividers = []
        # si un número es primo o compuesto basta con dividirlo por los números primos menores que él hasta llegar a un cociente igual o menor que el divisor.
        for j in range(1, i + 1):
            if i % j == 0:
                dividers.append(j)
        # Si ninguna de estas divisiones es exacta, el número es primo.
        # Si alguna de las divisiones es exacta el número es compuesto.
        if len(dividers) == 2:
            listPrime.append(i)

    print(f"Numeros primos: {listPrime}")
else:
    print("Debe ingresar un numero positivo.")
