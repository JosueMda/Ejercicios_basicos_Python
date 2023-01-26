"""6) Se desea determinar el estado de un alumno según la nota obtenida y
mostrar si el alumno aprobó, recupera o perdió la materia.
La nota obtenida puede ser alguna de las siguientes letras ‘A’, ‘B’, ‘C’ o ‘D’.
Los estados posibles son aprobado, recupera, o pierde la materia.
Para las notas ‘A’ y ‘B’ se considera aprobado la materia, para la nota ‘C’ se
debe recuperar y para la nota es ‘D’ se pierde la materia.
Ejemplo: ingresa “C”, deberá mostrar que debe recuperar.
    """
    
ingresar_nota= input("Por favor ingrese su nota: ")
if ingresar_nota == "A" or ingresar_nota == "B":
    print("Felicitaciones, usted ha aprobado")
elif ingresar_nota == "C":
    print("Usted debe recuperar la materia")
elif ingresar_nota == "D":
    print("Lo sentimos, pero usted ha perdido la materia")
else:
    print("Calificación invalida, vuelva a intentarlo")