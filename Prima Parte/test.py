import numpy as np
import timeit
import utils

def run_test():
    # Test DCT:
    a = np.array([231, 32, 233, 161, 24, 71, 140, 245])

    # DEBUG: print (transformation_matrix)

    dct = utils.dct_created(a)
    formatted_dct = ["{:.2e}".format(val) for val in dct]
    print("\n-----------------------TEST DCT HomeMade-------------------------")
    print(formatted_dct)

    input_matrix = np.array([[231, 32, 233, 161, 24, 71, 140, 245], 
                            [247, 40, 248, 245, 124, 204, 36, 107], 
                            [234, 202, 245, 167, 9, 217, 239, 173],
                            [193, 190, 100, 167, 43, 180, 8, 70],
                            [11, 24, 210, 177, 81, 243, 8, 112],
                            [97, 195, 203, 47, 125, 114, 165, 181],
                            [193, 70, 174, 167, 41, 30, 127, 245],
                            [87, 149, 57, 192, 65, 129, 178, 228]])
    dct2_result = utils.dct2_created(input_matrix)
    print("\n------------------------------------------------------------------\n")
    print("\n-----------------------TEST DCT2 HomeMade-------------------------")
    print(dct2_result)

    dct = utils.dct_library(a)
    formatted_dct = ["{:.2e}".format(val) for val in dct]
    print("\n------------------------------------------------------------------\n")
    print("\n-----------------------TEST DCT Library-------------------------")
    print(formatted_dct)

    dct2_result = utils.dct2_library(input_matrix)
    print("\n------------------------------------------------------------------\n")
    print("\n-----------------------TEST DCT2 Library-------------------------")
    print(dct2_result)

def test_N(): 
    # Dimensioni delle matrici NxN (da 50 a 900 con passo 50)
    matrix_dimensions = list(range(50, 951, 50))

    times_scipy_dct = []
    times_my_dct = []

    for n in matrix_dimensions:
        print("Dimension: ", n)

        # Creazione di una matrice random
        np.random.seed(5)
        matrix = np.random.uniform(low=0.0, high=255.0, size=(n, n))

        # Calcolo del tempo di esecuzione con scipy DCT2
        time_scipy = timeit.timeit(lambda: utils.dct2_library(matrix), number=1)
        times_scipy_dct.append(time_scipy)

        # Calcolo del tempo di esecuzione con la tua DCT2
        time_my_dct = timeit.timeit(lambda: utils.dct2_created(matrix), number=1)
        times_my_dct.append(time_my_dct)

    return times_scipy_dct, times_my_dct, matrix_dimensions