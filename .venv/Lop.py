from frame1 import new_frame
class lenh:
    # ---------
    def Click(event):
        if event.widget.get() == "User name":
            event.widget.delete(0, 'end')
        elif event.widget.get() == "Password":
            event.widget.delete(0, 'end')
            event.widget.config(show='*')

    def Leave(event, placeholder):
        if event.widget.get() == '':
            event.widget.insert(0, placeholder)

    def center_window(m):
        screen_width = m.winfo_screenwidth()
        screen_height = m.winfo_screenheight()
        x = (screen_width - m.winfo_reqwidth()) // 2
        y = (screen_height - m.winfo_reqheight()) // 2
        m.geometry(f"+{x}+{y}")

    #------------
    def gett(m, a, b):
        print(a.get())
        print(b.get())
        if a.get()=="x" and b.get()=="y":
            new_frame.new(m)
