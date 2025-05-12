import tkinter as tk
from tkinter import ttk

class working:
    def create(m):
        m.destroy()
        m= tk.Tk()
        m.focus()
        m.mainloop()
    #-------------
    def done(m,x):
        if (x.get()=="x"):
            working.create(m)