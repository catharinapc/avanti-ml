#Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

def filtrar_primos(lista):
    lista_primos = []
    for num in lista:
        if num > 1:
            eh_primo = True
            for x in range(2, int(num ** 0.5) + 1):
                if num % x == 0:
                    eh_primo = False
                    break
            if eh_primo:
                lista_primos.append(num)
    return lista_primos


listaEx = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
print(filtrar_primos(listaEx))

