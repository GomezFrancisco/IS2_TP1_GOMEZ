import json
import sys
import threading
import os

# Variable para alternar entre el código basado en funciones y el basado en clases
USE_CLASS_BASED_IMPLEMENTATION = True

# Versión del programa
VERSION = "1.2"

# Implementación basada en funciones
def print_json_value(jsonfile, jsonkey, entity, token):
    """
    Lee un archivo JSON y devuelve el valor asociado a una clave específica.
    
    :param jsonfile: Ruta del archivo JSON
    :param jsonkey: Clave del JSON cuyo valor se desea obtener
    :param entity: Entidad bancaria para realizar el pago
    :param token: Token para realizar el pago
    :return: Valor asociado a la clave o None si no se encuentra la clave
    o si el archivo no existe o no es un JSON válido
    """
    try:
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
            obj = json.loads(data)
            return obj.get(jsonkey)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Se produjo un error inesperado: {e}"


def main_function_based():
    """
    Función principal para la implementación basada en funciones.
    Verifica los argumentos de línea de comandos y muestra el valor del JSON.
    """
    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        print(f"Versión {VERSION}")
        return

    if len(sys.argv) != 5:
        print("Uso: python getJason.py <archivo.json> <clave> <entidad_bancaria> <token> o python getJason.py -v")
        return

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2]
    entity = sys.argv[3]
    token = sys.argv[4]

    if not os.path.isfile(jsonfile):
        print(f"El archivo '{jsonfile}' no existe.")
        return

    if not jsonfile.endswith('.json'):
        print("El archivo especificado no tiene una extensión '.json'.")
        return

    result = print_json_value(jsonfile, jsonkey, entity, token)

    if result is not None:
        print(f"{{1.0}}{result}")
    else:
        print(f"No se encontró la clave '{jsonkey}' en el archivo JSON.")

# Implementación basada en clases (Singleton)
class JSONHandler:
    """
    Manejador de las clases Singleton
    """
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, jsonfile):
        """
        Implementación del patrón Singleton. Asegura que solo haya una instancia de JSONHandler.
        
        :param jsonfile: Ruta del archivo JSON
        :return: La única instancia de JSONHandler
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(JSONHandler, cls).__new__(cls)
                    cls._instance.jsonfile = jsonfile
        return cls._instance

    def get_value(self, jsonkey, entity, token):
        """
        Lee un archivo JSON y devuelve el valor asociado a una clave específica.
    
        :param jsonkey: Clave del JSON cuyo valor se desea obtener
        :param entity: Entidad bancaria para realizar el pago
        :param token: Token para realizar el pago
        :return: Valor asociado a la clave o None si no se encuentra la clave,
        si el archivo no existe o si no es un JSON válido
        """
        try:
            with open(self.jsonfile, 'r') as myfile:
                data = myfile.read()
                obj = json.loads(data)
                return obj.get(jsonkey)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            return f"Error: {e}"
        except Exception as e:
            return f"Se produjo un error inesperado: {e}"


class JSONPrinter:
    def __init__(self, json_handler):
        """
        Inicializa JSONPrinter con una instancia de JSONHandler.
        
        :param json_handler: Instancia de JSONHandler
        """
        self.json_handler = json_handler

    def print_value(self, jsonkey, entity, token):
        """
        Imprime el valor asociado a una clave específica en el JSON.
        
        :param jsonkey: Clave del JSON cuyo valor se desea imprimir
        :param entity: Entidad bancaria para realizar el pago
        :param token: Token para realizar el pago
        """
        result = self.json_handler.get_value(jsonkey, entity, token)
        if result is not None:
            print(f"{{1.0}}{result}")
        else:
            print(f"No se encontró la clave '{jsonkey}' en el archivo JSON.")


def main_class_based():
    """
    Función principal para la implementación basada en clases.
    Verifica los argumentos de línea de comandos y muestra el valor del JSON.
    """
    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        print(f"Versión {VERSION}")
        return

    if len(sys.argv) != 5:
        print("Uso: python getJason.py <archivo.json> <clave> <entidad_bancaria> <token> o python getJason.py -v")
        return

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2]

    if not os.path.isfile(jsonfile):
        print(f"El archivo '{jsonfile}' no existe.")
        return

    if not jsonfile.endswith('.json'):
        print("El archivo especificado no tiene una extensión '.json'.")
        return

    entity = sys.argv[3]
    token = sys.argv[4]

    try:
        json_handler = JSONHandler(jsonfile)
        json_printer = JSONPrinter(json_handler)
        json_printer.print_value(jsonkey, entity, token)
    except Exception as e:
        print(f"Se produjo un error inesperado al procesar el archivo JSON: {e}")

if __name__ == "__main__":
    if USE_CLASS_BASED_IMPLEMENTATION:
        main_class_based()
    else:
        main_function_based()

    # Mensaje de derechos de autor
    print("copyright UADERFCyT-IS2©2024 todos los derechos reservados")
