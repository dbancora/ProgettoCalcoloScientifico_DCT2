import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont
from tkinter import ttk

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Bitmap files", "*.bmp")])
    if file_path:
        label_path.config(text="File selezionato: " + file_path)
    else:
        label_path.config(text="Nessun file selezionato")

def create_interface():
    # Dichiarazione della variabile globale    
    global label_path
    
    # Creazione della finestra principale
    root = tk.Tk()
    root.title("Seleziona file .bmp in toni di grigio")

    # Calcola le dimensioni dello schermo attuale
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Imposta le nuove dimensioni della finestra (la metà dello schermo)
    window_width = int(screen_width / 2)
    window_height = int(screen_height / 2)
    root.geometry(f"{window_width}x{window_height}")

    # Calcola la nuova dimensione del carattere in base alle dimensioni della finestra
    font_size = int(window_height / 30)

    # Crea un font con la nuova dimensione
    custom_font = tkFont.Font(size=font_size)

    # Etichetta per visualizzare il percorso del file selezionato
    label_path = tk.Label(root, text="Nessun file selezionato", wraplength=300, font=custom_font)
    label_path.pack(pady=10)

    # Pulsante "Sfoglia" per selezionare il file con lo stile di Material-UI
    style = ttk.Style()
    style.configure("Material.TButton", font=custom_font)  # Configura lo stile del bottone
    browse_button = ttk.Button(root, text="Sfoglia", command=browse_file, style="Material.TButton")
    browse_button.pack(pady=5)

    # Esecuzione del main loop
    root.mainloop()