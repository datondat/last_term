import tkinter as tk
from tkinter import ttk
from ConnectSV import connect
import webbrowser
import common
from Frame3 import neww
class working:
    def create(m):
        m.destroy()
        m= tk.Tk()
        m.title("Select room")
        a = [[0 for _ in range(5)] for _ in range(5)]
        width1=m.winfo_screenwidth()
        height1=m.winfo_screenheight()
        m.geometry("%dx%d"%(width1,height1))
        x=0
        for row in range(5):
            for col in range(5):
                x=x+1
                a[row][col]=x
                if connect().get4(x)=="Trống":
                    tk.Button(
                        master=m,
                        text=f"Room {x}\n {connect().get3(x)}",
                        width=41,
                        height=10,
                        bg="green",
                        command=lambda val=x: working.pay(m, val),
                    ).grid(row=row,column=col,padx=3,pady=2)
                else:
                    tk.Button(
                        master=m,
                        text=f"Room {x}\n {connect().get3(x)}",
                        width=41,
                        height=10,
                        bg="red",
                        command=lambda val=x: working.pay(m, val),
                    ).grid(row=row, column=col, padx=3, pady=2)
        m.focus()
        m.mainloop()
    #-------------
    def done(m,a,b,c,d,e):
        if connect().get2(a.get(),b.get(),c.get(),d.get(),e.get()):
            working.create(m)
    def pay(m,x):
        common.aaaa=x
        neww.create1(m,common.aaaa)