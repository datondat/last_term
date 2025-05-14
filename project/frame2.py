import tkinter as tk
from tkinter import ttk
from ConnectSV import connect

class working:
    def create(m):
        m.destroy()
        m= tk.Tk()
        width1=m.winfo_screenwidth()
        height1=m.winfo_screenheight()
        m.geometry("%dx%d"%(width1,height1))
        for row in range(5):
            for col in range(5):
                tk.Button(
                    master=m,
                    text=f"Room ({(row+1)*(col+1)})",
                    width=41,
                    height=10,
                ).grid(row=row,column=col,padx=3,pady=2)
        m.focus()
        m.mainloop()
    #-------------
    def done(m,a,b,c,d,e):
        if connect().get2(a.get(),b.get(),c.get(),d.get(),e.get()):
            working.create(m)