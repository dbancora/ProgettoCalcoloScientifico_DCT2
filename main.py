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

# Funzione per DCT2 creata
def dct2_created(input_matrix):
    
    m, n = input_matrix.shape

    # Crezione della matrice 
    dct2_result = np.zeros((m, n))

    # DCT per ogni riga
    for i in range(m):
        dct2_result[i, :] = dct_created(input_matrix[i, :])

    # DCT per ogni colonna
    for j in range(n):
        dct2_result[:, j] = dct_created(dct2_result[:, j])

    return dct2_result

# Esempio di utilizzo:
a = np.array([231, 32, 233, 161, 24, 71, 140, 245])

# DEBUG: print (transformation_matrix)

dct = dct_created(a)
formatted_dct = ["{:.2e}".format(val) for val in dct]
print(formatted_dct)


input_matrix = np.array([[231, 32, 233, 161, 24, 71, 140, 245], 
                         [247, 40, 248, 245, 124, 204, 36, 107], 
                         [234, 202, 245, 167, 9, 217, 239, 173],
                         [193, 190, 100, 167, 43, 180, 8, 70],
                         [11, 24, 210, 177, 81, 243, 8, 112],
                         [97, 195, 203, 47, 125, 114, 165, 181],
                         [193, 70, 174, 167, 41, 30, 127, 245],
                         [87, 149, 57, 192, 65, 129, 178, 228]])
dct2_result = dct2_created(input_matrix)
print(dct2_result)
