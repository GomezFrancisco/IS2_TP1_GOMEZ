import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.history = []

    def write(self, string):
        self.content += string

    def save(self):
        # Guarda el estado actual en el historial antes de guardar un nuevo estado
        self.history.append(Memento(self.file, self.content))
        # Limita el historial a los últimos 4 estados
        self.history = self.history[-4:]
        return Memento(self.file, self.content)

    def undo(self, memento, index=0):
        # Recupera el estado del historial basado en el índice proporcionado
        if len(self.history) > index:
            self.file = self.history[-1 - index].file
            self.content = self.history[-1 - index].content
        else:
            print("No hay suficientes estados guardados para deshacer a ese nivel.")

class FileWriterCaretaker:
    def save(self, writer):
        self.obj = writer.save()

    def undo(self, writer, index=0):
        writer.undo(self.obj, index)

if __name__ == '__main__':
    os.system("clear")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("se invoca al <undo>")
    caretaker.undo(writer, 0)

    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("se invoca al <undo>")
    caretaker.undo(writer, 1)

    print("Se muestra el estado actual")
    print(writer.content + "\n\n")
