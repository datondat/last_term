import tkinter as tk
from tkinter import ttk
from frame2 import working
from project.Lop import lenh


class new_frame:
    def new(m):
        m.destroy()
        m=tk.Tk()
        m.title("Register")
        m.geometry('250x400')
        m.resizable(0, 0)
        m.title("Register")
        t_label1 = ttk.Label(master=m, text='Register', font=("Arial", 35))
        t_label1.pack()
        l1=ttk.Label(master=m,text="User name",font=('Arials',10))
        l1.place(x=20,y=60)
        r=ttk.Entry(m)
        r.place(x=90,y=60)
        l2 = ttk.Label(master=m, text="Password", font=('Arials', 10))
        l2.place(x=20,y=120)
        r1 = ttk.Entry(m)
        r1.place(x=90,y=120)
        r1.bind("<FocusIn>",lenh.Click)
        l2 = ttk.Label(master=m, text="Phone", font=('Arials', 10))
        l2.place(x=20,y=180)
        r2 = ttk.Entry(m)
        r2.place(x=90,y=180)
        l3= ttk.Label(master=m, text="Mail", font=('Arials', 10))
        l3.place(x=20,y=240)
        r3 = ttk.Entry(m)
        r3.place(x=90,y=240)
        l4 = ttk.Label(master=m, text="ID", font=('Arials', 10))
        l4.place(x=20,y=280)
        r4 = ttk.Entry(m)
        r4.place(x=90,y=280)
        b=ttk.Button(master=m,text="Register",command=lambda : working.done(m,r,r1,r2,r3,r4))
        b.place(x=80,y=320)
        m.focus()
        m.mainloop()
