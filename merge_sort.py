import random


def merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        meio = (inicio + fim) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, (meio + 1), fim)
        combina(lista, inicio, meio, fim)
    return lista


def combina(lista, inicio, meio, fim):
    qtd_lista_b = meio - inicio + 1
    qtd_lista_c = fim - meio
    lista_b = [0] * qtd_lista_b
    lista_c = [0] * qtd_lista_c
    for i in range(qtd_lista_b):
        lista_b[i] = lista[inicio + i]
    for j in range(qtd_lista_c):
        lista_c[j] = lista[meio + j + 1]
    i = 0
    j = 0
    k = inicio
    while i < qtd_lista_b and j < qtd_lista_c:
        if lista_b[i] <= lista_c[j]:
            lista[k] = lista_b[i]
            i += 1
        else:
            lista[k] = lista_c[j]
            j += 1
        k += 1
    while i < qtd_lista_b:
        lista[k] = lista_b[i]
        i += 1
        k += 1
    while j < qtd_lista_c:
        lista[k] = lista_c[j]
        j += 1
        k += 1


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
        lista_ordenada, comparacoes = merge_sort(lista)
        exibir_resultados(nome, lista_original, lista_ordenada, comparacoes)
    print("*******************************")


if __name__ == "__main__":
    main()
