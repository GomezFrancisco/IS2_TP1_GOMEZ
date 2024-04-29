import os

class State:
    def __init__(self):
        self.stations = {"M1": None, "M2": None, "M3": None, "M4": None}
        self.pos = 0
        self.name = ""

    def scan(self):
        keys = list(self.stations.keys())
        self.pos += 1
        if self.pos == len(keys):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[keys[self.pos]], self.name))

class AmState(State):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.stations = {"M1": "1250", "M2": "1380", "M3": "1510", "M4": "1620"}
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

class FmState(State):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.stations = {"M1": "81.3", "M2": "89.1", "M3": "103.9", "M4": "107.7"}
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 4 + [radio.toggle_amfm] + [radio.scan] * 4
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()
