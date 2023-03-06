#se definirán las funciones correspondientes a las operaciones
#operación Suma
def suma(x,y):
    return x + y
#operación Resta
def resta (x,y):
    return x - y
# operación Multiplicación
def multi (x,y):
    return x * y
#operación División
def division (x,y):
    return x / y

# se le pedirá al usuario que ingrese 2 números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

#Se llama a las funciones para que realizan las operaciones definidas
res_suma = suma(numero1,numero2) #se pasa como parametro los numeros ingresados por el usuario
res_resta = resta(numero1, numero2)#se pasa como parametro los numeros ingresados por el usuario
res_multiplicacion = multi(numero1, numero2)#se pasa como parametro los numeros ingresados por el usuario
res_division = division(numero1, numero2)#se pasa como parametro los numeros ingresados por el usuario

#se imprimirán los resultados de las operaciones realizadas por las funciones
print("El resultado de la suma es: ", res_suma)
print("El resultado de la resta es: ", res_resta)
print("El resultado de la multplicación es: ", res_multiplicacion)
print("El resultado de la división es: ", res_division)