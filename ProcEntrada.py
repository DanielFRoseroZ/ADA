with open('entrada.txt', 'r') as file:
    n = int(file.readline().strip())
    m = int(file.readline().strip())
    k = int(file.readline().strip())

    animales = {}
    for _ in range(n):
        linea = file.readline().strip().split() # Lee una linea y la separa por espacios
        nombre = linea[0] # Nombre del animal
        Grandeza = int(linea[1]) # Grandeza del animal
        animales[nombre] = Grandeza

    escenas = []
    for _ in range(m):
        escena = file.readline().strip()[1:-1].split('}, {')  # Lee una línea y la separa por espacios
        escena = [set(animal.strip() for animal in s.split(', ')) for s in escena]  # Separa cada animal de la escena
        # Asignar 'None' a los animales que no están en el diccionario
        escena = [[animal if animal in animales else None for animal in grupo] for grupo in escena]
        escenas.append(escena)  # Agrega la escena a la lista de escenas

# Imprimir la entrada
print("n:", n)
print("m:", m)
print("k:", k)
print("Animales:", animales)
print("Escenas:", escenas)