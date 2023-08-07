# iterar listas con for
animales = ["perro", "gato", "perico", "pajaro"]
numeros = [12, 34, 44, 46]


for animal in animales:
    descripcion = f'esta especie de animal es {animal}'
    print(descripcion)


for numero in numeros:
    resultado = numero * 10
    print(resultado)


# para iterar dos o mas listas al mismo tiempo se usa zip() cada lista debe tener
# el mismo numero de elemento para que esto funcione
for numero, animal in zip(numeros, animales):
    text1 = f"resusltados de la primera lista {numero}"
    text2 = f"resuldatos de la segunda lista {animal}"

    print(text1 + text2)

# como usar el metodo range en un for esto imprime los elementos especificados en range

# forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])

# forma optima de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es {indice} y el valor es {valor}")




#WHile 
frutas = ["manzana", "papaya", "mango", "uva"]

#con len tomamos el numero de elementos que contiene la lista
elementos = len(frutas)

#iterador
i = 0 
#bucle
while i < elementos:
    print(frutas[i])
    i += 1

