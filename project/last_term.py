import tkinter as tk
from tkinter import ttk
from Lop import lenh
#----------
#----------
m=tk.Tk()
m.title("hotel")
lenh.center_window(m)
m.geometry('200x200')
m.resizable(0,0)
t_label=ttk.Label(master=m,text='LOG IN',font=("Arial",30))
t_label.pack()
#-----------
e = ttk.Entry(m)
e.insert(0, "User name")
e.pack(padx=5, pady=5)
e.bind("<FocusIn>", lenh.Click)
e.bind("<FocusOut>", lambda event: lenh.Leave(event, "User name"))
#------------
e1 = ttk.Entry(m)
e1.insert(0, "Password")
e1.pack(padx=5, pady=5)
e1.bind("<FocusIn>", lenh.Click)
e1.bind("<FocusOut>", lambda event: lenh.Leave(event, "Password"))
#-------------
b=ttk.Button(master=m,text="Login", command = lambda: lenh.gett(m,e,e1))
b.pack(padx=6)
#-------------
m.focus()
m.mainloop()