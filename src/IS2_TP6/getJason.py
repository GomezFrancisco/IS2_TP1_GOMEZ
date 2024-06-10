import json
import sys

def print_json_value(jsonfile, jsonkey):
    try:
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
            obj = json.loads(data)
            if jsonkey in obj:
                return obj[jsonkey]
            else:
                return None
    except FileNotFoundError:
        return f"El archivo '{jsonfile}' no existe."
    except json.JSONDecodeError:
        return f"El archivo '{jsonfile}' no es un JSON válido."

def main():
    if len(sys.argv) != 3:
        print("Uso: python getJason.py <archivo.json> <clave>")
        return

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2]
    result = print_json_value(jsonfile, jsonkey)

    if result is not None:
        print(f"{{1.0}}{result}")
    else:
        print(f"No se encontró la clave '{jsonkey}' en el archivo JSON.")

if __name__ == "__main__":
    main()
