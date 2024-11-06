def burbuja_sort(lista):
    n = len(lista)

    for i in range(n):
        print(f"\nPasada {i + 1}:")
        # En cada iteración, las palabras "mayores" van "flotando" hacia el final de la lista
        for j in range(0, n - i - 1):
            # Muestra la lista y los elementos que se están comparando
            print(f"Comparando lista[{j}] = '{lista[j]}' y lista[{j + 1}] = '{lista[j + 1]}'")
            # Se intercambia si el elemento es mayor que el siguiente
            if lista[j].lower() > lista[j + 1].lower():  # .lower() es para ignorar mayúsculas
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(f"Intercambiando lista[{j}] = '{lista[j]}' con lista[{j + 1}] = '{lista[j + 1]}'")
        print(f"Lista después de la pasada {i + 1}: {lista}") # Muestra como queda la lista después de cada paso
    return lista

nombres = input("Ingresa las palabras o nombres a ordenar, separados por espacios: ").split()

print("\nLista original: ", nombres) # Muestra la lista original

print("\nOrdenamiento por el metodo de burbuja: ")  # Ejecuta y muestra cada paso
burbuja_sort(nombres)

print("\nLista ordenada: ", nombres) # Se despliega como queda la lista
