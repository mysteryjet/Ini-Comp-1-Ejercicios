contador = 0 #esta variable almacenará el numero de veces que un usuario ingrese un numero que no sea 0
num = int(input("Introduzca un número entero. Para finalizar, ingrese 0: "))

while num != 0:
    contador += 1
    num = int(input("Introduzca otro número entero.  Cuando desee finalizar, ingrese 0: "))

print("Se ingresaron un total de: ",contador, "números enteros antes de ingresar 0.")