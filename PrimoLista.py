'''
Este ejercicio se ingresa un numero, y determina de 0 a dicho numero, cuanto son primos
'''

numeros = int(input("Ingrese un numero entero positivos: "))
list_primo = []

#Ciclo que determina si cada numero es primo o no, si es primo se agrega a la lista
for i in range(numeros + 1):
    divisores = []
    #si un número es primo o compuesto basta con dividirlo por los números primos menores que él hasta llegar a un cociente igual o menor que el divisor.
    for j in range(1, i + 1):
        if i % j == 0:
            divisores.append(j)
    #Si ninguna de estas divisiones es exacta, el número es primo.
    #Si alguna de las divisiones es exacta el número es compuesto y podemos interrumpir el proceso.
    if len(divisores) == 2:
        list_primo.append(i)

print(f"Primos: {list_primo}")
