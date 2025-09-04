from typing import List

def intercambio(a: List[int], i: int, j: int) -> int:
    a[i], a[j] = a[j], a[i]
    return 1

def insercion(a: List[int]) -> int:   #este lo cambié un poco porque me dió problemas
    swaps = 0#contador
    n = len(a)
    for i in range(1, n):
        j = i - 1
        while j >= 0 and a[j] > a[j + 1]:
            swaps += intercambio(a, j, j + 1)
            j -= 1
    return swaps

def seleccion(a: List[int]) -> int:
    swaps = 0 #contador
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            swaps += intercambio(a, i, min_idx)
    return swaps

def burbuja(a: List[int]) -> int:
    swaps = 0 #contador
    n = len(a)
    for i in range(n):
        hubo_i = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                swaps += intercambio(a, j, j + 1)
                hubo_i = True
        if not hubo_i:
            break
    return swaps
