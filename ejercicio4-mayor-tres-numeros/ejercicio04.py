n1 = float(input("Ingrese el primer número: ")) # aqui se almacena el primer numero
n2 = float(input("Ingrese el segundo número: "))# aqui se almacena el segundo numero
n3 = float(input("Ingrese el tercer número: "))# aqui se almacena el tercer numero

if n1 >= n2 and n1 >= n3: #se crea la condicion si numero1 es mayor o igual a numero2 Y numero1 es mayor o igual a numero3
    print("El mayor número es:", n1)
elif n2 >= n1 and n2 >= n3:#se crea la condicion si numero2 es mayor o igual a numero1 Y numero2 es mayor a numero3
    print("El mayor número es:", n2)
else:# si nunguna de las anteriores condiciones se cumple, entonces el mayor sera numero3
    print("El mayor número es:", n3)
