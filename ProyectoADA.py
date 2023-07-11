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
#La parte del espectaculo a la que pertenecen se asigna de forma arbitraria, este valor se utilizará luego para ordenar las escenas.
class Escena:

    def __init__(self, lista, parte):
        self.lista = lista
        self.parte = parte

    def __str__(self):
        return str(self.lista)

#----------------------FUNCIONES AUXILIARES----------------------#

def sum_escena(escena,animales):
    '''
    Funcion que suma la grandeza de los 3 animales que participan en una escena.
    Recibe como parametros una escena y el diccionario de animales con sus respectivas grandezas.
    Retorna la suma de las grandeza de los animales que participan en la escena.
    '''
    suma = 0
    for animal in escena.lista:
        suma += animales[animal]
    return suma

def max_escena(escena,animales):
    '''
    Funcion que retorna la grandeza del animal de mayor grandeza que participa en una escena.
    Recibe como parametros una escena y el diccionario de animales con sus respectivas grandezas.
    Retorna la suma de las grandeza de los animales que participan en la escena.
    '''
    maximo = animales[escena.lista[2]]
    return maximo

def ordenar_escena(escena, animales):
    '''
    Funcion que ordena los 3 animales que participan en una escena de forma ascendente.
    Recibe como parametros una escena y el diccionario de animales con sus respectivas grandezas.
    Retorna la escena con los animales ordenados de forma ascendente.
    '''
    #Ya que el numero de animales por escena es fijo, la complejidad de esta funcion es O(1).

    for i in range(1, len(escena.lista)):
        key = escena.lista[i]
        j = i-1
        while j >= 0 and animales[key] < animales[escena.lista[j]]:
            escena.lista[j+1] = escena.lista[j]
            escena.lista[j] = key
            j -= 1
        escena.lista[j+1] = key
    return escena

def suma_total_parte(parte, animales):
    '''
    Funcion que suma la grandeza de todas las escenas que hacen parte de una parte del espectaculo.
    Recibe como parametros una parte del espectaculo y el diccionario de animales con sus respectivas grandezas.
    Retorna la suma de las grandeza de todas las escenas que hacen parte de la parte del espectaculo.
    '''
    #Ya que esta función recorre la parte una unica vez y aplica la función sum_escena a cada escena, la complejidad de esta función es O(n).

    suma = 0
    for escena in parte:
        suma += sum_escena(escena, animales)
    return suma


#----------------------FUNCIONES PRINCIPALES DE ORDENAMIENTO----------------------#

def ordenar_escenas_entrada(entrada, animales):
    '''
    Funcion que ordena las escenas de la apertura aplicando la funcion ordenar_escena a cada escena que hace parte de la apertura.
    Recibe como parametros la apertura y el diccionario de animales con sus respectivas grandezas.
    Retorna la apertura con las escenas ordenadas.
    '''
    #Ya que esta función recorre la apertura una unica vez y aplica la función ordenar_escena a cada escena, la complejidad de esta función es O(n).

    entrada_ordenada = []
    for escena in entrada:
        parte_orden = ordenar_escena(escena,animales)
        entrada_ordenada.append(parte_orden)
    return entrada_ordenada

def ordenar_entrada_max_valor(entrada, animales):
    '''
    Funcion que ordena las escenas de la apertura segun el animal con mayor grandeza en cada escena, utilizando el algoritmo de ordenamiento Counting Sort.
    Recibe como parametros la apertura y el diccionario de animales con sus respectivas grandezas.
    Retorna la apertura con las escenas ordenadas segun lo establecido.
    '''
    #Ya que esta función ordena la apertura utilizando el algoritmo de ordenamiento Counting Sort, la complejidad de esta función es O(n).

    apertura = ordenar_escenas_entrada(entrada, animales)

    # # Almacenar la grandeza individual mas alta de cada escena que hace parte de la apertura.
    max_escenas = []
    for escena in apertura:
        max_escenas.append(max_escena(escena, animales)) #Se recorre la apertura una unica vez encontrando la grandeza individual de cada escena, por lo que la complejidad de esta linea es O(n).

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
    '''
    Funcion que ordena las escenas de la apertura segun la grandeza total de las escenas que la componen, utilizando el algoritmo de ordenamiento Counting Sort.
    Recibe como parametros la apertura y el diccionario de animales con sus respectivas grandezas.
    Retorna la apertura con las escenas ordenadas segun lo establecido.
    Se entiende que la grandeza total de una escena es la suma de las grandezas individuales de cada animal que hace parte de la escena.
    '''

    #Ya que esta función ordena la apertura utilizando el algoritmo de ordenamiento Counting Sort, la complejidad de esta función es O(n).

    apertura = ordenar_entrada_max_valor(entrada, animales)

    # # Almacenar la grandeza total de cada escena que hace parte de la apertura.
    sum_escenas = []
    for escena in apertura:
        sum_escenas.append(sum_escena(escena,animales)) #Se recorre la apertura una unica vez encontrando la grandeza total de cada escena, por lo que la complejidad de esta linea es O(n).

    # # Encontrar el rango máximo del arreglo
    max_val = max(sum_escenas) + 1

    # # Inicializar un arreglo de conteo con ceros
    count = [0] * max_val

    # # Contar la frecuencia de cada elemento en el arreglo de entrada
    for num in sum_escenas:
        count[num] += 1

    # # Calcular las posiciones finales de cada elemento
    for i in range(1, max_val):
        count[i] += count[i - 1]

    apertura_ordenada = [0] * len(sum_escenas)

    i = len(sum_escenas) - 1

    # # Colocar cada elemento en su posición correcta en el arreglo de salida
    for num in sum_escenas[::-1]:
        apertura_ordenada[count[num] - 1] = apertura[i]
        i -= 1
        count[num] -= 1 

    return apertura_ordenada

