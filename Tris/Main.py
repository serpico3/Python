from tkinter import *
from tkinter import ttk
import modulo

root = Tk()
frm = ttk.Frame(root, padding=10)
numero=0

frm.grid()

ttk.Label(root, text=numero).grid(column=0, row=0)
ttk.Button(root, text="Print", command=lambda: modulo.printRes1(numero)).grid(column=0, row=1)

root.mainloop()