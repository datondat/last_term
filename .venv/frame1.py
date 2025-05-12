import tkinter as tk
from tkinter import ttk
from doing import working
class new_frame:
    def new(m):
        m.destroy()
        m=tk.Tk()
        m.geometry('250x400')
        m.title("Register")
        t_label1 = ttk.Label(master=m, text='Register', font=("Arial", 35))
        t_label1.pack()
        r=ttk.Entry(m)
        r.pack(pady=10)
        r1 = ttk.Entry(m)
        r1.pack(pady=10)
        r2 = ttk.Entry(m)
        r2.pack(pady=10)
        r3 = ttk.Entry(m)
        r3.pack(pady=10)
        b=ttk.Button(master=m,text="enter",command=lambda : working.done(m,r))
        b.pack()
        m.focus()
        m.mainloop()
