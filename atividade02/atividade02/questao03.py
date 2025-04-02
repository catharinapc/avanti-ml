# Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.

def elementos_diferentes(lista1, lista2):
    return list(set(lista1) ^ set(lista2))


listaEx1 = [2, "ML", 50, 7, "Avanti", False, 13, 17, 19, "banana", 23, 290, 4]
listaEx2 = [2, "AI", 8, "Avanti", False, True, "Morango", 19, "banana", 23, 290]

print(elementos_diferentes(listaEx1, listaEx2))
