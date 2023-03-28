"""Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.
Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo """

def esMultiplo (num1, num2):
    var= num1 % num2
    if var == 0:
        print("Es múltiplo")
    else:
        print("No es múltiplo")
        
esMultiplo(14, 3)