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
            transformation_matrix[i, j] = alpha[i] * np.cos((i * math.pi * (2 * j + 1)) / (2 * n))
    
    return transformation_matrix

# Funzione per DCT creata 
def dct_created(input_vector):
    # Creazione della matrice di trasformazione
    transformation_matrix = create_transformation_matrix(input_vector)

    # Calcolo del risultato (c) come la moltiplizazione tra la matrice di trasformazione con il vettore dato in input (f)
    dct_result = np.dot(transformation_matrix, input_vector)
    
    return dct_result


# Esempio di utilizzo:
a = np.array([231, 32, 233, 161, 24, 71, 140, 245])

# DEBUG: print (transformation_matrix)

dct = dct_created(a)
formatted_dct = ["{:.2e}".format(val) for val in dct]
print(formatted_dct)