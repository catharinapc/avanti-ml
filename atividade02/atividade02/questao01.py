#Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.

def filtrar_impares(lista):
    lista_impares = []
    for num in lista:
        if num % 2 != 0:
            lista_impares.append(num)
    return lista_impares

listaEx = [7,9,53,67,80,89,101,143,200,204,305,409]

print(filtrar_impares(listaEx))





