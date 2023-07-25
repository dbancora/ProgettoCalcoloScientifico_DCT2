import numpy as np
import utils

def run_test():
    # TEst DTC:
    a = np.array([231, 32, 233, 161, 24, 71, 140, 245])

    # DEBUG: print (transformation_matrix)

    dct = utils.dct_created(a)
    formatted_dct = ["{:.2e}".format(val) for val in dct]
    print("\n-----------------------TEST DTC HomeMade-------------------------")
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
    print("\n-----------------------TEST DTC2 HomeMade-------------------------")
    print(dct2_result)

    dct = utils.dct_library(a)
    formatted_dct = ["{:.2e}".format(val) for val in dct]
    print("\n-----------------------TEST DTC Library-------------------------")
    print(formatted_dct)

    dct2_result = utils.dct2_library(input_matrix)
    print("\n-----------------------TEST DTC2 Library-------------------------")
    print(dct2_result)

