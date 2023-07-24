import numpy as np

def create_transformation_matrix(a):
    n = len(a)
    alpha = np.zeros(n)
    alpha[0] = 1 / np.sqrt(n)
    alpha[1:] = np.sqrt(2/n)

    print(alpha)

    transformation_matrix = np.outer(alpha, a)
    return transformation_matrix

# Esempio di utilizzo:
a = np.array([1, 2, 3, 4])
transformation_matrix = create_transformation_matrix(a)