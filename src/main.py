import random
from .test import generador_vector, run_test, boxplot

def main():
    vectores = generador_vector(k=10, n=100) 
    df, resultados = run_test(vectores)
    print(df.to_string(index=False))
    ruta = boxplot(resultados)
    print(f"Grafico Boxplot se guardado en:{ruta}")

if __name__ == "__main__":
    main()
