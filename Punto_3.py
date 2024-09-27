import json
archivo = r"C:\Users\USUARIO\Documents\UNAL\Programacion de computadoras\Reto 13\archivo.json"

def deporte():
    deporte = str(input("Ingrese el nombre del deporte: "))
    with open(archivo, "r") as read_file:
        datos = dict(json.load(read_file))

    diccionario = {}

    for persona, info in datos.items():
        if deporte in info['deportes']: 
            diccionario["nombres"] = info["nombres"]
            diccionario["apellidos"] = info["apellidos"]
            print(f"Nombre completo: {diccionario["nombres"]} {diccionario["apellidos"]}")

def edades():
    x = int(input("Ingrese el limite inferior del rango de edades: "))
    y = int(input("Ingrese el limite superior del rango de edades"))
    with open(archivo, "r") as read_file: 
        datos =dict(json.load(read_file))
    
    diccionario = {}

    for persona in datos.items():
        if  int(persona["edad"]) in range(x,y):
            diccionario["nombres"] = persona["nombres"]
            diccionario["apellidos"] = persona["apellidos"]
            print(f"Nombre completo: {diccionario["nombres"]} {diccionario["apellidos"]}")

            
if __name__ == "__main__":
    deporte()
    edades()
