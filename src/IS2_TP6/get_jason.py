'''
Programa de Gestión de Balances entre Bancos a través de tokens
'''
import json
import sys
import threading
import os

# Variable para alternar entre el código basado en funciones y el basado en clases
USE_CLASS_BASED_IMPLEMENTATION = True

# Versión del programa
VERSION = "1.2"

# Lista para almacenar los pagos realizados
pagos_realizados = []

class Pago:
    """
    Clase que representa un pago realizado.
    """
    def __init__(self, numero_pedido, token, monto):
        self.numero_pedido = numero_pedido
        self.token = token
        self.monto = monto

    def __str__(self):
        return f"Pedido {self.numero_pedido}: Token {self.token}, Monto ${self.monto}"

class PagoIterator:
    """
    Clase que implementa el patrón Iterator para iterar sobre los pagos realizados.
    """
    def __init__(self, pagos):
        self._pagos = pagos
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._pagos):
            pago = self._pagos[self._index]
            self._index += 1
            return pago
        raise StopIteration

# Implementación basada en funciones
def print_json_value(jsonfile, jsonkey, account_balance): 
    """
    Lee un archivo JSON y devuelve el valor asociado a una clave específica.
    
    :param jsonfile: Ruta del archivo JSON
    :param jsonkey: Clave del JSON cuyo valor se desea obtener
    :param account_balance: Saldo disponible en la cuenta
    :return: Valor asociado a la clave o None si no se encuentra la clave
    o si el archivo no existe o no es un JSON válido
    """
    try:
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
            obj = json.loads(data)
            value = obj.get(jsonkey)
            if value is not None and value <= account_balance:
                return value
            else:
                return "Saldo insuficiente o clave no encontrada."
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

    if len(sys.argv) == 2 and sys.argv[1] == "-l":
        listar_pagos()
        return

    if len(sys.argv) != 5:
        print("Uso: python getJason.py <archivo.json> <clave> <entidad_bancaria> <token>")
        print("Uso: python getJason.py -v para versiones")
        print("Uso: python getJason.py -l para listar pagos realizados")
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

    def get_value(self, jsonkey, bank_name, token):
        """
        Lee un archivo JSON y devuelve el valor asociado a una clave específica.

        :param jsonkey: Clave del JSON cuyo valor se desea obtener
        :param bank_name: Nombre del banco (token)
        :param token: Token para realizar el pago
        :return: Valor asociado a la clave o None si no se encuentra la clave,
        si el archivo no existe o si no es un JSON válido
        """
        try:
            bank_key = self.get_bank_key(bank_name)
            if bank_key is None:
                return "No se encontró la clave del banco en el archivo sitedata.json."

            with open(self.jsonfile, 'r') as myfile:
                data = myfile.read()
                obj = json.loads(data)
                return obj.get(bank_key, {}).get(jsonkey)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            return f"Error: {e}"
        except Exception as e:
            return f"Se produjo un error inesperado: {e}"
            
    def get_bank_key(self, bank_name):
        """
        Lee el archivo sitedata.json y devuelve la clave asociada al nombre del banco.

        :param bank_name: Nombre del banco (token)
        :return: Clave asociada al nombre del banco o None si no se encuentra el banco
        """
        try:
            with open("sitedata.json", 'r') as sitefile:
                data = sitefile.read()
                obj = json.loads(data)
                return obj.get(bank_name)
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

    def print_value(self, jsonkey, bank_name, token):
        """
        Imprime el valor asociado a una clave específica en el JSON.

        :param jsonkey: Clave del JSON cuyo valor se desea imprimir
        :param bank_name: Nombre del banco (token)
        :param token: Token para realizar el pago
        """
        result = self.json_handler.get_value(jsonkey, bank_name, token)
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

    if len(sys.argv) == 2 and sys.argv[1] == "-l":
        listar_pagos()
        return

    if len(sys.argv) != 5:
        print("Uso: python3 getJason.py <archivo.json> <clave> <entidad_bancaria> <token>")
        print("Uso: python getJason.py -v para versiones")
        print("Uso: python getJason.py -l para listar pagos realizados")
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

class Handler:
    """
    Clase base abstracta para los manejadores de la cadena de comando.
    """
    def __init__(self, successor=None):
        """
        Inicializa el manejador con un sucesor opcional en la cadena.

        :param successor: El siguiente manejador en la cadena de comando.
        """
        self._successor = successor

    def handle_request(self, bank_name, amount):
        """
        Maneja la solicitud o pasa la solicitud al siguiente manejador en la cadena.

        :param bank_name: Nombre del banco (token)
        :param amount: Monto de la transacción
        """
        if self._successor is not None:
            self._successor.handle_request(bank_name, amount)

    def set_successor(self, successor):
        """
        Establece el siguiente manejador en la cadena de comando.

        :param successor: El siguiente manejador en la cadena de comando.
        """
        self._successor = successor

class Token1Handler(Handler):
    """
    Manejador para la cuenta correspondiente a "token1".
    """
    def __init__(self, balance=1000):
        super().__init__()
        self.balance = balance

    def handle_request(self, bank_name, amount):
        if bank_name == "token1":
            if amount <= self.balance:
                self.balance -= amount
                pagos_realizados.append(Pago(len(pagos_realizados) + 1, bank_name, amount))
                print(f"Transacción exitosa. Pedido {len(pagos_realizados)}: Token {bank_name}, Monto ${amount}. Nuevo saldo: {self.balance}.")
            else:
                print("Saldo insuficiente para completar la transacción.")
        else:
            super().handle_request(bank_name, amount)

class Token2Handler(Handler):
    """
    Manejador para la cuenta correspondiente a "token2".
    """
    def __init__(self, balance=2000):
        super().__init__()
        self.balance = balance

    def handle_request(self, bank_name, amount):
        if bank_name == "token2":
            if amount <= self.balance:
                self.balance -= amount
                pagos_realizados.append(Pago(len(pagos_realizados) + 1, bank_name, amount))
                print(f"Transacción exitosa. Pedido {len(pagos_realizados)}: Token {bank_name}, Monto ${amount}. Nuevo saldo: {self.balance}.")
            else:
                print("Saldo insuficiente para completar la transacción.")
        else:
            super().handle_request(bank_name, amount)

def handle_transactions():
    """
    Maneja las transacciones entre los manejadores de tokens.
    """
    # Configuración de la cadena de comando
    token1_handler = Token1Handler()
    token2_handler = Token2Handler()

    # Establecer el siguiente manejador en la cadena
    token1_handler.set_successor(token2_handler)

    # Realizar pedidos de pago alternando entre las cuentas
    pedidos = [(i, 500) for i in range(1, 11)]  # 10 pedidos de $500 cada uno
    for i, (numero_pedido, monto) in enumerate(pedidos):
        if i % 2 == 0:
            token1_handler.handle_request("token1", monto)
        else:
            token1_handler.handle_request("token2", monto)

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        print(f"Versión {VERSION}")
        return

    if len(sys.argv) != 5:
        print("Uso: python getJason.py <archivo.json> <clave> <entidad_bancaria> <token>")
        print("Uso: python getJason.py -v para versiones")
        return

    if USE_CLASS_BASED_IMPLEMENTATION:
        main_class_based()
    else:
        main_function_based()

if __name__ == "__main__":
    main()
    # Realizar y listar transacciones
    handle_transactions()
    # Mensaje de derechos de autor
    print("copyright UADERFCyT-IS2©2024 todos los derechos reservados")
