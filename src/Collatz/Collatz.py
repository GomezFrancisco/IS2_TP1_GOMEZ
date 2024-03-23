import matplotlib.pyplot as plt

def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        sequence.append(n)
    return sequence

# Crear una lista para almacenar el número de iteraciones para cada número
iterations = []

# Calcular la secuencia de Collatz para cada número entre 1 y 10000
for i in range(1, 10001):
    sequence = collatz(i)
    iterations.append(len(sequence))

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(range(1, 10001), iterations)
plt.xlabel('Número inicial de la secuencia')
plt.ylabel('Número de iteraciones hasta converger')
plt.title('Número de iteraciones de la secuencia de Collatz para números del 1 al 10000')
plt.grid(True)
plt.show()