# Se le pide al usuario que ingrese los valores numéricos
dividendo = float(input("Ingrese el dividendo: ")) #variable que guarda dividendo
divisor = float(input("Ingrese el divisor: "))#variable que guarda divisor

# Se revisa si el divisor es cero
if divisor == 0:
    print("Error. No es posible dividir entre cero.")#mensaje de error
else:
    # Realizamos la división y mostramos el resultado
    resultado = dividendo / divisor
    print("El resultado de la división es:", resultado)
