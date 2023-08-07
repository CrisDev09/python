"""build in"""

numeros = [12, 23, 45 ,46 , 89]

#encontrando un numero mayor en una lista usando el metodo max()
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrar un numero menor de una lista usando el metodo min()
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redorndear numeros con round()
numero  = round(12.4589898, 2)
print(numero)

#retorna  false -> 0, vacio, False, none.  True -> distinto 0, Ture, no vacio. cadenas no vacias bool()
resultado_booleano = bool()
print(resultado_booleano)

# retorna True si todos los valores son verdaderos all()
resultado_all = all([True, 12, 'hola'])
print(resultado_all)

