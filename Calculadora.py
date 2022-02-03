from fractions import Fraction
import math
import time

'''
Este ejercicio realiza las operaciones basicas de una calculadora cientifica, datos ingresados por consola.
'''


# Operaciones Basicas.
# DONE: 01. Devuelve la suma de 'nUno' y 'nDos'
def suma(nUno: float, nDos: float) -> float:
    resultado = nUno + nDos
    print(f"Suma = {nUno} + {nDos} = {resultado}")
    return resultado


# DONE: 02. Devuelve la resta de 'nUno' y 'nDos'
def resta(nUno: float, nDos: float) -> float:
    resultado = nUno - nDos
    print(f"Resta = {nUno} - {nDos} = {resultado}")
    return resultado


# DONE: 03. Devuelve la multiplicacion del 'factor1' y del 'factor2'
def Multiplicacion(factor1: float, factor2: float) -> float:
    producto = factor1 * factor2
    print(f"Multiplicacion = {factor1} * {factor2} = {producto}")
    return producto


# DONE: 04. Devuelve la dividicion del 'dividendo' y el 'divisor'
def divicion(dividendo: float, divisor: float) -> float:
    cociente = 0.0
    if divisor <= 0:
        print("Error: el divisor nunca puede ser 0.")
    else:
        cociente = dividendo / divisor
        resto = dividendo // divisor
        decimales = cociente - resto
        print(f"Divicion = {dividendo} / {divisor} = {cociente}")
        print(f"Resto = {resto}")
        print(f"Desto = {decimales}")
    return cociente


# DONE: 05. Devuelve la dividicion modular del 'dividendo' y el 'divisor'
def dividirModular(dividendo: float, divisor: float) -> float:
    cociente = 0.0
    if divisor <= 0:
        print("Error: el divisor nunca puede ser 0.")
    else:
        cociente = dividendo % divisor
        print(f"Divicion Modular = {dividendo} % {divisor} = {cociente}")
    return cociente


# Potencia y funciones logarítmicas
# DONE: 06. Devuelve la Potencia de la 'base' elevado a la 'exponente'.
def potenciacion(base: float, exponente: float) -> float:
    potencia = math.pow(base, exponente)
    print(f"Potencia = {base} ^ {exponente} = {potencia}")
    return potencia


# DONE: 07. Devuelve el resultado de la 'base' e elevado al 'exponente'.
def potenciacionBasee(exponente: float) -> float:
    potencia = math.exp(exponente)
    print(f"Numero e elevado a {exponente} = {potencia}")
    return potencia


# DONE: 08. Devuelve el logaritmo natural del 'argumento'.
def log(argumento: float) -> float:
    logaritmo = math.log(argumento)
    print(f"Logaritmo de base e (Logaritmo Neperiano) = {logaritmo}")
    return logaritmo


# DONE: 09. Devuelve el logaritmo en base 10 del 'argumento'.
def log10(argumento: float) -> float:
    logaritmo = math.log10(argumento)
    print(f"Logaritmo de base 10 = {logaritmo}")
    return logaritmo


# DONE: 10. Devuelve la Raíz Cuadrada del 'subradical'.
def raizCuadrada(subradical: float) -> float:
    raiz = math.sqrt(subradical)
    print(f"Raiz Cuadrada = {raiz}")
    return raiz


# Funciones trigonométricas
# DONE: 11. Devuelve el Coseno de 'nUno'.
def coseno(nUno: float) -> float:
    cos = math.cos(nUno)
    print(f"Coseno = {cos}")
    return cos


# DONE: 12. Devuelve el arcocoseno de 'nUno'.
def arcocoseno(nUno: float) -> float:
    acos = math.acos(nUno)
    print(f"ArcoCoseno = {acos}")
    return acos


# DONE: 13. Devuelve el Seno de 'nUno'.
def seno(nUno: float) -> float:
    sin = math.sin(nUno)
    print(f"Seno = {sin}")
    return sin


