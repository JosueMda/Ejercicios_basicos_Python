"""Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d','e','i','n','o','r','t']"""


def ordenar(palabra1):
  mi_set = set()
  for palabra in palabra1:
    mi_set.add(palabra)

  lista = list(mi_set)
  lista.sort()
  return lista


print(ordenar("josueeee"))