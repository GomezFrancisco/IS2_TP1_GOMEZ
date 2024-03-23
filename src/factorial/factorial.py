#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

import sys

# Definición de la función factorial
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
    elif num == 0: 
        return 1
    else:
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Comprobamos que se haya ingresado al menos un argumento
if len(sys.argv) < 2:
    print("Debe ingresar dos numeros")
    sys.exit(1)

# Separamos los números ingresados con el guión
numeros = sys.argv[1].split('-')
# Convertimos los números a enteros
desde = int(numeros[0])
hasta = int(numeros[1])

# Comprobamos que los números ingresados estén en el rango permitido
if desde < 1 or desde > 60:
    print("Solo se aceptan valores entre 1 - 60 en para cualquier valor de entrada")
    sys.exit(1)
if hasta < 1 or hasta > 60:
    print("Solo se aceptan valores entre 1 - 60 para cualquier valor de entrada")
    sys.exit(1)

# Comprobamos que el primer número sea menor que el segundo
if desde >= hasta:
    print("El primer número debe ser menor que el segundo número en el rango.")
    sys.exit(1)

# Calculamos y mostramos el factorial de cada número en el rango
for num in range(desde, hasta + 1):
    print("Factorial de", num, "! es", factorial(num))