# DONE: 14. Devuelve el ArcoSeno de 'nUno'.
def arcoseno(nUno: float) -> float:
    asin = math.asin(nUno)
    print(f"ArcoSeno = {asin}")
    return asin


# DONE: 15. Devuelve el Tangente de 'nUno'.
def tangente(nUno: float) -> float:
    tan = math.tan(nUno)
    print(f"Tangente = {tan}")
    return tan


# DONE: 16. Devuelve el arcotangente de 'nUno'.
def arcotangente(nUno: float) -> float:
    atan = math.atan(nUno)
    print(f"ArcoTangente = {atan}")
    return atan


# DONE: 17. Devuelve la cosecante de 'nUno'.
def cosecante(nUno: float) -> float:
    cosec = 1 / math.sin(nUno)
    print(f"Cosecante = {cosec}")
    return cosec


# DONE: 18. Devuelve la Arcocosecante de 'nUno'.
def arcoCosecante(nUno: float) -> float:
    arccosec = math.asin(1 / nUno)
    print(f"ArcoCosecante = {arccosec}")
    return arccosec


# DONE: 19. Devuelve la secante de 'nUno'.
def secante(nUno: float) -> float:
    sec = 1 / math.cos(nUno)
    print(f"Secante = {sec}")
    return sec


# DONE: 20. Devuelve el ArcoSecante de 'nUno'.
def arcoSecante(nUno: float) -> float:
    arcsec = math.acos(1 / nUno)
    print(f"ArcoSecante = {arcsec}")
    return arcsec


# DONE: 21. Devuelve la cotangente de 'nUno'.
def cotangente(nUno: float) -> float:
    cotag = 1 / math.tan(nUno)
    print(f"Cotangente = {cotag}")
    return cotag


# DONE: 22. Devuelve la ArcoCotangente de 'nUno'.
def arcoCotangente(nUno: float) -> float:
    arccotag = math.atan(1 / nUno)
    print(f"ArcoCotangente = {arccotag}")
    return arccotag


# Funciones hiperbólicas
# DONE: 23. Devuelve el coseno hiperbólico de 'nUno'.
def cosenoHiper(nUno: float) -> float:
    cosh = math.cosh(nUno)
    print(f"Coseno Hiperbolico = {cosh}")
    return cosh


# DONE: 24. Devuelve el ArcoCoseno hiperbólico de 'nUno'.
def arcoCosenoHiper(nUno: float) -> float:
    arccosh = 1 / math.cosh(nUno)
    print(f"ArcoCoseno Hiperbolico = {arccosh}")
    return arccosh


# DONE: 25. Devuelve el seno hiperbólico de 'nUno'.
def senoHiper(nUno: float) -> float:
    sinh = math.sinh(nUno)
    print(f"Seno Hiperbolico = {sinh}")
    return sinh


# DONE: 26. Devuelve el ArcocoSeno hiperbólico de 'nUno'.
def arcoSenoHiper(nUno: float) -> float:
    arcsinh = 1 / math.sinh(nUno)
    print(f"ArcocoSeno Hiperbolico = {arcsinh}")
    return arcsinh


# DONE: 27. Devuelve el tangente hiperbólico de 'nUno'.
def tangenteHiper(nUno: float) -> float:
    tanh = math.tanh(nUno)
    print(f"Tangente Hiperbolico = {tanh}")
    return tanh


# DONE: 28. Devuelve la ArcoTangente hiperbólica de 'nUno'.
def arcoTangenteHiper(nUno: float) -> float:
    arctagh = 1 / math.tanh(nUno)
    print(f"ArcoTangente Hiperbolico = {arctagh}")
    return arctagh


# DONE: 29. Devuelve la Cosecante hiperbolico de 'nUno'.
def cosecanteHiper(nUno: float) -> float:
    coseh = 1 / math.sinh(nUno)
    print(f"Cosecante Hiperbolico = {coseh}")
    return coseh


