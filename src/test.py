import os
import random
from statistics import mean, stdev#para promedio y desviacion estandar
from typing import Dict, List, Tuple

import pandas as pd#para datos en forma de tabla
import matplotlib.pyplot as plt#para crear el grafico

from .sorting import insercion, seleccion, burbuja

def generador_vector(k: int = 10, n: int = 100) -> List[List[int]]:#generador de vector de 10 con #'s random de 1-100
    return [[random.randint(1, 100) for _ in range(n)] for _ in range(k)]

def run_test(vectors: List[List[int]]) -> Tuple[pd.DataFrame, Dict[str, List[int]]]:
    resultados = {"Insercion": [], "Seleccion": [], "Burbuja": []}
    algoritmos = {#mapea los nombres a las funciones
        "Insercion": insercion,
        "Seleccion": seleccion,
        "Burbuja": burbuja,
    }
    for nombre, algo in algoritmos.items():
        for v in vectors:
            arr = v[:]#hace copia del vector origi.
            intercambios = algo(arr)#cuenta el intercambio
            resultados[nombre].append(intercambios)#lo guarda

    #para las estadísticas
    filas = []
    for nombre, vals in resultados.items():
        prom = mean(vals)#promedio
        sd = stdev(vals) if len(vals) > 1 else 0.0#descviacion estandar
        filas.append({
            "Algoritmo": nombre,
            "Intercambios promedio": round(prom, 2),
            "Desviación estandar": round(sd, 2),
        })
    #crea el dataFrame con los resultados
    df = pd.DataFrame(filas)
    return df, resultados

#crea el boxplot, con diccionario de los result. de los swaps y la ruta dónde guardarlo
def boxplot(resultados: Dict[str, List[int]], outpath: str = "figures/boxplot_intercambio.png") -> str:
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    plt.figure()#crea la figura vacía de la lib matplotlib
    plt.boxplot(
        [resultados["Insercion"], resultados["Seleccion"], resultados["Burbuja"]],#lista de listas con los swaps de c/u algoritmo
        labels=["Insercion", "Seleccion", "Burbuja"]#son los nombres que aparecen en el graf.
    )
    plt.title("Intercambios por algoritmo(10 runs)")
    plt.ylabel("Número de intercambios")#etiqueta del eje y
    plt.savefig(outpath, bbox_inches="tight", dpi=160)#ruta para guardarlo,eliminar los bordes blancos,calidad de imagen
    plt.close()#cierra la figura para liberar memoria
    return outpath#confirma dónde se guardó el gráfico para usarlo después
