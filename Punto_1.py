def imprimir_valores():
    while True:
        try:
            cantidad_elementos: int = int(input("Por favor ingrese la cantidad de elementos(clave-valor) que va a tener el diccionario") )
        except ValueError:
            print("Por favor ingrese un numero entero.")
        break

    diccionario = {}

    for i in range(cantidad_elementos):
        clave = input("Por favor ingrese una clave: ")
        diccionario[clave] = input("Por favor ingresa el valor de esa clave:")

    valores = list(diccionario.values())
    valores_ordenados = sorted(valores)

    print(f"Los valores del diccionario ordenados de forma ascendente son {valores_ordenados}")

if __name__ == "__main__":
    imprimir_valores()