"""Ingresar por teclado usuario y clave. Informar los siguientes casos:
a. Si usuario=”pepito” y clave=”1234” informar “Bienvenido pepito!”
b. Si usuario=”pepito” y clave no es “1234” informar
“Contraseña incorrecta”
c. Si usuario no es “pepito” y clave= “1234” informar “Usuario
incorrecto”
"""

usuario= "pepito"
clave= "1234"
consulta_usuario = input("Por favor ingrese su usuario: ")
consulta_clave = input("Por favor ingrese su contraseña: ")

if usuario == consulta_usuario and clave == consulta_clave:
    print("Bienvenido pepito!")
elif usuario != consulta_usuario and clave == consulta_clave:
    print("Usuario incorrecto")
else:
    print ("Contraseña incorrecta")
    