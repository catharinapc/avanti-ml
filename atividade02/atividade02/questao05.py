# Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.


def ordenar_por_nome(lista_pessoas):
    return sorted(lista_pessoas, key=lambda pessoa: pessoa[0])

pessoas = [
    ("Lucas", 28),
    ("Mariana", 34),
    ("Fernando", 22),
    ("Amanda", 29),
    ("Ricardo", 41),
    ("Beatriz", 26),
    ("Gabriel", 30),
    ("Tatiane", 35),
    ("Henrique", 27),
    ("Vanessa", 33)
]

print(ordenar_por_nome(pessoas))