# DONE: 30. Devuelve la ArcoCosecante Hiperbolico de 'nUno'.
def arcoCosecanteHiper(nUno: float) -> float:
    arcsech = 1 / (1 / math.sinh(nUno))
    print(f"ArcoCosecante Hiperbolico = {arcsech}")
    return arcsech


# DONE: 31. Devuelve la Secante hiperbolico de 'nUno'.
def secanteHiper(nUno: float) -> float:
    sech = 1 / math.cosh(nUno)
    print(f"Secante Hiperbolico = {sech}")
    return sech


# DONE: 32. Devuelve la ArcoSecante hiperbolico de 'nUno'.
def arcoSecanteHiper(nUno: float) -> float:
    arccoseh = 1 / (1 / math.cosh(nUno))
    print(f"ArcoSecante Hiperbolico = {arccoseh}")
    return arccoseh


# DONE: 33 Devuelve la Cotangente Hiperbolico de 'nUno'.
def cotangenteHiper(nUno: float) -> float:
    cotagh = 1 / math.tanh(nUno)
    print(f"Cotangente Hiperbolico = {cotagh}")
    return cotagh


# DONE: 34 Devuelve la ArcoCotangente Hiperbolico de 'nUno'.
def arcoCotangenteHiper(nUno: float) -> float:
    arccotagh = 1 / (1 / math.tanh(nUno))
    print(f"ArcoCotangente Hiperbolico = {arccotagh}")
    return arccotagh


# Conversión angular
# DONE: 35. Devuelve la conversion de radianes a grados de 'radians'.
def getGrados(radians: float) -> float:
    degrees = math.degrees(radians)
    print(f"Pasar de Radianes = {radians} a Grados = {degrees}")
    return degrees


# DONE: 36. Devuelve la conversion de grados a radianes de 'degrees'.
def getRadianes(degrees: float) -> float:
    radians = math.radians(degrees)
    print(f"Pasar de Grados = {degrees} a Radianes = {radians}")
    return radians


# Constantes
# DONE: 37. Devuelve la constante matemática π = 3.141592….
def getPI() -> float:
    print(f"Numero π = {math.pi}")
    return math.pi


# DONE: 38. Devuelve la constante matemática e = 2.718281….
def gete() -> float:
    print(f"Numero e = {math.e}")
    return math.e


# Ecuacion
# DONE: 39. Devuelve el Ecuacion de 2º grado de 'nUno', 'nDos', 'nTres'.
def ecuacionSegundoGrado(nUno: float, nDos: float, nTres: float) -> tuple:
    if nUno == 0:
        print("El coeficiente a no puede ser igual a cero")
    else:
        discriminante = math.pow(nDos, 2) - (4 * nUno * nTres)
        if discriminante >= 0:
            if discriminante == 0:
                resultado = -nDos / (2 * nUno)
                print(f"La raíz única es {resultado}")
                return (resultado, 0)
            else:
                valor1 = ((-nDos) + math.sqrt(discriminante)) / (2 * nUno)
                valor2 = ((-nDos) - math.sqrt(discriminante)) / (2 * nUno)
                print(f"La raíz real (+) es = {valor1}")
                print(f"La raíz real (-) es = {valor2}")
                return (valor1, valor2)
        else:
            discriminante = math.fabs(discriminante)
            pImaginaria = math.sqrt(discriminante) / (2 * nUno)
            pReal = -nDos / (2 * nUno)
            print(f"La raíz compleja (+) es {pReal} + {pImaginaria}")
            print(f"La raíz compleja (-) es {pReal} - {pImaginaria}")
            return (pReal, pImaginaria)


# DONE: 40. Devuelve la Ecuacion cuadratica de 'nUno', 'nDos', 'nTres'.
def ecuacionCuadratica(nUno: float, nDos: float, nTres: float) -> tuple:
    ecuacion = ecuacionSegundoGrado(nUno, nDos, nTres)
    ecuacion = (math.pow(ecuacion[0], 2), math.pow(ecuacion[1], 2))
    print(f"Ecuacion Cuadratica (+)= {ecuacion[0]}")
    print(f"Ecuacion Cuadratica (-)= {ecuacion[1]}")
    return ecuacion


