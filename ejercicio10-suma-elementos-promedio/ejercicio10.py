# Se pide al usuario que ingrese la cantidad de números que desea almacenar
cantidad = int(input("Indica la cantidad de números que tendrá el arreglo: "))

# Se crea un arreglo vacío  para llenarlo con la cantidad indicada por el usuario
arreglo = []

# Se pide al usuario que ingrese cada número y lo agregamos al arreglo
for i in range(cantidad):
    numero = int(input("Introduzca un número entero: "))
    arreglo.append(numero) # se usa esta función para agregar un elemento al final del arreglo

# Se calcula la suma de los elementos introducidos por el usuario dentro del arreglo
suma = 0
for numero in arreglo:
    suma += numero

# Se calcula el promedio de los elementos del arreglo
promedio = suma / cantidad

# Imprimimos el arreglo, la suma y el promedio
print("Los números que has ingresado son:")
for numero in arreglo:
    print(numero)#impresión de los elementos del arreglo

print("La suma de los elementos dentro del arreglo es de: ", suma)
print("El promedio de los elementos dentro del arreglo es de: ", promedio)