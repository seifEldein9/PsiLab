from tkinter import*
from sympy import *
import tkinter as tk
from numpy import sin, cos
from sympy import symbols
from sympy import simplify
from tkinter import messagebox
#=====================================
from popup_menu import*
#=====================================
class Home():
    def Home(home):
        def Clear():
            functionsset.delete(0, END)
            Labelmain.set('')

        def math():  
            math = Toplevel(home)
            math.geometry("500x800+50+200")
            math.configure(background="#f8f8ff")
            math.resizable(False,False)
            math.title("mathematics")
            math.iconbitmap('photo\logo.ico')
            math.protocol("WM_DELETE_WINDOW", lambda: close_window(math))
            functions_Button.config(state='disabled')
            def close_window(window):
                window.destroy()
                functions_Button.config(state='normal')
            x,y,z,a,b,t,w = symbols('x y z a b t w')
            def Integration():
                functionsset.insert("end",'Integral(  , (x))')
            def definiteIntegrate():
                functionsset.insert("end",'Integral(  , (x , 0 , 1))')   
            def deriving():
                functionsset.insert("end",'diff((),x)')     
            def limit():
                functionsset.insert("end",'limit(,x,1)') 
            def Matrix():
                functionsset.insert("end",'Matrix()')
            def factorial():
                functionsset.insert("end",'factorial()')
            def log():
                functionsset.insert("end",'log()')
            def sqrt():
                functionsset.insert("end",'sqrt()')
            def cbrt():
                functionsset.insert("end",'cbrt()')
            def sin():
                functionsset.insert("end",'sin()')
            def cos():
                functionsset.insert("end",'cos()')
            def tan():
                functionsset.insert("end",'tan()')
            def asin():
                functionsset.insert("end",'asin()')
            def acos():
                functionsset.insert("end",'acos()')
            def atan():
                functionsset.insert("end",'atan()')
            def sinh():
                functionsset.insert("end",'sinh()')
            def cosh():
                functionsset.insert("end",'cosh()')
            def tanh():
                functionsset.insert("end",'tanh()')
            def asinh():
                functionsset.insert("end",'asinh()')
            def acosh():
                functionsset.insert("end",'acosh()')
            def atanh():
                functionsset.insert("end",'atanh()')
            def pi():
                functionsset.insert("end",3.14159265359)
            def e():
                functionsset.insert("end",2.71828182846)




            bx1 = Button(math,text='integrate()',bg='#537FE7',fg='#E9F8F9',font=2,command=Integration)
            bx1.pack(fill=X)
            bx2 = Button(math,text='definiteIntegrate()',bg='#537FE7',fg='#E9F8F9',font=2,command=definiteIntegrate)
            bx2.pack(fill=X)
            bx2 = Button(math,text='deriving()',bg='#537FE7',fg='#E9F8F9',font=2,command=deriving)
            bx2.pack(fill=X)
            bx3 = Button(math,text='limit()',bg='#537FE7',fg='#E9F8F9',font=2,command=limit)
            bx3.pack(fill=X)
            bx4 = Button(math,text='Matrix()',bg='#537FE7',fg='#E9F8F9',font=2,command=Matrix)
            bx4.pack(fill=X)
            bx5 = Button(math,text='factorial()',bg='#537FE7',fg='#E9F8F9',font=2,command=factorial)
            bx5.pack(fill=X)
            bx6 = Button(math,text='log()',bg='#537FE7',fg='#E9F8F9',font=2,command=log)
            bx6.pack(fill=X)
            bx7 = Button(math,text='sqrt()',bg='#537FE7',fg='#E9F8F9',font=2,command=sqrt)
            bx7.pack(fill=X)
            bx8 = Button(math,text='cbrt()',bg='#537FE7',fg='#E9F8F9',font=2,command=cbrt)
            bx8.pack(fill=X)
            bx9 = Button(math,text='sin()',bg='#537FE7',fg='#E9F8F9',font=2,command=sin)
            bx9.pack(fill=X)
            bx10 = Button(math,text='cos()',bg='#537FE7',fg='#E9F8F9',font=2,command=cos)
            bx10.pack(fill=X)
            bx11 = Button(math,text='tan()',bg='#537FE7',fg='#E9F8F9',font=2,command=tan)
            bx11.pack(fill=X)
            bx12 = Button(math,text='asin()',bg='#537FE7',fg='#E9F8F9',font=2,command=asin)
            bx12.pack(fill=X)
            bx13 = Button(math,text='acos()',bg='#537FE7',fg='#E9F8F9',font=2,command=acos)
            bx13.pack(fill=X)
            bx14 = Button(math,text='atan()',bg='#537FE7',fg='#E9F8F9',font=2,command=atan)
            bx14.pack(fill=X)
            bx15 = Button(math,text='sinh()',bg='#537FE7',fg='#E9F8F9',font=2,command=sinh)
            bx15.pack(fill=X)
            bx16 = Button(math,text='cosh()',bg='#537FE7',fg='#E9F8F9',font=2,command=cosh)
            bx16.pack(fill=X)
            bx17 = Button(math,text='tanh()',bg='#537FE7',fg='#E9F8F9',font=2,command=tanh)
            bx17.pack(fill=X)
            bx18 = Button(math,text='asinh()',bg='#537FE7',fg='#E9F8F9',font=2,command=asinh)
            bx18.pack(fill=X)
            bx19 = Button(math,text='acosh()',bg='#537FE7',fg='#E9F8F9',font=2,command=acosh)
            bx19.pack(fill=X)
            bx20 = Button(math,text='atanh()',bg='#537FE7',fg='#E9F8F9',font=2,command=atanh)
            bx20.pack(fill=X)
            bx21 = Button(math,text='atanh()',bg='#537FE7',fg='#E9F8F9',font=2,command=atanh)
            bx21.pack(fill=X)
            bx22 = Button(math,text='pi()',bg='#537FE7',fg='#E9F8F9',font=2,command=pi)
            bx22.pack(fill=X)
            bx23 = Button(math,text='e()',bg='#537FE7',fg='#E9F8F9',font=2,command=e)
            bx23.pack(fill=X)
        #=======================================================
        Home = Frame(home,bg='#f8f8ff',width='1800',height='1000')
        Home.place(x=250,y=50)
        #--------------------------------------------------------
        def account():
            if vv.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            if vv.get() == 'Integral(  , (x))': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'Integral(  , (x , 0 , 1))': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'diff((),x)': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'limit(,x,1)': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'Matrix()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'factorial()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'log()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'sqrt()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'cbrt()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'sin()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'cos()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'tan()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'asin()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'acos()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'atan()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'sinh()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'cosh()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'tanh()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'asinh()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'acosh()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'atanh()': 
                  messagebox.showinfo("EROR",'The equation is not complete')

            get1 = vv.get()
            z = simplify(get1)
            z2 = str(pretty(z))
            Labelmain.set(z2)
        def expand2():
            if vv.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            if vv.get() == 'Integral(  , (x))': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'Integral(  , (x , 0 , 1))': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'diff((),x)': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'limit(,x,1)': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'Matrix()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'factorial()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'log()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'sqrt()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'cbrt()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'sin()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'cos()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'tan()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'asin()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'acos()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'atan()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'sinh()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'cosh()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'tanh()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'asinh()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'acosh()': 
                  messagebox.showinfo("EROR",'The equation is not complete')
            if vv.get() == 'atanh()': 
                  messagebox.showinfo("EROR",'The equation is not complete')    



            get1 = vv.get()
            z  = expand(get1)
            z2 = str(pretty(z))
            Labelmain.set(z2)
  
    
        vv = StringVar()
        Labelmain = StringVar()  
        
        functionsset = Entry(Home,bg='#f8f8ff',fg='#080808',font=2,textvariable=vv)
        functionsset.place(x=250,y=50,height=50,width=850)
        popup_menu(functionsset,Home)
        functionsset2 = Label(Home,bg='#f8f8ff',fg='#080808',font=2,text="0.0",textvariable=Labelmain)
        functionsset2.place(x=250,y=150,height=100,width=850)
        account1 = Button(Home,text=' account ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=account)
        account1.place(x=280,y=110)
        Clear1 = Button(Home,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=Clear)
        Clear1.place(x=360,y=110)
        expand22 = Button(Home,text='  expand  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=expand2)
        expand22.place(x=440,y=110)
        mainframe = Frame(Home , bg="#3F61B0",height=50,width=1800)
        mainframe.place(x=0,y=0)
        mainframe.pack_propagate(False)
        l2f = Label(mainframe,text='Home', bg="#3F61B0",fg='#E9F8F9',font=('Bold',20))
        l2f.pack(side=LEFT)
        wfd1 = Frame(Home , bg="#DFDFE6",height=1000,width=250)
        wfd1.place(x=0,y=50)
        functions_Button = Button(wfd1, text="functions",font=('Bold',25),bd=0,bg="#DFDFE6",fg='#3F61B0',activebackground='#3F61B0',activeforeground='#E9F8F9',command=math)
        functions_Button.place(x=20,y= 20)