def ordenar_partes(partes, animales):
    '''
    Funcion que ordena las partes segun la suma de la grandeza total de las escenas que la componen, utilizando el algoritmo de ordenamiento Counting Sort.
    Recibe como parametros las partes y el diccionario de animales con sus respectivas grandezas.
    Retorna las partes con las escenas ordenadas segun lo establecido.
    '''
    #Ya que esta función ordena las partes utilizando el algoritmo de ordenamiento Counting Sort, la complejidad de esta función es O(n).

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

#----------------------LECTURA DE DATOS----------------------#
entrada = "./input.txt"
# Leer el archivo de entrada en una lista con las lineas
with open(entrada) as f:
    lineas = f.read().splitlines()

# Nombres de los animales
animales_b = lineas[6].split("animales = {")[1].split("}")[0]
# Grandezas de los animales
grandezas_b = lineas[8].split("grandezas = {")[1].split("}")[0]

# Crea el diccionario con los animales
animales_unir = animales_b.split(",")
grandezas_unir = grandezas_b.split(",")

animales = {}
for i, animal in enumerate(animales_unir):
    animales[animal.replace(" ", "")] = int(grandezas_unir[i])

# Cantidad de partes
m = int(lineas[2].split("m = ")[1][0])

# Crea una lista con todas las partes\
partes = []

for i in range(12, (m-1)*2+12, 2):
    sub_parte = []
    parte = lineas[i].split("parte = {{")[1].split("}}")[0]
    for parte in parte.split("}, {"):
        sub_parte.append(parte.split(", "))
    
    partes.append(sub_parte)

# Crea las escenas de cada parte
for i, parte in enumerate(partes):
    for j, escena in enumerate(parte):
        parte[j] = Escena(escena, i)

# Crea la apertura uniendo todas las partes
apertura = []
for parte in partes:
    apertura += parte
    
# ----------------------EJECUCION DEL ALGORITMO----------------------#
ordenada = ordenar_apertura(apertura, animales) # apertura ordenada

partes_ordenadas = [[] for i in range(len(partes))]

for escena in ordenada:
    partes_ordenadas[escena.parte].append(escena)   

#----------------------SALIDA DE DATOS----------------------#
print("El orden en el que se debe presentar el espectaculo es:")
# print("Apertura:", [(escena.lista, sum_escena(escena, animales)) for escena in ordenada])
print("Apertura:", [escena.lista for escena in ordenada])

partes2 = ordenar_partes(partes_ordenadas, animales)
for i, parte in enumerate(partes2):
    print("Parte", i+1, ":", [escena.lista for escena in parte], "Grandeza total:", suma_total_parte(partes2[i], animales))



#----------------------ESTADISTICOS----------------------#
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
    # Encontrar las escenas con la grandeza minima y maxima
    if grandeza == min_grandeza:
        escena_min_g.append(escena)
    if grandeza == max_grandeza:
        escena_max_g.append(escena)


max_participacion = float('-inf')
min_participacion = float('inf')
for key, value in participaciones.items():
    # Calcula el valor de mayor y menor participacion
    if value > max_participacion:
        max_participacion = value
    if value < min_participacion:
        min_participacion = value

animal_max_p = []
animal_min_p = []
for key, value in participaciones.items():
    # Encontrar los animales con la mayor y menor participacion
    if value == max_participacion:
        animal_max_p.append(key)
    if value == min_participacion:
        animal_min_p.append(key)

# Calcula el promedio de grandeza de todo el espectaculo
promedio_grandeza = 0
for escena in ordenada:
    promedio_grandeza += sum_escena(escena, animales)
promedio_grandeza /= len(ordenada)

#----------------------IMPRESION DE ESTADISTICOS----------------------#
print("El animal que participo en mas escenas dentro del espectaculo fue", animal_max_p, "con", max_participacion*2, "escenas")
print("El animal que menos participo en escenas dentro del espectaculo fue", animal_min_p, "con", min_participacion*2, "escenas")
print("La escena con menor grandeza total fue", [escena.lista for escena in escena_min_g], "con", min_grandeza, "grandeza total")
print("La escena con mayor grandeza total fue", [escena.lista for escena in escena_max_g], "con", max_grandeza, "grandeza total")
print("El promedio de grandeza total del espectaculo fue", promedio_grandeza)
