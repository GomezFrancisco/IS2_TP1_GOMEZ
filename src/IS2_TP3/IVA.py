from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}\n"
        return result

class FacturaIVAResponsableCreator(Creator):
    def factory_method(self) -> Product:
        return FacturaIVAResponsable()

class FacturaIVAExentoCreator(Creator):
    def factory_method(self) -> Product:
        return FacturaIVAExento()

class FacturaIVANoInscriptoCreator(Creator):
    def factory_method(self) -> Product:
        return FacturaIVANoInscripto()

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class FacturaIVAResponsable(Product):
    def operation(self) -> str:
        return "{Factura para IVA Responsable}"

class FacturaIVANoInscripto(Product):
    def operation(self) -> str:
        return "{Factura para IVA No Inscripto}"

class FacturaIVAExento(Product):
    def operation(self) -> str:
        return "{Factura para IVA Exento}"


def client_code(creator: Creator) -> None:
    print(f"Yo soy un mero intermediario tipo FACTORY que no se que es lo que estoy creando, pero lo creo.\n"
        f"{creator.some_operation()}", end="")

if __name__ == "__main__":
    print("\n\n")
    print("App: Creando una factura para IVA Responsable")
    client_code(FacturaIVAResponsableCreator())
    print("\n")

    print("App: Creando una factura para IVA No Inscripto")
    client_code(FacturaIVANoInscriptoCreator())
    print("\n")

    print("App: Creando una factura para IVA Exento")
    client_code(FacturaIVAExentoCreator())