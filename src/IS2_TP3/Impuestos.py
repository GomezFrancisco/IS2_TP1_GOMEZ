class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ImpuestosCalculator(metaclass=SingletonMeta):
    def impuesto(self, n):
        IVA = n * 0.21
        IIBB = n * 0.05
        IM = n * 0.012
        TOTAL = IVA + IIBB + IM
        return TOTAL
    
if __name__ == "__main__":
    calculator1 = ImpuestosCalculator()
    calculator2 = ImpuestosCalculator()
    print('Ingrese el monto que quiere calcular: ')
    importe = int(input())

    if id(calculator1) == id(calculator2):
        print("Sobre la base $", importe, " le corresponde una carga impositiva de $", calculator1.impuesto(importe))
    else:
        print("Singleton failed, variables contain different instances.")