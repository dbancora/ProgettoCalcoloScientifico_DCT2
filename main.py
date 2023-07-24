import numpy as np
import math


# Funzione per la creazione della matrice di trasformazione
def create_transformation_matrix(a):
    # Calcolo della lunghezza dell'array
    n = len(a)

    # Creazione del vettore alfa lungo quanto il vettore passato
    alpha = np.zeros(n)

    # Calcolo dei valori in base alla posizione 
    alpha[0] = 1 / np.sqrt(n)
    alpha[1:] = np.sqrt(2/n)

    #DEBUG: print(alpha)

    # Creazione della matrice di trasformazione
    transformation_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            transformation_matrix[i, j] = alpha[i] * np.cos((math.pi * (2 * j + 1) * i) / (2 * n))
    
    return transformation_matrix

# Esempio di utilizzo:
a = np.array([1, 2, 3, 4])
transformation_matrix = create_transformation_matrix(a)
# DEBUG: print (transformation_matrix)