import random


def bubble_sort(lista):
    n = len(lista)
    comparacoes = 0
    for j in range(n - 1):
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                comparacoes += 1
    return lista, comparacoes


def exibir_resultados(nome, lista_original, lista_ordenada, comparacoes):
    print(f"\nCaso de teste: {nome}")
    print(f"Lista Original: {lista_original}")
    print(f"Lista Ordenada: {lista_ordenada}")
    print(f"Número de Comparações: {comparacoes}")


def main():
    lista_random = random.sample(range(1, 1000), 32)
    lista_ordenada = list(range(1, 33))
    lista_decr = list(range(32, 0, -1))
    lista_unica = [7]

    exemplos = {'Números aleatórios': lista_random,
                'Já ordenados': lista_ordenada,
                'Ordem decrescente': lista_decr,
                'Lista única': lista_unica}

    print("*******************************")
    for nome, lista in exemplos.items():
        lista_original = lista.copy()
        lista_ordenada, comparacoes = bubble_sort(lista)
        exibir_resultados(nome, lista_original, lista_ordenada, comparacoes)
    print("*******************************")


if __name__ == "__main__":
    main()
