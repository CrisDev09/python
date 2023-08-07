# declaramos la lisa
numeros = []

# solicitamos el numero de elementos al usuario 
nun_element = int(input("digite el numero de elementos que desea en la lista\n"))

# iterador
i = 0

# usamos un while para recorer la lista y llenarala con los elementos
while i < nun_element:

    # pedimos el numero que deseamos guardar en la lista
    elemento = int(input(f"digite el elemento { i + 1 }\n"))

    # agregamos el elemento a la lista
    numeros.append(elemento)
    i += 1

# imprimimos los elementos de la lista
print(max(numeros))