# Otros
# DONE: 41. Devuelve el Valor absoluto de 'nUno'.
def absoluto(nUno: float) -> float:
    resultado = math.fabs(nUno)
    print(f"Valor Absoluto = {nUno}! = {resultado}")
    return resultado


# DONE: 42. Devuelve la conversion de decimales a Fraccion de 'decimales'.
def getFraccion(decimales: float) -> Fraction:
    fraccion = Fraction(decimales)
    print(f"Convertir Decimal {decimales} a Fraccion = {fraccion}")
    return fraccion


# DONE: 43. Devuelve la conversion de Fraccion a decimales de 'fraccion'.
def getDecimal(fraccion: Fraction) -> float:
    decimales = float(fraccion)
    print(f"Convertir Fraccion {fraccion} a Decimal = {decimales}")
    return decimales


# DONE: 44. Devuelve la conversion de un numero a Binario de 'valor'.
def getBinario(valor: int) -> str:
    res = valor
    binario = ""
    while valor > 0:
        if (valor % 2) == 0:
            binario = "0" + binario
        else:
            binario = "1" + binario
        valor = int(valor / 2)
    print(f"Convertir numero {res} a Binario = {binario}")
    return binario


# DONE: 45. Devuelve los decimales de Binario a un numero de 'binario'.
def getRetornarBinario(binario: str) -> str:
    resultado = 0
    j = 0
    for i in binario[::-1]:
        if i == "1":
            resultado += int(math.pow(2, j))
        j += 1
    print(f"Convertir Binario {binario} a numero = {resultado}")
    return resultado


# Inicio
opcion = -1

while opcion < 0 or opcion > 45:
    print("*****************Calculadora*****************\n" +
          "00. SALIR\n"
          "*************Operaciones Basicas*************\n" +
          "01. Sumar\n" +
          "02. Restar\n" +
          "03. Multiplicar\n" +
          "04. Dividir\n" +
          "05. Dividion Modular\n" +
          "******Potencia y funciones logarítmicas******\n" +
          "06. Potencia\n" +
          "07. Exponencial\n" +
          "08. Logaritmo Neperiano\n" +
          "09. Logaritmo de base 10\n" +
          "10. Raiz Cuadrada\n" +
          "**********Funciones trigonométricas**********\n" +
          "11. Coseno\n" +
          "12. ArcoCoseno\n" +
          "13. Seno\n" +
          "14. ArcoSeno\n" +
          "15. Tangente\n" +
          "16. ArcoTangente\n" +
          "17. Cosecante\n" +
          "18. ArcoCosecante\n" +
          "19. Secante\n" +
          "20. ArcoSecante\n" +
          "21. Cotangente\n" +
          "22. ArcoCotangente\n" +
          "***********Funciones hiperbólicas************\n" +
          "23. Coseno Hiperbolico\n" +
          "24. ArcoCoseno Hiperbolico\n" +
          "25. Seno Hiperbolico\n" +
          "26. ArcoSeno Hiperbolico\n" +
          "27. Tangente Hiperbolico\n" +
          "28. ArcoTangente Hiperbolico\n" +
          "29. Cosecante Hiperbolico\n" +
          "30. ArcoCosecante Hiperbolico\n" +
          "31. Secante Hiperbolico\n" +
          "32. ArcoSecante Hiperbolico\n" +
          "33. Cotangente Hiperbolico\n" +
          "34. ArcoCotangente Hiperbolico\n" +
          "*************Conversión angular**************\n" +
          "35. Pasar de Radianes a Grados\n" +
          "36. Pasar de Grados a Radianes\n" +
          "**************Constantes*********************\n" +
          "37. Numero π\n" +
          "38. Numero e\n" +
          "******************Ecuacion*******************\n" +
          "39. Ecuacion de Segundo Grado\n" +
          "40. Ecuacion Cuadratica\n" +
          "********************Otros********************\n" +
          "41. Valor Absoluto\n" +
          "42. Convertir Decimal a Fraccion\n" +
          "43. Convertir Fraccion a Decimal\n" +
          "44. Convertir valor a Binario\n" +
          "45. Convertir Binario a valor")
    try:
        opcion = float(input("Ingrese una opcion (00-45): "))
        if opcion == 0:
            print("Gracia por su participacion")
        elif opcion < 0: 
            print("La opcion debe ser mayor a 0")
        elif opcion > 45: 
            print("La opcion debe ser menor o igual a 45")
    except Exception as exception:
        print(f"Error: Debe ingresar un numero entero")
    finally:
        time.sleep(2)

