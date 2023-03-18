from tkinter import*
class hide():
        def hide1(widget,a1,l1):
            widget.place(width='0',height='0')  
            a1.delete(0, END)
            l1.set('')
        def hide2(widget,a1,a2,l1):
            widget.place(width='0',height='0')  
            a1.delete(0, END)
            a2.delete(0, END)
            l1.set('')
        def hide3(widget,a1,a2,a3,l1):
            widget.place(width='0',height='0')  
            a1.delete(0, END)
            a2.delete(0, END)
            a3.delete(0, END)
            l1.set('')
        def hide4(widget,a1,a2,a3,a4,l1):
            widget.place(width='0',height='0')  
            a1.delete(0, END)
            a2.delete(0, END)
            a3.delete(0, END)
            a4.delete(0, END)
            l1.set('')