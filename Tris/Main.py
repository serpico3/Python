from tkinter import *
from tkinter import ttk
import modulo

root = Tk()
frm = ttk.Frame(root, padding=10)
numero = 0
frm.grid()
ttk.Button(root, text="1", command=modulo.printRes1(Text)).grid(column=0, row=1)
"""ttk.Button(root, text="2", command=printRes2).grid(column=1, row=1)
ttk.Button(root, text="3", command=printRes3).grid(column=2, row=1)
ttk.Button(root, text="4", command=printRes4).grid(column=0, row=2)
ttk.Button(root, text="5", command=printRes5).grid(column=1, row=2)
ttk.Button(root, text="6", command=printRes6).grid(column=2, row=2)
ttk.Button(root, text="7", command=printRes7).grid(column=0, row=3)
ttk.Button(root, text="8", command=printRes8).grid(column=1, row=3)
ttk.Button(root, text="9", command=printRes9).grid(column=2, row=3)
ttk.Button(root, text="+", command=add(numero)).grid(column=3, row=1)
ttk.Button(root, text="-", command=sub(numero)).grid(column=3, row=2)
ttk.Button(root, text="*", command=mul(numero)).grid(column=3, row=3)
ttk.Button(root, text="/", command=div(numero)).grid(column=3, row=4)"""
ttk.Label(root, text=numero).grid(column=0, row=0)

root.mainloop()