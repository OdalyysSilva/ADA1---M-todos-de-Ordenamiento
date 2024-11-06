def seleccion_sort(lista):
    for i in range(len(lista)): # Reccorre la lista de inicio al final
        min_index = i # Se asigna al primer valor de la lista suponiendoq que es el minimo 
        print(f"\nPasada {i + 1}: Se busca el mínimo desde la posición {i}")
        # Comparamos ese valor minimo con el resto de los valores
        for j in range(i + 1, len(lista)):
            if lista[j].lower() < lista[min_index].lower():  # Compara ignorando mayúsculas
                min_index = j  # Actualiza el índice del mínimo si se encuentra un valor menor
            # Se muestra la lista y el valor mínimo encontrado
            print(f"Comparando lista[{j}] = '{lista[j]}' con lista[{min_index}] = '{lista[min_index]}'")
        # Intercambia el valor mínimo encontrado con el primer elemento del segmento
        lista[i], lista[min_index] = lista[min_index], lista[i]
        print(f"Intercambiando lista[{i}] = '{lista[i]}' con lista[{min_index}] = '{lista[min_index]}'")
        print(f"Lista después de la pasada {i + 1}: {lista}")
    return lista

nombres = input("Ingresa los nombres a ordenar, separados por espacios: ").split()

print("\nLista original: ", nombres) # Muestra la lista original

print("\nOrdenamiento por el metodo de selección: ") # Ejecuta y muestra cada paso
seleccion_sort(nombres)

print("\nLista ordenada: ", nombres)  # Se despliega como queda la lista
