import csv
import math


def bubble_sort_recurrence(n):
    if n == 1:
        return 0
    else:
        return (n - 1) + bubble_sort_recurrence(n - 1)


def merge_sort_recurrence(n):
    if n == 1:
        return 1
    else:
        return 2 * merge_sort_recurrence(n / 2) + n


def bubble_sort_formula(n):
    return ((n - 1) * n) // 2


def merge_sort_formula(n):
    return n + n * math.log2(n)


def run_comparison():
    # Lista de tamanhos, potências de 2 de 2^1 a 2^9
    sizes = [2**i for i in range(1, 10)]
    results = []
    for size in sizes:
        # Calcular o valor teórico usando a sequência recorrente para Bubble Sort
        bubble_recurrence = bubble_sort_recurrence(size)
        # Calcular o valor teórico usando a fórmula fechada para Bubble Sort
        bubble_formula = bubble_sort_formula(size)
        # Calcular o valor teórico usando a sequência recorrente para Merge Sort
        merge_recurrence = merge_sort_recurrence(size)
        # Calcular o valor teórico usando a fórmula fechada para Merge Sort
        merge_formula = merge_sort_formula(size)
        results.append([size, bubble_recurrence, bubble_formula,
                       merge_recurrence, merge_formula])

    # Escrever os resultados em um arquivo CSV
    with open('comparison_results.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Size", "Bubble Recurrence",
                           "Bubble Formula", "Merge Recurrence", "Merge Formula"])
        csvwriter.writerows(results)


if __name__ == "__main__":
    run_comparison()
