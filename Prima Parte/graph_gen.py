import matplotlib.pyplot as plt
import numpy as np

def plot_dct_times(times_scipy_dct, times_my_dct, matrix_dimensions):
    # Dividiamo per 10^6 in modo da visualizzare le righe di comparazione vicino alla riga 
    n3 = [n**3 /1e5 for n in matrix_dimensions]    
    n2_logn = [n**2 * np.log(n) / 1e8 for n in matrix_dimensions]

    plt.figure(figsize=(10, 6))
    plt.semilogy(matrix_dimensions, times_scipy_dct, label='Library DCT2', color="tab:green")
    plt.semilogy(matrix_dimensions, n2_logn, label='n^2 * log(n)', color="tab:green", linestyle='dashed')
    plt.semilogy(matrix_dimensions, times_my_dct, label='DCT2 created', color="tab:blue")
    plt.semilogy(matrix_dimensions, n3, label='n^3', color="tab:blue", linestyle='dashed')
    
    plt.xlabel('Dimensione N')
    plt.ylabel('Tempo di esecuzione in secondi')
    plt.title('Tempi di esecuzione della DCT2 al variare della dimensione N')
    plt.legend()
    plt.grid(True)

    # Salva l'immagine del grafico
    plt.savefig('Prima Parte/grafico_dct_times.png')

    plt.show()