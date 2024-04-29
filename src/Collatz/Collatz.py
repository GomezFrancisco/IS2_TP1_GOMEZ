import matplotlib.pyplot as plt

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    start_numbers = range(1, 10001)
    convergence_iterations = []

    for num in start_numbers:
        sequence = collatz_sequence(num)
        convergence_iterations.append(len(sequence) - 1)

    plt.plot(start_numbers, convergence_iterations, '.')
    plt.xlabel('Número inicial de la secuencia')
    plt.ylabel('Iteraciones para converger')
    plt.title('Convergencia de la conjetura de Collatz para números entre 1 y 10000')
    plt.show()

if __name__ == "__main__":
    main()