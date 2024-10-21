#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.#
num1 = int(input("Dime el numerador: "))
num2 = int(input("Dime el denominador: "))
if num2 == 0:
    print("error")
else:
    print(num1/num2)