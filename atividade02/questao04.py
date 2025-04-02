#Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.

def segundo_maior(lista):
    lista_ordenada = sorted(set(lista), reverse=True)
    return lista_ordenada[1]

listaEx = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 4, 6, 8]
print(segundo_maior(listaEx))