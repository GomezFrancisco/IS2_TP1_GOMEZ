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

class HamburguesaMostradorCreator(Creator):
    def factory_method(self) -> Product:
        return HamburguesaMostrador()

class HamburguesaRetiroCreator(Creator):
    def factory_method(self) -> Product:
        return HamburguesaRetiro()

class HamburguesaDeliveryCreator(Creator):
    def factory_method(self) -> Product:
        return HamburguesaDelivery()

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class HamburguesaMostrador(Product):
    def operation(self) -> str:
        return "{Hamburguesa para entregar en mostrador}"

class HamburguesaRetiro(Product):
    def operation(self) -> str:
        return "{Hamburguesa para retirar por el cliente}"

class HamburguesaDelivery(Product):
    def operation(self) -> str:
        return "{Hamburguesa para enviar por delivery}"

def client_code(creator: Creator) -> None:
    print(f"Yo soy un mero intermediario tipo FACTORY que no se que es lo que estoy creando, pero lo creo.\n"
          f"{creator.some_operation()}", end="")

if __name__ == "__main__":
    print("\n\n")
    print("App: Creando una hamburguesa para entregar en mostrador")
    client_code(HamburguesaMostradorCreator())
    print("\n")

    print("App: Creando una hamburguesa para retirar por el cliente")
    client_code(HamburguesaRetiroCreator())
    print("\n")

    print("App: Creando una hamburguesa para enviar por delivery")
    client_code(HamburguesaDeliveryCreator())