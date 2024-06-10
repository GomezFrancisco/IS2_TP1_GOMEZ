import json
import sys
import threading

class JSONHandler:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, jsonfile):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(JSONHandler, cls).__new__(cls)
                    cls._instance.jsonfile = jsonfile
        return cls._instance

    def get_value(self, jsonkey):
        try:
            with open(self.jsonfile, 'r') as myfile:
                data = myfile.read()
                obj = json.loads(data)
                if jsonkey in obj:
                    return obj[jsonkey]
                else:
                    return None
        except FileNotFoundError:
            return f"El archivo '{self.jsonfile}' no existe."
        except json.JSONDecodeError:
            return f"El archivo '{self.jsonfile}' no es un JSON válido."

class JSONPrinter:
    def __init__(self, json_handler):
        self.json_handler = json_handler

    def print_value(self, jsonkey):
        result = self.json_handler.get_value(jsonkey)
        if result is not None:
            print(f"{{1.0}}{result}")
        else:
            print(f"No se encontró la clave '{jsonkey}' en el archivo JSON.")

def main():
    if len(sys.argv) != 3:
        print("Uso: python getJason.py <archivo.json> <clave>")
        return

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2]

    json_handler = JSONHandler(jsonfile)
    json_printer = JSONPrinter(json_handler)
    json_printer.print_value(jsonkey)

if __name__ == "__main__":
    main()
