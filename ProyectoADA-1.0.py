def ordenar_animales(animales):
    for i in range(len(animales)):
        max_index = i
        for j in range(i + 1, len(animales)):
            if animales[j][1] > animales[max_index][1]:
                max_index = j
        animales[i], animales[max_index] = animales[max_index], animales[i]

def generar_escenas(animales, m, k):
    escenas = []
    for i in range(m - 1):
        escenas_parte = []
        for j in range(k):
            escena = animales[j: j + 3]
            escenas_parte.append(escena)
        ordenar_escenas(escenas_parte)  # Ordenar las escenas de la parte actual
        escenas.extend(escenas_parte)
    return escenas

def ordenar_escenas(escenas):
    escenas.sort(key=lambda x: (sum(grandeza for _, grandeza in x), -max(grandeza for _, grandeza in x)))

def obtener_estadisticas(escenas):
    animales_participantes = {}
    escena_menor_grandeza = None
    escena_mayor_grandeza = None
    suma_grandezas = 0

    for escena in escenas:
        suma_grandezas += sum(grandeza for _, grandeza in escena)

        for animal in escena:
            nombre_animal = animal[0]
            if nombre_animal in animales_participantes:
                animales_participantes[nombre_animal] += 1
            else:
                animales_participantes[nombre_animal] = 1

        if escena_menor_grandeza is None or sum(grandeza for _, grandeza in escena) < sum(grandeza for _, grandeza in escena_menor_grandeza):
            escena_menor_grandeza = escena

        if escena_mayor_grandeza is None or sum(grandeza for _, grandeza in escena) > sum(grandeza for _, grandeza in escena_mayor_grandeza):
            escena_mayor_grandeza = escena

    return animales_participantes, escena_menor_grandeza, escena_mayor_grandeza, suma_grandezas / len(escenas)

# Ejemplo de uso
n = 10  # Número total de animales
m = 4   # Número total de partes del espectáculo
k = 3   # Número de animales por escena

# Generar lista de animales con sus grandezas
animales = [('Animal1', 5), ('Animal2', 9), ('Animal3', 2), ('Animal4', 7), ('Animal5', 4), ('Animal6', 8), ('Animal7', 1), ('Animal8', 3), ('Animal9', 6), ('Animal10', 10)]

# Ordenar animales según su grandeza
ordenar_animales(animales)

# Generar las escenas para las partes del espectáculo
escenas = generar_escenas(animales, m, k)

# Mostrar el resultado
print("Gran apertura:")
for escena in escenas[:k]:
    print(escena)

print("\nPartes siguientes:")
for escena in escenas[k:]:
    print(escena)

# Obtener estadísticas
animales_participantes, escena_menor_grandeza, escena_mayor_grandeza, promedio_grandezas = obtener_estadisticas(escenas)

print("\nAnimales que participaron en más escenas:")
max_participantes = max(animales_participantes.values())
animales_max_participantes = [animal for animal, participaciones in animales_participantes.items() if participaciones == max_participantes]
for animal in animales_max_participantes:
    print(f"{animal}: {max_participantes} escenas")

print("\nAnimales que participaron en menos escenas:")
min_participantes = min(animales_participantes.values())
animales_min_participantes = [animal for animal, participaciones in animales_participantes.items() if participaciones == min_participantes]
for animal in animales_min_participantes:
    print(f"{animal}: {min_participantes} escenas")

print("\nEscena de menor grandeza total:")
print(escena_menor_grandeza)

print("\nEscena de mayor grandeza total:")
print(escena_mayor_grandeza)

print("\nPromedio de grandeza de todo el espectáculo:")
print(promedio_grandezas)