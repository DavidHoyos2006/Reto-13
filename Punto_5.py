import json
import requests

# Función para imprimir pares clave : valor
def imprimir_pares(data):
    for key, value in data.items(): # Itera sobre los elementos del diccionario.
        print(f"{key}: {value}") # Imprime cada clave con su respectivo valor.

# API 1: Open Trivia Database
trivia_url = 'https://opentdb.com/api.php?amount=1'
trivia_response = requests.get(trivia_url) # Realiza la solicitud GET a la API.
if trivia_response.status_code == 200: # Se verifica si hubo una respuesta exitosa.
    trivia_data = trivia_response.json() # Convierte la respuesta en un diccionario de Python.
    print("Datos de la API Open trivia Database (Clima actual en Londres):")
    imprimir_pares(trivia_data) # Llama a la función para imprimir los datos de la API.
else:
    print(f"Error al acceder a Open Trivia Database") # Mensaje de error, por si la solicitud falla.

# API 2: Datos sobre la última misión espacial de SpaceX
spacex_url = "https://api.spacexdata.com/v4/launches/latest"
spacex_response = requests.get(spacex_url) # Realiza la solicitud GET a la API.
if spacex_response.status_code == 200: # Se verifica si hubo una respuesta exitosa.
    spacex_data = spacex_response.json() # Convierte la respuesta en un diccionario de Python.
    print("Datos de la API SpaceX (Último lanzamiento):")
    imprimir_pares(spacex_data) # Llama a la función para imprimir los datos de la API.
else:
    print(f"Error al acceder a SpaceX API") # Mensaje de error, por si la solicitud falla.


cripto_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd" #Se hace exactamente lo mismo que con las dos API anteriores.
cripto_response = requests.get(cripto_url) 
if cripto_response.status_code == 200: 
    cripto_data = cripto_response.json() 
    print("Datos de la API cripto:")
    imprimir_pares(cripto_data) 
else:
    print(f"Error al acceder a cripto") 
