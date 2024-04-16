import os

class Director:
    __builder = None
    
    def setBuilder(self, builder):
        self.__builder = builder
	    
    def getPlane(self):
        plane = Plane()

        undercarriage = self.__builder.getUndercarriage()
        plane.setUndercarriage(undercarriage)

        i = 0
        while i < 2:
            turbines = self.__builder.getTurbines()
            plane.attachTurbines(turbines)
            i += 1

        j = 0
        while j < 2:
            wings = self.__builder.getWings()
            plane.attachWings(wings)
            j += 1

        body = self.__builder.getBody()
        plane.setBody(body)

        return plane


class Plane:
    def __init__(self):
        self.__wings = list()
        self.__turbines = list()
        self.__undercarriage = None
        self.__body = None

    def attachWings(self, wings):
        self.__wings.append(wings)

    def attachTurbines(self, turbines):
        self.__turbines.append(turbines)

    def setUndercarriage(self, undercarriage):
        self.__undercarriage = undercarriage

    def setBody(self, body):
        self.__body = body

    def specification(self):
        print ("Forma del tren de aterrizaje: %s" % (self.__undercarriage.forma))
        print ("Tamaño de alas: %d\'" % (self.__wings[0].tamanio))
        print ("Span de alas: %d\'" % (self.__wings[0].span))
        print ("Tamaño de las turbinas: %d\'" % (self.__turbines[0].tamanio))
        print ("Caballos de fuerza de turbinas: %d\'" % (self.__turbines[0].horsepower))
        print ("Forma del cuerpo: %s" % (self.__body.forma))
        print ("Material del cuerpo: %s" % (self.__body.material))
        print ("Longitud del cuerpo: %s" % (self.__body.largo))

class Builder:
    def getUndercarriage(self): pass
    def getTurbines(self): pass
    def getWings(self): pass
    def getBody(self): pass

class PlaneBuilder(Builder):
    
    def getUndercarriage(self):
        gear = Undercarriage()
        gear.forma = "Retractiles"
        return gear
    
    def getTurbines(self):
        turb = Turbine()
        turb.horsepower = 10000
        turb.tamanio = 22 
        return turb
    
    def getWings(self):
        wing = Wings()
        wing.span = 60
        wing.tamanio = 22  
        return wing
    
    def getBody(self):
        body = Body()
        body.forma = "Cilíndrica"
        body.material = "Titanio"
        body.largo = 65  # en metros
        return body


class Undercarriage:
    forma = None

class Turbine:
    horsepower = None
    tamanio = None

class Wings:
    span = None
    tamanio = None

class Body:
    forma = None
    material = None
    largo = None

def main():

    planeBuilder = PlaneBuilder() # initializing the class
    director = Director() 
    director.setBuilder(planeBuilder)
    plane = director.getPlane()
    plane.specification()
    print ("\n\n")

if __name__ == "__main__":
    os.system("cls")
    print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avión\n")

    main()