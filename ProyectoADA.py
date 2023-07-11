# Para resolver el problema del zoologico
# Recorrer el arreglo de la apertura y a cada escena, ordenar sus elementos de menor a mayor
# Ordenar el arreglo de la apertura tomando como valor clave, el elemento de mayor valor de cada escena (el ultimo)
# Ordenar nuevamente el arreglo de la apertura tomando como valor clave, la suma de todos los valores de cada escena
# -----------------------------
# Una vez ordenada
# -----------------------------
# Counting sort: O(n) porque el valor mas grande del arreglo es 3n-3
# Recorrer el arreglo inicial y ordenar cada escena: O(3n)
# Ordenar el arreglo por grandeza individual: O(n)
# Ordenar el arreglo por grandeza total: O(n)
# -----------------------------
# Máximo valor que puede tomar n: indefinido
# Máximo número de escenas posibles: (n^3-3n^2+2n)/6
# Máximo valor que puede tomar m: depende de k en el mayor caso
# Máximo valor que puede tomar k: depende de m en el mayor caso 
# -----------------------------

#Se crea una clase escena, a la cual pertenecerán todas las escenas que hacen parte del espectaculo.
#Una escena cuenta con una lista de animales que participan en ella y la parte del espectaculo a la que pertenece.
#La parte del espectaculo a la que pertenecen se asigna de forma arbitraria, este valor se utilizará luego para ordenar las escenas. #CONCLUSION, SE HACE QUE TODOS LOS INPUTS SIGAN ESA ESTRUCTURA ESPECIFICA Y SE MENCIONA EN EL INFORME, QUE TODAS LAS ENTRADAS SIGUEN ESE FORMATO 
class Escena:

    def __init__(self, lista, parte):
        self.lista = lista
        self.parte = parte

    def __str__(self):
        return str(self.lista)

#----------------------FUNCIONES AUXILIARES----------------------#

#Funcion que suma la grandeza de los 3 animales que participan en una escena.
#Recibe como parametros una escena y el diccionario de animales con sus respectivas grandezas.
#Retorna la suma de las grandeza de los animales que participan en la escena.
def sum_escena(escena,animales):
    suma = 0
    for animal in escena.lista:
        suma += animales[animal]
    return suma

#Funcion que retorna el animal de mayor grandeza que participa en una escena.
#Recibe como parametros una escena y el diccionario de animales con sus respectivas grandezas.
#Retorna el animal de mayor grandeza que participa en la escena.
def max_escena(escena,animales):
    maximo = animales[escena.lista[2]]
    return maximo

#Funcion que ordena los 3 animales que participan en una escena de forma ascendente.
#Recibe como parametros una escena y el diccionario de animales con sus respectivas grandezas.
#Retorna la escena con los animales ordenados de forma ascendente.
#
def ordenar_escena(escena, animales):
    for i in range(1, len(escena.lista)):
        key = escena.lista[i]
        j = i-1
        while j >= 0 and animales[key] < animales[escena.lista[j]]:
            escena.lista[j+1] = escena.lista[j]
            escena.lista[j] = key
            j -= 1
        escena.lista[j+1] = key
    return escena

animales = {
    "Leon" : 9,
    "PanteraNegra" : 7,
    "Cebra" : 6,
    "Cocodrilo" : 5,
    "Boa" : 4,
    "Loro" : 2, 
    "Caiman" : 3,
    "Tigre" : 8,
    "Capibara" : 1,
}

partes = [
    [
        ["Caiman", "Capibara", "Loro"],
        ["Tigre", "Loro", "Capibara"],
        ["Tigre", "Cebra", "PanteraNegra"],
    ],
    [
        ["PanteraNegra", "Cocodrilo", "Loro"],
        ["Leon", "PanteraNegra", "Cebra"],
        ["Cocodrilo", "Capibara", "Loro"]
    ],
    [
        ["Boa", "Caiman", "Capibara"], 
        ["Leon", "Caiman", "Loro"],
        ["Leon", "Cocodrilo", "Boa"]
    ]
]

for i, parte in enumerate(partes):
    for j, escena in enumerate(parte):
        parte[j] = Escena(escena, i)

apertura = []
for parte in partes:
    apertura += parte

# ARREGLO ORDENADO
# ARREGLO P1
# ARREGLO P2

def ordenar_escenas_entrada(entrada, animales):
    gran_entrada = []
    for escena in entrada:
        entrada_ordenada = ordenar_escena(escena,animales)
        gran_entrada.append(entrada_ordenada)
    return gran_entrada

def ordenar_apertura_max_valor(entrada, animales):
    apertura = ordenar_escenas_entrada(entrada, animales)
    max_escenas = []
    for escena in apertura:
        max_escenas.append(max_escena(escena, animales))

    # # Encontrar el rango máximo del arreglo
    max_val = max(max_escenas) + 1

    # # Inicializar un arreglo de conteo con ceros
    count = [0] * max_val

    # # Contar la frecuencia de cada elemento en el arreglo de entrada
    for num in max_escenas:
        count[num] += 1

    # # Calcular las posiciones finales de cada elemento
    for i in range(1, max_val):
        count[i] += count[i - 1]
    
    apertura_ordenada = [0] * len(max_escenas)

    i = 0

    # # Colocar cada elemento en su posición correcta en el arreglo de salida
    for num in max_escenas:
        apertura_ordenada[count[num] - 1] = apertura[i]
        i += 1
        count[num] -= 1

    return apertura_ordenada

