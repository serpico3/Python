# calcolatrice_gui.py

import tkinter as tk
from tkinter import ttk
from modulo import *

# Inizializza la calcolatrice
calcolatrice = Calcolatrice()

def aggiorna_display():
    """Aggiorna il display con l'operazione corrente."""
    display_var.set(calcolatrice.operazione)

def gestisci_click(tasto):
    """Gestisce il click su un tasto della calcolatrice."""
    if tasto == "=":
        calcolatrice.calcola()
    elif tasto == "C":
        calcolatrice.reset()
    else:
        calcolatrice.aggiungi(tasto)
    aggiorna_display()

# Creazione della finestra principale
root = tk.Tk()
root.title("Calcolatrice")

# Variabile per il display
display_var = tk.StringVar()

# Display della calcolatrice
display = ttk.Entry(root, textvariable=display_var, font=("Arial", 20), justify="right", state="readonly")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Bottoni della calcolatrice
tasti = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for testo, riga, colonna in tasti:
    ttk.Button(root, text=testo, command=lambda t=testo: gestisci_click(t)).grid(row=riga, column=colonna, sticky="nsew")

# Configura la griglia per una migliore gestione dello spazio
for i in range(6):  # 5 righe + 1 per il display
    root.rowconfigure(i, weight=1)
for i in range(4):  # 4 colonne
    root.columnconfigure(i, weight=1)

# Avvia il loop principale
root.mainloop()
