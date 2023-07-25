# ProgettoCalcoloScientifico_DCT2

 ## Prima parte
La prima parte del progetto consiste nel confrontare i tempi di esecuzione di **DCT2** spiegata a lezione con la **DCT2** fornita da librerie open source.  
Il linguaggio utilizzato per l'implementazione è _python_.  
All'interno del progetto, è stata implementata la **DCT2** di _SciPy_ in versione _fft_, che fornisce funzionalità avanzate per il calcolo scientifico e per l'analisi dei dati: essa fornisce un'implementazione veloce ed efficace della _Discrete Cosine Transform_ e quindi risulta essere perfetta per il nostro scopo. 

All'interno della cartella è possibile trovare anche un grafico che confronota i tempi di esecuzione della DCT2 implementata da noi (con le formule viste a lezione) e la DCT2 disponibile all'intenro del package _fft_ di scipy, implementata in versione fast.  

Si noti che i tempi di esecuzione delle DCT2 personalizzata e di Scipy variano al crescere della dimensione N delle matrici: la nostra implementazione personalizzata della DCT2 ha dimostrato buone prestazioni, ma la DCT2 di Scipy ha vantaggi significativi nelle dimensioni di matrice più grandi grazie alla sua ottimizzazione e algoritmi efficienti.


 ## Seconda parte
