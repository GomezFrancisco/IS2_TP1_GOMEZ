from abc import ABC, abstractmethod
from datetime import datetime

# Define Prototypes
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Shopkeeper(Prototype):
    def __init__(self, height, age, defense, attack):
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        self.charisma = 30

    def clone(self):
        return type(self)(self.height, self.age, self.defense, self.attack)

class Warrior(Prototype):
    def __init__(self, height, age, defense, attack):
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        self.stamina = 60

    def clone(self):
        return type(self)(self.height, self.age, self.defense, self.attack)

class Mage(Prototype):
    def __init__(self, height, age, defense, attack):
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        self.mana = 100

    def clone(self):
        return type(self)(self.height, self.age, self.defense, self.attack)

# Main Program
print("Ejemplo de taller para patrón prototipo")

# Single Instances
print('Comienzo creando 20 objetos Shopkeeper NPC: ', datetime.now())
shopkeeper_template = Shopkeeper(180, 22, 5, 8)
shopkeepers = [shopkeeper_template.clone() for _ in range(20)]
print('Finaliza la creación de 20 objetos Shopkeeper NPC: ', datetime.now())

print('Comienzo creando 20 objetos Warrior NPC: ', datetime.now())
warrior_template = Warrior(185, 22, 4, 21)
warriors = [warrior_template.clone() for _ in range(20)]
print('Finaliza la creación de 20 objetos Warrior NPC: ', datetime.now())

print('Comienzo creando 20 objetos Mage NPC: ', datetime.now())
mage_template = Mage(172, 65, 8, 15)
mages = [mage_template.clone() for _ in range(20)]
print('Finaliza la creación de 20 objetos Mage NPC: ', datetime.now())

