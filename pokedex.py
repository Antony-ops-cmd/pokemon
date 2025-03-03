import requests
import json
import os

# URL base de la API de Pokémon
POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

# Función para obtener información del Pokémon
def obtener_pokemon(nombre):
    response = requests.get(POKEAPI_URL + nombre.lower())  # Convierte el nombre a minúsculas para evitar errores
    if response.status_code == 200:
        return response.json()  # Devuelve los datos en formato JSON
    elif response.status_code == 404:
        print("Error: Pokémon no encontrado.")
    else:
        print(f"Error al consultar la API: Código {response.status_code}")
    return None

# Función para mostrar la información del Pokémon
def mostrar_pokemon(datos):
    print("\nInformación del Pokémon:")
    print(f"Nombre: {datos['name'].capitalize()}")
    print(f"Peso: {datos['weight']}")
    print(f"Altura: {datos['height']}")

    # Obtener tipos
    tipos = [tipo['type']['name'] for tipo in datos['types']]
    print(f"Tipos: {', '.join(tipos)}")

    # Obtener habilidades
    habilidades = [habilidad['ability']['name'] for habilidad in datos['abilities']]
    print(f"Habilidades: {', '.join(habilidades)}")

    # Obtener algunos movimientos
    movimientos = [movimiento['move']['name'] for movimiento in datos['moves'][:5]]
    print(f"Movimientos: {', '.join(movimientos)}")

    # Mostrar imagen
    print(f"Imagen del Pokémon: {datos['sprites']['front_default']}")

# Función para guardar la información en un archivo JSON
def guardar_pokemon(datos):
    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")  # Crea la carpeta si no existe

    archivo_json = f"pokedex/{datos['name']}.json"
    with open(archivo_json, "w") as archivo:
        json.dump(datos, archivo, indent=4)
    print(f"\nDatos guardados en: {archivo_json}")

# Función principal
def main():
    nombre_pokemon = input("Ingresa el nombre de un Pokémon: ").strip()
    datos_pokemon = obtener_pokemon(nombre_pokemon)
    
    if datos_pokemon:
        mostrar_pokemon(datos_pokemon)
        guardar_pokemon(datos_pokemon)

# Ejecutar el programa
if __name__ == "__main__":
    main()

