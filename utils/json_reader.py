import json
from pathlib import Path

def read_full_json(file_path):
    """Lee un archivo JSON y retorna su contenido completo."""
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def read_json_file(file_path, key):
    """Lee un archivo JSON y extrae los valores asociados a una clave específica."""
    ruta = Path(file_path)
    with ruta.open("r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    if isinstance(data, list): # Comprobación de que 'data' es una lista para aplicar la comprensión de lista, si no, retorna todo el objeto
        extracted_values = [element[key] for element in data]
        return extracted_values
    else:
        print(f"Advertencia: El contenido de {file_path} no es una lista. Se retorna el objeto completo.")
        return data