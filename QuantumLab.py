import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from tkinter import messagebox
from tkinter import messagebox
from PIL import ImageTk, Image 
from tkinter import*
import numpy as np
import cirq



class QuantumLab():
    def QuantumLab(home):
        QuantumLab = Frame(home,bg='#f8f8ff',width='1800',height='1000')
        QuantumLab.place(x=250,y=50)
        h4f = Frame(QuantumLab , bg="#3F61B0",height=50,width=1850)
        h4f.place(x=0,y=0)
        wfdw = Frame(QuantumLab , bg="#DFDFE6",height=1000,width=250)
        wfdw.place(x=0,y=50)
        circuit = cirq.Circuit()
        qbits= cirq.LineQubit.range(25)
        
        def Gate():
            Gate = Toplevel(home)
            Gate.geometry("500x700+50+200")
            Gate.configure(background="#f8f8ff")
            Gate.resizable(False,False)
            Gate.title("Gate")
            Gate.iconbitmap('photo\logo.ico') 
            Gate.protocol("WM_DELETE_WINDOW", lambda: close_window(Gate))
            lw.config(state='disabled')
            def close_window(window):
                window.destroy()
                lw.config(state='normal')
#-----------------------------------------------------------------------------

            #---------------------------------------XGate----------------------------------------------------
            
            def XGate():
                XGate = Toplevel()
                XGate.geometry("200x200+50+200")
                XGate.configure(background="#f8f8ff")
                XGate.resizable(False,False)
                XGate.title("X-Gate")
                XGate.iconbitmap('photo\logo.ico')
                XGate.protocol("WM_DELETE_WINDOW", lambda: close_window(XGate))
                qqx1.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx1.config(state='normal')

                def addq():
                    if wqs.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax =wqs.get()
                    circuit.append(cirq.X(qbits[wsax])) 
                    asw.set(circuit)
                    
                    
                    
                wqs=IntVar() 
                zw = Label(XGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw.place(x=50,y=1,height=30,width=90)   
                za = Spinbox(XGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs,from_=0, to=24)
                za.place(x=50,y=40,height=30,width=100)
                xz = Button(XGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq)
                xz.place(x=50,y=80,width=100) 

            #---------------------------------------YGate----------------------------------------------------
            def YGate():
                YGate = Toplevel()
                YGate.geometry("200x200+50+200")
                YGate.configure(background="#f8f8ff")
                YGate.resizable(False,False)
                YGate.title("Y-Gate")
                YGate.iconbitmap('photo\logo.ico')
                YGate.protocol("WM_DELETE_WINDOW", lambda: close_window(YGate))
                qqx2.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx2.config(state='normal')

                def addq2():
                    if wqs2.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax2 =wqs2.get()
                    circuit.append(cirq.Y(qbits[wsax2])) 
                    asw.set(circuit)
                    
                    
                    
                wqs2=IntVar() 
                zw2 = Label(YGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw2.place(x=50,y=1,height=30,width=90)   
                za2 = Spinbox(YGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs2,from_=0, to=24)
                za2.place(x=50,y=40,height=30,width=100)
                xz2 = Button(YGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq2)
                xz2.place(x=50,y=80,width=100) 
                
            #---------------------------------------ZGate----------------------------------------------------
            def ZGate():
                ZGate = Toplevel()
                ZGate.geometry("200x200+50+200")
                ZGate.configure(background="#f8f8ff")
                ZGate.resizable(False,False)
                ZGate.title("Z-Gate")
                ZGate.iconbitmap('photo\logo.ico')
                ZGate.protocol("WM_DELETE_WINDOW", lambda: close_window(ZGate))
                qqx3.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx3.config(state='normal')


                def addq3():
                    if wqs3.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax3 =wqs3.get()
                    circuit.append(cirq.Z(qbits[wsax3])) 
                    asw.set(circuit)
                    
                    
                wqs3=IntVar() 
                zw3 = Label(ZGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw3.place(x=50,y=1,height=30,width=90)   
                za3 = Spinbox(ZGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs3,from_=0, to=24)
                za3.place(x=50,y=40,height=30,width=100)
                xz3 = Button(ZGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq3)
                xz3.place(x=50,y=80,width=100)

            #---------------------------------------HGate----------------------------------------------------
            def HGate():
                HGate = Toplevel()
                HGate.geometry("200x200+50+200")
                HGate.configure(background="#f8f8ff")
                HGate.resizable(False,False)
                HGate.title("H-Gate")
                HGate.iconbitmap('photo\logo.ico')
                HGate.protocol("WM_DELETE_WINDOW", lambda: close_window(HGate))
                qqx4.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx4.config(state='normal')

                def addq4():
                    if wqs4.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax4 =wqs4.get()
                    circuit.append(cirq.H(qbits[wsax4])) 
                    asw.set(circuit)
                    
                    
                    
                wqs4=IntVar() 
                zw4 = Label(HGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw4.place(x=50,y=1,height=30,width=90)   
                za4 = Spinbox(HGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs4,from_=0, to=24)
                za4.place(x=50,y=40,height=30,width=100)
                xz4 = Button(HGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq4)
                xz4.place(x=50,y=80,width=100)

            #---------------------------------------IGate----------------------------------------------------
            def IGate():
                IGate = Toplevel()
                IGate.geometry("200x200+50+200")
                IGate.configure(background="#f8f8ff")
                IGate.resizable(False,False)
                IGate.title("I-Gate")
                IGate.iconbitmap('photo\logo.ico')
                IGate.protocol("WM_DELETE_WINDOW", lambda: close_window(IGate))
                qqx5.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx5.config(state='normal')

                def addq5():
                    if wqs5.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax5 =wqs5.get()
                    circuit.append(cirq.I(qbits[wsax5])) 
                    asw.set(circuit)
                    
                    
                    
                wqs5=IntVar() 
                zw5 = Label(IGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw5.place(x=50,y=1,height=30,width=90)   
                za5 = Spinbox(IGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs5,from_=0, to=24)
                za5.place(x=50,y=40,height=30,width=100)
                xz5 = Button(IGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq5)
                xz5.place(x=50,y=80,width=100)


            #---------------------------------------TGate----------------------------------------------------
            def TGate():
                TGate = Toplevel()
                TGate.geometry("200x200+50+200")
                TGate.configure(background="#f8f8ff")
                TGate.resizable(False,False)
                TGate.title("T-Gate")
                TGate.iconbitmap('photo\logo.ico')
                TGate.protocol("WM_DELETE_WINDOW", lambda: close_window(TGate))
                qqx6.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx6.config(state='normal')


                def addq6():
                    if wqs6.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax6 =wqs6.get()
                    circuit.append(cirq.T(qbits[wsax6])) 
                    asw.set(circuit)
                    
                    
                wqs6=IntVar() 
                zw6 = Label(TGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw6.place(x=50,y=1,height=30,width=90)   
                za6 = Spinbox(TGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs6,from_=0, to=24)
                za6.place(x=50,y=40,height=30,width=100)
                xz6 = Button(TGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq6)
                xz6.place(x=50,y=80,width=100)
            
            #---------------------------------------SGate----------------------------------------------------
            def SGate():
                SGate = Toplevel()
                SGate.geometry("200x200+50+200")
                SGate.configure(background="#f8f8ff")
                SGate.resizable(False,False)
                SGate.title("S-Gate")
                SGate.iconbitmap('photo\logo.ico')
                SGate.protocol("WM_DELETE_WINDOW", lambda: close_window(SGate))
                qqx7.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx7.config(state='normal')


                def addq7():
                    if wqs7.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax7 =wqs7.get()
                    circuit.append(cirq.S(qbits[wsax7])) 
                    asw.set(circuit)
                    
                    
                wqs7=IntVar() 
                zw7 = Label(SGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw7.place(x=50,y=1,height=30,width=90)   
                za7 = Spinbox(SGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs7,from_=0, to=24)
                za7.place(x=50,y=40,height=30,width=100)
                xz7 = Button(SGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq7)
                xz7.place(x=50,y=80,width=100)

            #---------------------------------------XXGate----------------------------------------------------  
            def XXGate():
                XXGate = Toplevel()
                XXGate.geometry("200x200+50+200")
                XXGate.configure(background="#f8f8ff")
                XXGate.resizable(False,False)
                XXGate.title("XX-Gate")
                XXGate.iconbitmap('photo\logo.ico')
                XXGate.protocol("WM_DELETE_WINDOW", lambda: close_window(XXGate))
                qqx8.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx8.config(state='normal')

                def addq8():
                    if wqs8.get() == wqs9.get() : 
                            messagebox.showinfo("EROR",'A gate containing two qubits cannot be in the same place')
                    if wqs8.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs9.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax8 =wqs8.get()
                    wsax9 =wqs9.get()
                    circuit.append(cirq.XX(qbits[wsax8],qbits[wsax9])) 
                    asw.set(circuit)
                    
                    
                wqs8=IntVar() 
                wqs9=IntVar()
                zw8 = Label(XXGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw8.place(x=50,y=1,height=30,width=90)   
                za8 = Spinbox(XXGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs8,from_=0, to=24)
                za8.place(x=50,y=40,height=30,width=100)
                zw9 = Label(XXGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw9.place(x=50,y=80,height=30,width=100)   
                za9 = Spinbox(XXGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs9,from_=0, to=24)
                za9.place(x=50,y=120,height=30,width=100)
                xz9 = Button(XXGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq8)
                xz9.place(x=50,y=160,width=100)

            #---------------------------------------YYGate---------------------------------------------------- 
            def YYGate():
                YYGate = Toplevel()
                YYGate.geometry("200x200+50+200")
                YYGate.configure(background="#f8f8ff")
                YYGate.resizable(False,False)
                YYGate.title("YY-Gate")
                YYGate.iconbitmap('photo\logo.ico')
                YYGate.protocol("WM_DELETE_WINDOW", lambda: close_window(YYGate))
                qqx9.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx9.config(state='normal')

                def addq9():
                    if wqs10.get() == wqs11.get() : 
                            messagebox.showinfo("EROR",'A gate containing two qubits cannot be in the same place')
                    if wqs10.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs11.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax10 =wqs10.get()
                    wsax11 =wqs11.get()
                    circuit.append(cirq.YY(qbits[wsax10],qbits[wsax11])) 
                    asw.set(circuit)
                    
                    
                wqs10=IntVar() 
                wqs11=IntVar()
                zw10 = Label(YYGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw10.place(x=50,y=1,height=30,width=90)   
                za10 = Spinbox(YYGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs10,from_=0, to=24)
                za10.place(x=50,y=40,height=30,width=100)
                zw11 = Label(YYGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw11.place(x=50,y=80,height=30,width=100)   
                za11 = Spinbox(YYGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs11,from_=0, to=24)
                za11.place(x=50,y=120,height=30,width=100)
                xz11 = Button(YYGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq9)
                xz11.place(x=50,y=160,width=100)

            #---------------------------------------ZZGate----------------------------------------------------     
            def ZZGate():
                ZZGate = Toplevel()
                ZZGate.geometry("200x200+50+200")
                ZZGate.configure(background="#f8f8ff")
                ZZGate.resizable(False,False)
                ZZGate.title("ZZ-Gate")
                ZZGate.iconbitmap('photo\logo.ico')
                ZZGate.protocol("WM_DELETE_WINDOW", lambda: close_window(ZZGate))
                qqx10.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx10.config(state='normal')

                def addq10():
                    if wqs12.get() == wqs13.get() : 
                            messagebox.showinfo("EROR",'A gate containing two qubits cannot be in the same place')
                    if wqs12.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs13.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax12 =wqs12.get()
                    wsax13 =wqs13.get()
                    circuit.append(cirq.ZZ(qbits[wsax12],qbits[wsax13])) 
                    asw.set(circuit)
                    
                    
                wqs12=IntVar() 
                wqs13=IntVar()
                zw12 = Label(ZZGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw12.place(x=50,y=1,height=30,width=90)   
                za12 = Spinbox(ZZGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs12,from_=0, to=24)
                za12.place(x=50,y=40,height=30,width=100)
                zw13 = Label(ZZGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw13.place(x=50,y=80,height=30,width=100)   
                za13 = Spinbox(ZZGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs13,from_=0, to=24)
                za13.place(x=50,y=120,height=30,width=100)
                xz13 = Button(ZZGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq10)
                xz13.place(x=50,y=160,width=100)

            #---------------------------------------SWAPGate----------------------------------------------------   
            def SWAPGate():
                SWAPGate = Toplevel()
                SWAPGate.geometry("200x200+50+200")
                SWAPGate.configure(background="#f8f8ff")
                SWAPGate.resizable(False,False)
                SWAPGate.title("SWAP-Gate")
                SWAPGate.iconbitmap('photo\logo.ico')
                SWAPGate.protocol("WM_DELETE_WINDOW", lambda: close_window(SWAPGate))
                qqx11.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx11.config(state='normal')

                def addq11():
                    if wqs14.get() == wqs15.get() : 
                            messagebox.showinfo("EROR",'A gate containing two qubits cannot be in the same place')
                    if wqs14.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs15.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax14 =wqs14.get()
                    wsax15 =wqs15.get()
                    circuit.append(cirq.SWAP(qbits[wsax14],qbits[wsax15])) 
                    asw.set(circuit)
                    
                    
                wqs14=IntVar() 
                wqs15=IntVar()
                zw14 = Label(SWAPGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw14.place(x=50,y=1,height=30,width=90)   
                za14 = Spinbox(SWAPGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs14,from_=0, to=24)
                za14.place(x=50,y=40,height=30,width=100)
                zw15 = Label(SWAPGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw15.place(x=50,y=80,height=30,width=100)   
                za15 = Spinbox(SWAPGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs15,from_=0, to=24)
                za15.place(x=50,y=120,height=30,width=100)
                xz15 = Button(SWAPGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq11)
                xz15.place(x=50,y=160,width=100)

            #---------------------------------------CNOTGate----------------------------------------------------  
            def CNOTGate():
                CNOTGate = Toplevel()
                CNOTGate.geometry("200x200+50+200")
                CNOTGate.configure(background="#f8f8ff")
                CNOTGate.resizable(False,False)
                CNOTGate.title("C-NOT-Gate")
                CNOTGate.iconbitmap('photo\logo.ico')
                CNOTGate.protocol("WM_DELETE_WINDOW", lambda: close_window(CNOTGate))
                qqx12.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx12.config(state='normal')

                def addq12():
                    if wqs16.get() == wqs17.get() : 
                            messagebox.showinfo("EROR",'A gate containing two qubits cannot be in the same place')
                    if wqs16.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs17.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax16 =wqs16.get()
                    wsax17 =wqs17.get()
                    circuit.append(cirq.CNOT(qbits[wsax16],qbits[wsax17])) 
                    asw.set(circuit)
                    
                    
                wqs16=IntVar() 
                wqs17=IntVar()
                zw16 = Label(CNOTGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw16.place(x=50,y=1,height=30,width=90)   
                za16 = Spinbox(CNOTGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs16,from_=0, to=24)
                za16.place(x=50,y=40,height=30,width=100)
                zw17 = Label(CNOTGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw17.place(x=50,y=80,height=30,width=100)   
                za17 = Spinbox(CNOTGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs17,from_=0, to=24)
                za17.place(x=50,y=120,height=30,width=100)
                xz17 = Button(CNOTGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq12)
                xz17.place(x=50,y=160,width=100)

            #---------------------------------------CCXGate----------------------------------------------------   
            def CCXGate():
                CCXGate = Toplevel()
                CCXGate.geometry("200x300+50+200")
                CCXGate.configure(background="#f8f8ff")
                CCXGate.resizable(False,False)
                CCXGate.title("CCX-Gate")
                CCXGate.iconbitmap('photo\logo.ico')
                CCXGate.protocol("WM_DELETE_WINDOW", lambda: close_window(CCXGate))
                qqx13.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx13.config(state='normal')

                def addq13():
                    if wqs18.get() == wqs19.get() or wqs18.get() == wqs20.get() or wqs19.get() == wqs20.get(): 
                            messagebox.showinfo("EROR",'A gate containing two qubits cannot be in the same place')
                    if wqs18.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs19.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs20.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax18 =wqs18.get()
                    wsax19 =wqs19.get()
                    wsax20 =wqs20.get()
                    circuit.append(cirq.CCX(qbits[wsax18],qbits[wsax19],qbits[wsax20])) 
                    asw.set(circuit)
                    
                    
                wqs18=IntVar() 
                wqs19=IntVar()
                wqs20=IntVar()
                zw18 = Label(CCXGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw18.place(x=50,y=1,height=30,width=90)   
                za18 = Spinbox(CCXGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs18,from_=0, to=24)
                za18.place(x=50,y=40,height=30,width=100)
                zw19 = Label(CCXGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw19.place(x=50,y=80,height=30,width=100)   
                za19 = Spinbox(CCXGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs19,from_=0, to=24)
                za19.place(x=50,y=120,height=30,width=100)
                zw20 = Label(CCXGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw20.place(x=50,y=160,height=30,width=100)   
                za20 = Spinbox(CCXGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs20,from_=0, to=24)
                za20.place(x=50,y=200,height=30,width=100)
                xz20 = Button(CCXGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq13)
                xz20.place(x=50,y=240,width=100)

            #---------------------------------------CCZGate----------------------------------------------------   
            def CCZGate():
                CCZGate = Toplevel()
                CCZGate.geometry("200x300+50+200")
                CCZGate.configure(background="#f8f8ff")
                CCZGate.resizable(False,False)
                CCZGate.title("CCZ-Gate")
                CCZGate.iconbitmap('photo\logo.ico')
                CCZGate.protocol("WM_DELETE_WINDOW", lambda: close_window(CCZGate))
                qqx14.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx14.config(state='normal')

                def addq14():
                    if wqs21.get() == wqs22.get() or wqs21.get() == wqs23.get() or wqs22.get() == wqs23.get(): 
                            messagebox.showinfo("EROR",'A gate containing two qubits cannot be in the same place')
                    if wqs21.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs22.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs23.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax21 =wqs21.get()
                    wsax22 =wqs22.get()
                    wsax23 =wqs23.get()
                    circuit.append(cirq.CCZ(qbits[wsax21],qbits[wsax22],qbits[wsax23])) 
                    asw.set(circuit)
                    
                    
                wqs21=IntVar() 
                wqs22=IntVar()
                wqs23=IntVar()
                zw21 = Label(CCZGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw21.place(x=50,y=1,height=30,width=90)   
                za21 = Spinbox(CCZGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs21,from_=0, to=24)
                za21.place(x=50,y=40,height=30,width=100)
                zw22 = Label(CCZGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw22.place(x=50,y=80,height=30,width=100)   
                za22 = Spinbox(CCZGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs22,from_=0, to=24)
                za22.place(x=50,y=120,height=30,width=100)
                zw23 = Label(CCZGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw23.place(x=50,y=160,height=30,width=100)   
                za23 = Spinbox(CCZGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs23,from_=0, to=24)
                za23.place(x=50,y=200,height=30,width=100)
                xz23 = Button(CCZGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq14)
                xz23.place(x=50,y=240,width=100)

            #---------------------------------------CCNOTGate----------------------------------------------------  
            def CCNOTGate():
                CCNOTGate = Toplevel()
                CCNOTGate.geometry("200x300+50+200")
                CCNOTGate.configure(background="#f8f8ff")
                CCNOTGate.resizable(False,False)
                CCNOTGate.title("CCNOT-Gate")
                CCNOTGate.iconbitmap('photo\logo.ico')
                CCNOTGate.protocol("WM_DELETE_WINDOW", lambda: close_window(CCNOTGate))
                qqx15.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx15.config(state='normal')

                def addq15():
                    if wqs24.get() == wqs25.get() or wqs24.get() == wqs26.get() or wqs25.get() == wqs26.get(): 
                            messagebox.showinfo("EROR",'A gate containing two qubits cannot be in the same place')
                    if wqs24.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs25.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs26.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax24 =wqs24.get()
                    wsax25 =wqs25.get()
                    wsax26 =wqs26.get()
                    circuit.append(cirq.CCNOT(qbits[wsax24],qbits[wsax25],qbits[wsax26])) 
                    asw.set(circuit)
                    
                    
                wqs24=IntVar() 
                wqs25=IntVar()
                wqs26=IntVar()
                zw24 = Label(CCNOTGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw24.place(x=50,y=1,height=30,width=90)   
                za24 = Spinbox(CCNOTGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs24,from_=0, to=24)
                za24.place(x=50,y=40,height=30,width=100)
                zw25 = Label(CCNOTGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw25.place(x=50,y=80,height=30,width=100)   
                za25 = Spinbox(CCNOTGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs25,from_=0, to=24)
                za25.place(x=50,y=120,height=30,width=100)
                zw26 = Label(CCNOTGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw26.place(x=50,y=160,height=30,width=100)   
                za26 = Spinbox(CCNOTGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs26,from_=0, to=24)
                za26.place(x=50,y=200,height=30,width=100)
                xz26 = Button(CCNOTGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq15)
                xz26.place(x=50,y=240,width=100)

            #---------------------------------------CSWAPGate----------------------------------------------------  
            def CSWAPGate():
                CSWAPGate = Toplevel()
                CSWAPGate.geometry("200x300+50+200")
                CSWAPGate.configure(background="#f8f8ff")
                CSWAPGate.resizable(False,False)
                CSWAPGate.title("CSWAP-Gate")
                CSWAPGate.iconbitmap('photo\logo.ico')
                CSWAPGate.protocol("WM_DELETE_WINDOW", lambda: close_window(CSWAPGate))
                qqx16.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx16.config(state='normal')

                def addq16():
                    if wqs27.get() == wqs28.get() or wqs27.get() == wqs29.get() or wqs28.get() == wqs29.get(): 
                            messagebox.showinfo("EROR",'A gate containing two qubits cannot be in the same place')
                    if wqs27.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs28.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs29.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax27 =wqs27.get()
                    wsax28 =wqs28.get()
                    wsax29 =wqs29.get()
                    circuit.append(cirq.CSWAP(qbits[wsax27],qbits[wsax28],qbits[wsax29])) 
                    asw.set(circuit)
                    
                    
                wqs27=IntVar() 
                wqs28=IntVar()
                wqs29=IntVar()
                zw27 = Label(CSWAPGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw27.place(x=50,y=1,height=30,width=90)   
                za27 = Spinbox(CSWAPGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs27,from_=0, to=24)
                za27.place(x=50,y=40,height=30,width=100)
                zw28 = Label(CSWAPGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw28.place(x=50,y=80,height=30,width=100)   
                za28 = Spinbox(CSWAPGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs28,from_=0, to=24)
                za28.place(x=50,y=120,height=30,width=100)
                zw29 = Label(CSWAPGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw29.place(x=50,y=160,height=30,width=100)   
                za29 = Spinbox(CSWAPGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs29,from_=0, to=24)
                za29.place(x=50,y=200,height=30,width=100)
                xz29 = Button(CSWAPGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq16)
                xz29.place(x=50,y=240,width=100)

            #---------------------------------------FREDKINGate----------------------------------------------------  
            def FREDKINGate():
                FREDKINGate = Toplevel()
                FREDKINGate.geometry("200x300+50+200")
                FREDKINGate.configure(background="#f8f8ff")
                FREDKINGate.resizable(False,False)
                FREDKINGate.title("FREDKIN-Gate")
                FREDKINGate.iconbitmap('photo\logo.ico')
                FREDKINGate.protocol("WM_DELETE_WINDOW", lambda: close_window(FREDKINGate))
                qqx17.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx17.config(state='normal')

                def addq17():
                    if wqs30.get() == wqs31.get() or wqs30.get() == wqs32.get() or wqs31.get() == wqs32.get(): 
                            messagebox.showinfo("EROR",'A gate containing two qubits cannot be in the same place')
                    if wqs30.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs31.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    if wqs32.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax30 =wqs30.get()
                    wsax31 =wqs31.get()
                    wsax32 =wqs32.get()
                    circuit.append(cirq.FREDKIN(qbits[wsax30],qbits[wsax31],qbits[wsax32])) 
                    asw.set(circuit)
                    
                    
                wqs30=IntVar() 
                wqs31=IntVar()
                wqs32=IntVar()
                zw30 = Label(FREDKINGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw30.place(x=50,y=1,height=30,width=90)   
                za30 = Spinbox(FREDKINGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs30,from_=0, to=24)
                za30.place(x=50,y=40,height=30,width=100)
                zw31 = Label(FREDKINGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw31.place(x=50,y=80,height=30,width=100)   
                za31 = Spinbox(FREDKINGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs31,from_=0, to=24)
                za31.place(x=50,y=120,height=30,width=100)
                zw32 = Label(FREDKINGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw32.place(x=50,y=160,height=30,width=100)   
                za32 = Spinbox(FREDKINGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs32,from_=0, to=24)
                za32.place(x=50,y=200,height=30,width=100)
                xz32 = Button(FREDKINGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq17)
                xz32.place(x=50,y=240,width=100)

            #---------------------------------------MeasurementGate----------------------------------------------------
            def MeasurementGate():
                MeasurementGate = Toplevel()
                MeasurementGate.geometry("200x400+50+200")
                MeasurementGate.configure(background="#f8f8ff")
                MeasurementGate.resizable(False,False)
                MeasurementGate.title("Measurement-Gate")
                MeasurementGate.iconbitmap('photo\logo.ico')
                MeasurementGate.protocol("WM_DELETE_WINDOW", lambda: close_window(MeasurementGate))
                qqx18.config(state='disabled')
                def close_window(window):
                    window.destroy()
                    qqx18.config(state='normal')

                def addq18():
                    if wqs33.get() >= 25 : 
                            messagebox.showinfo("Qubit number",'The maximum number of Qubits is 25 from 0 to 24')
                    wsax33 =wqs33.get()
                    circuit.append(cirq.measure(qbits[wsax33]))
                    asw.set(circuit)

                def addq19(): 
                    xs = wqs34.get()
                    ys = wqs35.get()      
                    for i in range(xs,ys):
                        circuit.append(cirq.measure(qbits[i]))
                        asw.set(circuit)
                wqs33=IntVar() 
                zw12 = Label(MeasurementGate,text='Qubit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw12.place(x=50,y=1,height=30,width=90)   
                za13 = Spinbox(MeasurementGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs33,from_=0, to=24)
                za13.place(x=50,y=40,height=30,width=100)
                xz14 = Button(MeasurementGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq18)
                xz14.place(x=50,y=80,width=100)
                
                wqs34=IntVar()
                wqs35=IntVar()
                zw34 = Label(MeasurementGate,text='start number',bg='#f8f8ff',fg='#080808',font=2)    
                zw34.place(x=50,y=120,height=30,width=90)  
                za34 = Spinbox(MeasurementGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs34,from_=0, to=24)
                za34.place(x=50,y=160,height=30,width=100)
                zw35 = Label(MeasurementGate,text='End number',bg='#f8f8ff',fg='#080808',font=2)    
                zw35.place(x=50,y=200,height=30,width=100)  
                za35 = Spinbox(MeasurementGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs35,from_=0, to=24)
                za35.place(x=50,y=240,height=30,width=100)
                xz35 = Button(MeasurementGate,text=' Add all',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq19)
                xz35.place(x=50,y=280,width=100)


        
            
            qqx1 = Button(Gate,text='X-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=XGate)
            qqx1.place(x=1,y=1,width='495')
            qqx2 = Button(Gate,text='Y-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=YGate)
            qqx2.place(x=1,y=30,width='495')
            qqx3 = Button(Gate,text='Z-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=ZGate)
            qqx3.place(x=1,y=60,width='495')
            qqx4 = Button(Gate,text='H-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=HGate)
            qqx4.place(x=1,y=90,width='495')
            qqx5 = Button(Gate,text='I-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=IGate)
            qqx5.place(x=1,y=120,width='495')
            qqx6 = Button(Gate,text='T-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=TGate)
            qqx6.place(x=1,y=150,width='495')
            qqx7 = Button(Gate,text='S-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=SGate)
            qqx7.place(x=1,y=180,width='495')
            qqx8 = Button(Gate,text='XX-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=XXGate)
            qqx8.place(x=1,y=210,width='495')
            qqx9 = Button(Gate,text='YY-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=YYGate)
            qqx9.place(x=1,y=240,width='495')
            qqx10 = Button(Gate,text='ZZ-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=ZZGate)
            qqx10.place(x=1,y=270,width='495')
            qqx11 = Button(Gate,text='SWAP-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=SWAPGate)
            qqx11.place(x=1,y=300,width='495')
            qqx12 = Button(Gate,text='CNOT-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=CNOTGate)
            qqx12.place(x=1,y=330,width='495')
            qqx13 = Button(Gate,text='CCX-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=CCXGate)
            qqx13.place(x=1,y=360,width='495')
            qqx14 = Button(Gate,text='CCZ-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=CCZGate)
            qqx14.place(x=1,y=390,width='495')
            qqx15 = Button(Gate,text='CCNOT-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=CCNOTGate)
            qqx15.place(x=1,y=420,width='495')
            qqx16 = Button(Gate,text='CSWAP-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=CSWAPGate)
            qqx16.place(x=1,y=450,width='495')
            qqx17 = Button(Gate,text='FREDKIN-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=FREDKINGate)
            qqx17.place(x=1,y=480,width='495')
            qqx18 = Button(Gate,text='Measurement-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=MeasurementGate)
            qqx18.place(x=1,y=510,width='495')

            #----------------------------
        #------Simulation-------------
        def Simulation():
            if sad.get() == '': 
                  messagebox.showinfo("Simulation",'Add a Measurement-Gate to each Qubit')
            Simulation = Toplevel(home)
            Simulation.geometry("500x600+50+200")
            Simulation.configure(background="#f8f8ff")
            Simulation.resizable(False,False)
            Simulation.title("Simulation")
            Simulation.iconbitmap('photo\logo.ico')
            Simulation.protocol("WM_DELETE_WINDOW", lambda: close_window(Simulation))
            lw2.config(state='disabled')
            def close_window(window):
                window.destroy()
                lw2.config(state='normal')
            #------------------------------------------------
            mainframe2 = Frame(Simulation , bg="#3F61B0",height=50,width=1800)
            mainframe2.place(x=0,y=0)
            mainframe2.pack_propagate(False)
            l2f2 = Label(mainframe2,text='Simulation', bg="#3F61B0",fg='#E9F8F9',font=('Bold',20))
            l2f2.pack(side=LEFT) 

            def ssml():   
                if sad.get() == '': 
                    messagebox.showinfo("Simulation",'Add a Measurement-Gate to each Qubit')
                rr = sim.run(circuit)
                rr2 = sim.run(circuit,repetitions=20)
                sad.set(rr) 
                sad2.set(rr2)
             
            xz14 = Button(Simulation,text=' Simulation ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=ssml)
            xz14.place(x=15,y=60)  
            waa = Label(Simulation,bg='#f8f8ff',fg='#080808',font=2,text="0.0",height=26,width=10,textvariable=sad,anchor="n")
            waa.place(x=15,y=100)    
            sim = cirq.Simulator()
            rr = sim.run(circuit) 
            sad.set(rr)

            rr2 = sim.run(circuit,repetitions=20)   
            sad2.set(rr2)
            waa2 = Label(Simulation,bg='#f8f8ff',fg='#080808',font=2,text="0.0",height=26,width=25,textvariable=sad2,anchor="n")
            waa2.place(x=180,y=100)                   
        #--------------------------------------------------------
        def blochsphere():
            if sad.get() == '': 
                messagebox.showinfo("blochsphere",'Building a quantum circuit to simulate the blochsphere')
                def cirq_state_to_bloch_coordinates(qubit_state):
                    x = 2 * np.real(np.conj(qubit_state[0]) * qubit_state[1])
                    y = 2 * np.imag(np.conj(qubit_state[1]) * qubit_state[0])
                    z = np.abs(qubit_state[0])**2 - np.abs(qubit_state[1])**2
                    return x, y, z
                def plot_bloch_sphere(qubit_state):
                    fig = plt.figure(figsize=(6, 6))
                    ax = fig.add_subplot(111, projection="3d")

                    # Set sphere color and alpha
                    ax.set_facecolor((0.95, 0.95, 0.95))
                    ax.alpha = 0.1

                    # Create grid of sphere points
                    u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]
                    x = np.cos(u)*np.sin(v)
                    y = np.sin(u)*np.sin(v)
                    z = np.cos(v)
                    ax.plot_wireframe(x, y, z, color="gray", alpha=0.2)

                    # Plot the Bloch vector and basis vectors
                    x, y, z = cirq_state_to_bloch_coordinates(qubit_state)
                    plot_bloch_vector([0, 0, 1], ax=ax)
                    plot_bloch_vector([1, 0, 0], ax=ax)
                    plot_bloch_vector([0, 1, 0], ax=ax)
                    plot_bloch_vector([x, y, z], ax=ax)

                    # Set plot limits and axis labels
                    ax.set_xlim(-1.2, 1.2)
                    ax.set_ylim(-1.2, 1.2)
                    ax.set_zlim(-1.2, 1.2)
                    ax.set_xlabel("X")
                    ax.set_ylabel("Y")
                    ax.set_zlabel("Z")

                    plt.show()
                    
                def plot_bloch_vector(vector, ax):
                    ax.plot([0,vector[0]], [0,vector[1]], [0,vector[2]], 
                            linewidth=2, marker='o', markersize=8)
                        
                simulator = cirq.Simulator()
                result = simulator.simulate(circuit)
                state_vector = result.final_state_vector
                plot_bloch_sphere(state_vector)
        #--------------------------------------
        def Clear_circuit():
            circuit[:] = []   
            asw.set(circuit)
        #--------------------------------------
        asw=StringVar()
        sad=StringVar() 
        sad2=StringVar()     
        waa = Label(QuantumLab,bg='#f8f8ff',fg='#080808',font=2,text="0.0",anchor="nw",height=50,width=160,textvariable=asw)
        waa.place(x=250,y=50)    
        #--------------------------------------
        lw = Button(wfdw, text="Gate",font=('Bold',20),bd=0,bg="#DFDFE6",fg='#3F61B0',activebackground='#3F61B0',activeforeground='#E9F8F9',command=Gate)
        lw.place(x=20,y= 20)
        lw2 = Button(wfdw, text="Simulation",font=('Bold',20),bd=0,bg="#DFDFE6",fg='#3F61B0',activebackground='#3F61B0',activeforeground='#E9F8F9',command=Simulation)
        lw2.place(x=20,y= 80)
        lw3 = Button(wfdw, text="Bloch Sphere",font=('Bold',20),bd=0,bg="#DFDFE6",fg='#3F61B0',activebackground='#3F61B0',activeforeground='#E9F8F9',command=blochsphere)
        lw3.place(x=20,y= 140)
        lw4 = Button(wfdw, text="Clear Circuit",font=('Bold',20),bd=0,bg="#DFDFE6",fg='#3F61B0',activebackground='#3F61B0',activeforeground='#E9F8F9',command=Clear_circuit)
        lw4.place(x=20,y= 200)
        #--------------------------------------
        h4f.pack_propagate(False)
        l4f = Label(h4f,text='Quantum Lab', bg="#3F61B0",fg='#E9F8F9',font=('Bold',20))
        l4f.pack(side=LEFT)
        #--------------------------------------
        
          