def unir_diccionarios(diccionario1: dict, diccionario2: dict):
    diccionario_nuevo = {}  # Inicializa un nuevo diccionario vacío
    diccionario_nuevo.update(diccionario1)  # Copia todos los elementos de diccionario1 a diccionario_nuevo
    for key in diccionario2:  # Itera sobre cada clave en diccionario2
        if key not in diccionario_nuevo:  # Si la clave no está en diccionario_nuevo
            diccionario_nuevo[key] = diccionario2[key]  # Añade la clave y su valor correspondiente de diccionario2 a diccionario_nuevo
        else:
            continue  # Si la clave ya está en diccionario_nuevo, no hace nada y continúa con la siguiente clave
    return diccionario_nuevo  # Devuelve el diccionario combinado

if __name__ == "__main__":
    diccionario = {
        "david" : 17,
        "isabella" : 18,
        "carlos": 60,
        "juan": 27,
        "maria jose": 20 
    }

    diccionario1 = {
        "david" : 21,
        "mariana" : 18,
        "diego": 60,
        "juan": 32,
        "ariana": 20 
    }
    # Imprime el diccionario resultante de unir diccionario y diccionario1
    print(f"El diccionario resultante es {unir_diccionarios(diccionario, diccionario1)}")

