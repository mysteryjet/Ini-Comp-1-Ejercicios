# Se pide al usuario que ingrese la cantidad de números que desea almacenar
cantidad = int(input("Indica la cantidad de números que tendrá el arreglo: "))

# Se crea un arreglo vacío  para llenarlo con la cantidad indicada por el usuario
arreglo = []

# Se pide al usuario que ingrese cada número y lo agregamos al arreglo
for i in range(cantidad):
    numero = int(input("Introduzca un número entero: "))
    arreglo.append(numero) # se usa esta función para agregar un elemento al final del arreglo

# Imprimimos el arreglo utilizando un ciclo for
print("Los números que has ingresado son:")
for numero in arreglo:
    print(numero)
