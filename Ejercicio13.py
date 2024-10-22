#Escribir un programa que muestre el eco de todo lo que el usuario
# introduzca hasta que el usuario escriba “salir” que terminará.
frase = ""
while (frase != "salir"):
    frase = input("Modo eco: ")
    print(frase)
print("Has salido del modo eco")