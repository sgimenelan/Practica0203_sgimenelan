#Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin, de acuerdo al sexo y el nombre. 
# Gryffindor está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y Slytheryn por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nombre = (input("Dime tu nombre: ")).lower()
sexo = (input("Dime tu sexo: ")).lower()
if ((nombre < "m" and sexo == "mujer") or (nombre > "n" and sexo == "hombre")):
    print("Perteneces a Gryffindor")
else:
    print("Perteneces a Slytherin")