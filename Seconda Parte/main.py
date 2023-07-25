import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Bitmap files", "*.bmp")])
    if file_path:
        label_path.config(text="File selezionato: " + file_path)
    else:
        label_path.config(text="Nessun file selezionato")

# Creazione della finestra principale
root = tk.Tk()
root.title("Seleziona file .bmp in toni di grigio")

# Etichetta per visualizzare il percorso del file selezionato
label_path = tk.Label(root, text="Nessun file selezionato", wraplength=300)
label_path.pack(pady=10)

# Pulsante "Sfoglia" per selezionare il file
browse_button = tk.Button(root, text="Sfoglia", command=browse_file)
browse_button.pack(pady=5)

# Esecuzione del main loop
root.mainloop()
