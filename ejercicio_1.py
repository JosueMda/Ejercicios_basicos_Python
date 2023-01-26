""" Ingresa por teclado 3 tipos de numeros enteros y distintos e informar cual es el mayor.
Ejemplo: Si ingresa 3 , 20 , 8, mostrara 20
"""

num1= int(input("Por favor ingrese un numero: "))
num2= int(input("Por favor ingrese un numero: "))
num3= int(input("Por favor ingrese un numero: "))
lista= [num1,num2,num3]
lista= max(lista)
print(f"El numero mayor que ha elegido es el {lista}")