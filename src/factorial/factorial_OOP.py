import sys

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

def run(min, max):
    if min < 1 or min > 60:
        print("Solo se aceptan valores entre 1 - 60 en para cualquier valor de entrada")
        sys.exit(1)
    if max < 1 or max > 60:
        print("Solo se aceptan valores entre 1 - 60 para cualquier valor de entrada")
        sys.exit(1)

    if min >= max:
        print("El primer número debe ser menor que el segundo número en el rango.")
        sys.exit(1)

    for num in range(min, max + 1):
        print("Factorial de", num, "! es", factorial(num))

if len(sys.argv) < 2:
    print("Debe ingresar dos numeros")
    sys.exit(1)

numeros = sys.argv[1].split('-')
desde = int(numeros[0])
hasta = int(numeros[1])

run(desde, hasta)
