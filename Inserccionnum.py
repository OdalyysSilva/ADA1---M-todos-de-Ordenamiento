def insercion_sort(lista):
    for i in range(1, len(lista)): # Se recorre a partir del segundo elemento hasta el final
        actual = lista[i] # Se guarda el valor actual
        j = i - 1
        print(f"\nInsertando {actual} en la lista ordenada")
        # Mueve los elementos de la lista que son mayores que el valor "actual"
        # a una posición adelante para hacer espacio para "actual"
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
            print(f"Moviendo {lista[j + 1]} a la posición {j + 2}")

        lista[j + 1] = actual # Inserta el elemento actual en su posición correcta
        print(f"Colocando {actual} en la posición {j + 1}")
        print("Estado de la lista:", lista)
    return lista

numeros = list(map(int, input("Ingresa los números a ordenar, separados por espacios: ").split()))

print("\nLista original:", numeros) # Muestra la lista original

print("\nOrdenamiento por selección paso a paso:") # Ejecuta y muestra cada paso
insercion_sort(numeros)

print("\nLista ordenada:", numeros)  # Se despliega como queda la lista