def ordenar_apertura(entrada, animales):
    apertura = ordenar_apertura_max_valor(entrada, animales)
    print("----DEBUG----")
    print([escena.lista for escena in apertura])
    sum_escenas = []
    for escena in apertura:
        sum_escenas.append(sum_escena(escena,animales))

    print(sum_escenas[::-1])
    # # Encontrar el rango máximo del arreglo
    max_val = max(sum_escenas) + 1

    # # Inicializar un arreglo de conteo con ceros
    count = [0] * max_val
    
    print("count", count)

    # # Contar la frecuencia de cada elemento en el arreglo de entrada
    for num in sum_escenas:
        count[num] += 1

    print("count2", count)

    # # Calcular las posiciones finales de cada elemento
    for i in range(1, max_val):
        count[i] += count[i - 1]

    print("count3", count)

    apertura_ordenada = [0] * len(sum_escenas)

    i = len(sum_escenas) - 1

    # # Colocar cada elemento en su posición correcta en el arreglo de salida
    for num in sum_escenas[::-1]:
        apertura_ordenada[count[num] - 1] = apertura[i]   #REGALARON EL ONLY DE UNA VIEJA QUE ESTA RE BUENA, QUE BENDICION ----PASELO---- AHI VOY, ESTA EN WPP
        i -= 1
        count[num] -= 1 
        print("count4", count, i+1)

    return apertura_ordenada

ordenada = ordenar_apertura(apertura, animales)

partes_ordenadas = [[] for i in range(len(partes))]

for escena in ordenada:
    partes_ordenadas[escena.parte].append(escena)   

def suma_total_parte(parte, animales):
    suma = 0
    for escena in parte:
        suma += sum_escena(escena, animales)
    return suma

def ordenar_partes(partes, animales):
    sum_partes = []
    for parte in partes:
        sum_partes.append(suma_total_parte(parte,animales))

    # # Encontrar el rango máximo del arreglo
    max_val = max(sum_partes) + 1

    # # Inicializar un arreglo de conteo con ceros
    count = [0] * max_val

    # # Contar la frecuencia de cada elemento en el arreglo de entrada
    for num in sum_partes:
        count[num] += 1

    # # Calcular las posiciones finales de cada elemento
    for i in range(1, max_val):
        count[i] += count[i - 1]

    partes_ordenadas = [0] * len(sum_partes)

    i = 0

    # # Colocar cada elemento en su posición correcta en el arreglo de salida
    for num in sum_partes:
        partes_ordenadas[count[num] - 1] = partes[i]
        i += 1
        count[num] -= 1

    return partes_ordenadas

print("Apertura")
print([(escena.lista, sum_escena(escena, animales)) for escena in ordenada])

print("Partes ordenadas por grandeza total")
partes2 = ordenar_partes(partes_ordenadas, animales)
for i, parte in enumerate(partes2):
    print("Parte", i+1, ":", [escena.lista for escena in parte], "Grandeza total:", suma_total_parte(partes2[i], animales))



# Estadisticas
participaciones = {}
for key in animales:
    participaciones[key] = 0

min_grandeza = float('inf')
max_grandeza = float('-inf')
for escena in ordenada:
    # Calcular las participaciones de cada animal
    for animal in escena.lista:
        participaciones[animal] += 1

    # Calcular la grandeza de la escena
    grandeza = sum_escena(escena, animales)
    if grandeza < min_grandeza:
        min_grandeza = grandeza
    if grandeza > max_grandeza:
        max_grandeza = grandeza

escena_min_g = []
escena_max_g = []
for escena in ordenada:
    grandeza = sum_escena(escena, animales)
    if grandeza == min_grandeza:
        escena_min_g.append(escena)
    if grandeza == max_grandeza:
        escena_max_g.append(escena)


max_participacion = float('-inf')
min_participacion = float('inf')
for key, value in participaciones.items():
    if value > max_participacion:
        max_participacion = value
    if value < min_participacion:
        min_participacion = value

animal_max_p = []
animal_min_p = []
for key, value in participaciones.items():
    if value == max_participacion:
        animal_max_p.append(key)
    if value == min_participacion:
        animal_min_p.append(key)

# Calcula el promedio de grandeza de todo el espectaculo
promedio_grandeza = 0
for escena in ordenada:
    promedio_grandeza += sum_escena(escena, animales)
promedio_grandeza /= len(ordenada)


print("El animal que participo en mas escenas fue", animal_max_p, "con", max_participacion*2, "escenas")
print("El animal que participo en menos escenas fue", animal_min_p, "con", min_participacion*2, "escenas")
print("La escena con menor grandeza total fue", [escena.lista for escena in escena_min_g], "con", min_grandeza, "grandeza total")
print("La escena con mayor grandeza total fue", [escena.lista for escena in escena_max_g], "con", max_grandeza, "grandeza total")
print("El promedio de grandeza total del espectaculo fue", promedio_grandeza)

