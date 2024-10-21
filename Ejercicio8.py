#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
numero = 1
while numero <= 10:
    for i in range(1, 11):
        print(numero * i)
    numero = numero + 1
