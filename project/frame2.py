import tkinter as tk
from tkinter import ttk
from ConnectSV import connect

class working:
    def create(m):
        m.destroy()
        m= tk.Tk()
        m.focus()
        m.mainloop()
    #-------------
    def done(m,a,b,c,d,e):
        if connect().get2(a.get(),b.get(),c.get(),d.get(),e.get()):
            working.create(m)