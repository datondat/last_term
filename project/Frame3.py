import tkinter as tk
from ConnectSV import connect

import common
class neww:
    def create1(m,x):
        m.destroy()
        m= tk.Tk()
        m.geometry("200x200")
        e1=tk.Entry()
        e1.pack()
        e2=tk.Entry()
        e2.pack()
        b=tk.Button(master=m,text="Pay",command=lambda: connect().submit(e1.get(),e2.get()))
        b.pack()
        b1 = tk.Button(master=m, text="Tra", command=lambda: connect().submit1(e1.get(), e2.get()))
        b1.pack()
        m.focus()
        m.mainloop()

