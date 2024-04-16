class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class FactorialCalculator(metaclass=SingletonMeta):
    def factorial(self, n):
        if n == 0 or n==1:
            return 1
        elif n>1:
            return n * self.factorial(n-1)


if __name__ == "__main__":
    calculator1 = FactorialCalculator()
    calculator2 = FactorialCalculator()
    print('Ingrese el número a evaluar: ')
    numero = int(input())

    if id(calculator1) == id(calculator2):
        print("El factorial de ", numero, " es: ", calculator1.factorial(numero))
    else:
        print("Singleton failed, variables contain different instances.")