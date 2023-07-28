import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.font as tkFont
from tkinter import ttk

# Dichiarazione delle variabili globali
global label_path, entry_variable_f, entry_variable_d, file_path

file_path = None

def browse_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Bitmap files", "*.bmp")])
    if file_path:
        label_path.config(text="File selezionato: " + file_path)
    else:
        label_path.config(text="Nessun file selezionato")

def save_variables():
    global entry_variable_f, entry_variable_d, file_path
    
    # Recupera i valori di F e d dalla label
    F = entry_variable_f.get()
    d = entry_variable_d.get()

    # Verifica che le label e l'immagine non siano vuote. in caso contrario, viene mostrato un messaggio di errore
    if not file_path:
        messagebox.showerror("Errore", "Seleziona un'immagine.")
        return

    if not F:
        messagebox.showerror("Errore", "Inserisci il valore di F.")
        return

    if not d:
        messagebox.showerror("Errore", "Inserisci il valore di d.")
        return

    if not is_integer(F):
        messagebox.showerror("Errore", "F deve essere un numero intero")
        return
    
    if not is_integer(d):
        messagebox.showerror("Errore", "d deve essere un numero intero")
        return

    F = int(F)
    d = int(d)

    if F < 0:
        messagebox.showerror("Errore", "F deve essere maggiore o uguale a 0")
        return
    if d < 0:
        messagebox.showerror("Errore", "d deve essere maggiore o uguale a 0")
        return

    # If all checks pass, proceed with compression
    print("Variabile F:", F)
    print("Variabile d:", d)
    print("Compressing...")

def create_interface():
    global label_path, entry_variable_f, entry_variable_d

    root = tk.Tk()
    root.title("Seleziona file .bmp in toni di grigio")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = int(screen_width / 2)
    window_height = int(screen_height / 2)
    root.geometry(f"{window_width}x{window_height}")

    font_size = int(window_height / 30)
    custom_font = tkFont.Font(size=font_size)

    label_path = tk.Label(root, text="Nessun file selezionato", wraplength=300, font=custom_font)
    label_path.pack(pady=10)

    style = ttk.Style()
    style.configure("Material.TButton", font=custom_font)
    browse_button = ttk.Button(root, text="Sfoglia", command=browse_file, style="Material.TButton")
    browse_button.pack(pady=5)

    label_variable_f = tk.Label(root, text="Inserisci la variabile F:", font=custom_font)
    label_variable_f.pack(pady=10)

    entry_variable_f = tk.Entry(root, font=custom_font)
    entry_variable_f.pack(pady=5)

    label_variable_d = tk.Label(root, text="Inserisci la variabile d (intero):", font=custom_font)
    label_variable_d.pack(pady=10)

    entry_variable_d = tk.Entry(root, font=custom_font)
    entry_variable_d.pack(pady=5)

    save_button = ttk.Button(root, text="Salva F e d", command=save_variables, style="Material.TButton")
    save_button.pack(pady=5)

    # Aggiungiamo il pulsante "Compress"
    compress_button = ttk.Button(root, text="Compress", command=save_variables, style="Material.TButton")
    compress_button.pack(pady=5)

    root.mainloop()


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False