if opcion == 1:
    print("****Suma de dos valores")
    nUno = float(input("Ingrese el valor 1: "))
    nDos = float(input("Ingrese el valor 2: "))
    suma(nUno, nDos)
elif opcion == 2:
    print("****Resta de dos valores")
    nUno = float(input("Ingrese el valor 1: "))
    nDos = float(input("Ingrese el valor 2: "))
    resta(nUno, nDos)
elif opcion == 3:
    print("****Multiplicacion de dos valores")
    factor1 = float(input("Ingrese el valor 1: "))
    factor2 = float(input("Ingrese el valor 2: "))
    Multiplicacion(factor1, factor2)
elif opcion == 4:
    print("****Division de dos valores")
    dividendo = float(input("Ingrese el numerador: "))
    divisor = float(input("Ingrese el divisor: "))
    divicion(dividendo, divisor)
elif opcion == 5:
    print("****Division modular de dos valores")
    dividendo = float(input("Ingrese el numerador: "))
    divisor = float(input("Ingrese el divisor: "))
    dividirModular(dividendo, divisor)
elif opcion == 6:
    print("****Potencia")
    base = float(input("Ingrese la base: "))
    exponente = float(input("Ingrese el exponente: "))
    potenciacion(base, exponente)
elif opcion == 7:
    print("****Exponencial e")
    exponente = float(input("Ingrese el valor: "))
    potenciacionBasee(exponente)
elif opcion == 8:
    print("****Logaritmo Neperiano")
    argumento = float(input("Ingrese el valor: "))
    log(argumento)
elif opcion == 9:
    print("****Logaritmo de base 10")
    argumento = float(input("Ingrese el valor: "))
    log10(argumento)
elif opcion == 10:
    print("****Raiz Cuadrada")
    subradical = float(input("Ingrese el valor: "))
    raizCuadrada(subradical)
elif opcion == 11:
    print("****Coseno")
    nUno = float(input("Ingrese el valor: "))
    coseno(nUno)
elif opcion == 12:
    print("****ArcoCoseno")
    nUno = float(input("Ingrese el valor: "))
    arcocoseno(nUno)
elif opcion == 13:
    print("****Seno")
    nUno = float(input("Ingrese el valor: "))
    seno(nUno)
elif opcion == 14:
    print("****ArcoSeno")
    nUno = float(input("Ingrese el valor: "))
    arcoseno(nUno)
elif opcion == 15:
    print("****Tangente")
    nUno = float(input("Ingrese el valor: "))
    tangente(nUno)
elif opcion == 16:
    print("****ArcoTangente")
    nUno = float(input("Ingrese el valor: "))
    arcotangente(nUno)
elif opcion == 17:
    print("****Cosecante")
    nUno = float(input("Ingrese el valor: "))
    cosecante(nUno)
elif opcion == 18:
    print("****ArcoCosecante")
    nUno = float(input("Ingrese el valor: "))
    arcoCosecante(nUno)
elif opcion == 19:
    print("****Secante")
    nUno = float(input("Ingrese el valor: "))
    secante(nUno)
elif opcion == 20:
    print("****ArcoSecante")
    nUno = float(input("Ingrese el valor: "))
    arcoSecante(nUno)
elif opcion == 21:
    print("****Cotangente")
    nUno = float(input("Ingrese el valor: "))
    cotangente(nUno)
