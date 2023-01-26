""" Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas. """
num = int(input("Por favor ingrese un numero entero positivo: "))
lista = []
for n in range(1,num,2):
    lista.append(n)
print(*lista, sep=", ")