#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo
#que tenga tantas líneas como el número introducido, como el triángulo de más abajo.
numero = int(input("Dime un numero entero: "))
for i in range(1, 2*numero, 2):
    for i in range(i, 0, -2):
        print(i, end=" ")
    print("")