elif opcion == 22:
    print("****ArcoCotangente")
    nUno = float(input("Ingrese el valor: "))
    arcoCotangente(nUno)
elif opcion == 23:
    print("****Coseno Hiperbolico")
    nUno = float(input("Ingrese el valor: "))
    cosenoHiper(nUno)
elif opcion == 24:
    print("****ArcoCoseno Hiperbolico")
    nUno = float(input("Ingrese el valor: "))
    arcoCosenoHiper(nUno)
elif opcion == 25:
    print("****Seno Hiperbolico")
    nUno = float(input("Ingrese el valor: "))
    senoHiper(nUno)
elif opcion == 26:
    print("****ArcoSeno Hiperbolico")
    nUno = float(input("Ingrese el valor: "))
    arcoSenoHiper(nUno)
elif opcion == 27:
    print("****Tangente Hiperbolico")
    nUno = float(input("Ingrese el valor: "))
    tangenteHiper(nUno)
elif opcion == 28:
    print("****ArcoTangente Hiperbolico")
    nUno = float(input("Ingrese el valor: "))
    arcoTangenteHiper(nUno)
elif opcion == 29:
    print("****Cosecante Hiperbolico")
    nUno = float(input("Ingrese el valor: "))
    cosecanteHiper(nUno)
elif opcion == 30:
    print("****ArcoCosecante Hiperbolico")
    nUno = float(input("Ingrese el valor: "))
    arcoCosecanteHiper(nUno)
elif opcion == 31:
    print("****Secante Hiperbolico")
    nUno = float(input("Ingrese el valor: "))
    secanteHiper(nUno)
elif opcion == 32:
    print("****ArcoSecante Hiperbolico")
    nUno = float(input("Ingrese el valor: "))
    arcoSecanteHiper(nUno)
elif opcion == 33:
    print("****Cotangente Hiperbolico")
    nUno = float(input("Ingrese el valor: "))
    cotangenteHiper(nUno)
elif opcion == 34:
    print("****ArcoCotangente Hiperbolico")
    nUno = float(input("Ingrese el valor: "))
    arcoCotangenteHiper(nUno)
elif opcion == 35:
    print("****Pasar de Radianes a Grados")
    radianes = float(input("Ingrese los radianes: "))
    getGrados(radianes)
elif opcion == 36:
    print("****Pasar de Grados a Radianes")
    grados = float(input("Ingrese los grados: "))
    getRadianes(grados)
elif opcion == 37:
    print("****Numero π")
    getPI()
elif opcion == 38:
    print("****Numero e")
    gete()
elif opcion == 39:
    print("****Ecuacion de Segundo Grado")
    nA = float(input("Ingrese el valor a: "))
    nB = float(input("Ingrese el valor b: "))
    nC = float(input("Ingrese el valor c: "))
    ecuacionSegundoGrado(nA, nB, nC)
elif opcion == 40:
    print("****Ecuacion Cuadratica")
    nA = float(input("Ingrese el valor a: "))
    nB = float(input("Ingrese el valor b: "))
    nC = float(input("Ingrese el valor c: "))
    ecuacionCuadratica(nA, nB, nC)
elif opcion == 41:
    print("****Valor Absoluto")
    nUno = float(input("Ingrese el valor: "))
    absoluto(nUno)
elif opcion == 42:
    print("****Convertir Decimal a Fraccion")
    decimales = float(input("Ingrese los decimales: "))
    getFraccion(decimales)
elif opcion == 43:
    print("****Convertir Fraccion a Decimal")
    numerador = int(input("Ingrese el numerador: "))
    denominador = int(input("Ingrese el denominador: "))
    getDecimal(Fraction(numerador, denominador))
elif opcion == 44:
    print("****Convertir valor a Binario")
    valor = int(input("Ingrese el valor: "))
    getBinario(valor)
elif opcion == 45:
    print("****Convertir Binario a valor")
    binario = input("Ingrese el codigo Binario: ")
    getRetornarBinario(binario)
    