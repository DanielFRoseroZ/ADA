# def counting_sort(arr):
#     # Encontrar el rango máximo del arreglo
#     max_val = max(arr) + 1

#     # Inicializar un arreglo de conteo con ceros
#     count = [0] * max_val

#     # Contar la frecuencia de cada elemento en el arreglo de entrada
#     for num in arr:
#         count[num] += 1

#     # Calcular las posiciones finales de cada elemento
#     for i in range(1, max_val):
#         count[i] += count[i - 1]

#     # Crear un arreglo de salida
#     output = [0] * len(arr)

#     # Colocar cada elemento en su posición correcta en el arreglo de salida
#     for num in arr:
#         output[count[num] - 1] = num
#         count[num] -= 1

#     return output

# #Ejemplo de uso
# arr = [4, 2, 2, 8, 3, 3, 1]
# sorted_arr = counting_sort(arr)
# print(sorted_arr)

# def insertion_sort(arr):
#     # Recorrer el arreglo desde el segundo elemento hasta el último
#     for i in range(1, len(arr)):
#         key = arr[i]  # Elemento actual a insertar en la posición correcta
#         j = i - 1  # Índice del elemento anterior

#         # Desplazar los elementos mayores hacia la derecha
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1

#         arr[j + 1] = key  # Insertar el elemento en la posición correcta

#     return arr

# # Ejemplo de uso
# arr = [3, 1, 2]
# sorted_arr = insertion_sort(arr)
# print(sorted_arr)