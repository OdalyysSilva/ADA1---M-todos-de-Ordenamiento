def burbuja_sort(lista):
    n = len(lista)

    for i in range(n):
        print(f"\nPasada {i + 1}:")
        for j in range(0, n - i - 1): # En cada movimiento los valores mas grandes se van al final de la lista
            # Muestra la lista y los elementos que se están comparando
            print(f"Comparando lista[{j}] = {lista[j]} y lista[{j + 1}] = {lista[j + 1]}")
            if lista[j] > lista[j + 1]: # Intercambia los valores si el primero es mayor al comparar
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(f"Intercambiando lista[{j}] = {lista[j]} con lista[{j + 1}] = {lista[j + 1]}")
        print(f"Lista después de la pasada {i + 1}: {lista}") # Muestra como queda la lista después de cada paso
    return lista

num = list(map(int, input("Ingresa los números a ordenar, separados por espacios: ").split()))

print("\nLista original: ", num) # Muestra la lista original

print("\nOrdenamiento por el metodo de burbuja: ") # Ejecuta y muestra cada paso
burbuja_sort(num)

print("\nLista ordenada: ", num) # Se despliega como queda la lista
