""" Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase. """
frase= input("Por favor ingrese una frase: ")
letra= input("Ingrese que letra le interesa saber cuantas veces se repite: ")

print(f"La letra {letra} se repite {frase.count(letra)} veces.")