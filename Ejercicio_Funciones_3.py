"""Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False"""

def numeros (*args):
  contador = 0
  for num in args:
    if args[contador] == 0 and args [contador + 1] == 0:
      return True
    else:
      contador += 1
  
  return False

print(numeros(1,2,5,0,6))
    