import cirq
from tkinter import*
from tkinter import messagebox
from tkinter import messagebox

class QuantumLab():
    def QuantumLab(home):
        QuantumLab = Frame(home,bg='#f8f8ff',width='1100',height='650')
        QuantumLab.place(x=250,y=50)
        h4f = Frame(QuantumLab , bg="#3F61B0",height=50,width=1350)
        h4f.place(x=0,y=0)
        wfdw = Frame(QuantumLab , bg="#DFDFE6",height=650,width=250)
        wfdw.place(x=0,y=50)
        circuit = cirq.Circuit()
        qbits= cirq.LineQubit.range(10)
        
        
        def Gate():
            
            Gate = Toplevel()
            Gate.geometry("500x700+50+200")
            Gate.configure(background="#f8f8ff")
            Gate.resizable(False,False)
            Gate.title("Gate")
            Gate.iconbitmap('photo\logo.ico') 
            #---------------------------
            
            def HGate():
                HGate = Toplevel()
                HGate.geometry("200x200+50+200")
                HGate.configure(background="#f8f8ff")
                HGate.resizable(False,False)
                HGate.title("H-Gate")
                HGate.iconbitmap('photo\logo.ico')
                
                def addq():
                    if wqs.get() >= 10 : 
                            messagebox.showinfo("Qbit number",'The maximum number of qubits is 10 from 0 to 9')
                    wsax =wqs.get()
                    circuit.append(cirq.H(qbits[wsax])) 
                    asw.set(circuit)
                    
                    
                    
                wqs=IntVar() 
                zw = Label(HGate,text='Qbit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw.place(x=50,y=1,height=30,width=90)   
                za = Entry(HGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs)
                za.place(x=70,y=40,height=30,width=50)
                xz2 = Button(HGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq)
                xz2.place(x=70,y=80)
                
            def ZGate():
                ZGate = Toplevel()
                ZGate.geometry("200x200+50+200")
                ZGate.configure(background="#f8f8ff")
                ZGate.resizable(False,False)
                ZGate.title("Z-Gate")
                ZGate.iconbitmap('photo\logo.ico')



                def addq2():
                    if wqs2.get() >= 10 : 
                            messagebox.showinfo("Qbit number",'The maximum number of qubits is 10 from 0 to 9')
                    wsax2 =wqs2.get()
                    circuit.append(cirq.Z(qbits[wsax2])) 
                    asw.set(circuit)
                    
                    
                wqs2=IntVar() 
                zw2 = Label(ZGate,text='Qbit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw2.place(x=50,y=1,height=30,width=90)   
                za2 = Entry(ZGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs2)
                za2.place(x=70,y=40,height=30,width=50)
                xz3 = Button(ZGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq2)
                xz3.place(x=70,y=80)

                
            def SWAPGate():
                SWAPGate = Toplevel()
                SWAPGate.geometry("200x200+50+200")
                SWAPGate.configure(background="#f8f8ff")
                SWAPGate.resizable(False,False)
                SWAPGate.title("SWAP-Gate")
                SWAPGate.iconbitmap('photo\logo.ico')


                def addq3():
                    if wqs3.get() == wqs4.get() : 
                            messagebox.showinfo("EROR",'A gate containing two qubits cannot be in the same place')
                    if wqs3.get() >= 10 : 
                            messagebox.showinfo("Qbit number",'The maximum number of qubits is 10 from 0 to 9')
                    if wqs4.get() >= 10 : 
                            messagebox.showinfo("Qbit number",'The maximum number of qubits is 10 from 0 to 9')
                    wsax3 =wqs3.get()
                    wsax4 =wqs4.get()
                    circuit.append(cirq.SWAP(qbits[wsax3],qbits[wsax4])) 
                    asw.set(circuit)
                    
                    
                wqs3=IntVar() 
                wqs4=IntVar()
                zw3 = Label(SWAPGate,text='Qbit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw3.place(x=50,y=1,height=30,width=90)   
                za3 = Entry(SWAPGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs3)
                za3.place(x=70,y=40,height=30,width=50)
                zw4 = Label(SWAPGate,text='Qbit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw4.place(x=50,y=80,height=30,width=90)   
                za5 = Entry(SWAPGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs4)
                za5.place(x=70,y=120,height=30,width=50)
                xz6 = Button(SWAPGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq3)
                xz6.place(x=70,y=160)

                
            def CNOTGate():
                CNOTGate = Toplevel()
                CNOTGate.geometry("200x200+50+200")
                CNOTGate.configure(background="#f8f8ff")
                CNOTGate.resizable(False,False)
                CNOTGate.title("C-NOT-Gate")
                CNOTGate.iconbitmap('photo\logo.ico')
                
                def addq3():
                    if wqs5.get() == wqs6.get() : 
                            messagebox.showinfo("EROR",'A gate containing two qubits cannot be in the same place')
                    if wqs5.get() >= 10 : 
                            messagebox.showinfo("Qbit number",'The maximum number of qubits is 10 from 0 to 9')
                    if wqs6.get() >= 10 : 
                            messagebox.showinfo("Qbit number",'The maximum number of qubits is 10 from 0 to 9')
                    wsax5 =wqs5.get()
                    wsax6 =wqs6.get()
                    circuit.append(cirq.CNOT(qbits[wsax5],qbits[wsax6])) 
                    asw.set(circuit)
                    
                    
                wqs5=IntVar() 
                wqs6=IntVar()
                zw7 = Label(CNOTGate,text='Qbit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw7.place(x=50,y=1,height=30,width=90)   
                za8 = Entry(CNOTGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs5)
                za8.place(x=70,y=40,height=30,width=50)
                zw9 = Label(CNOTGate,text='Qbit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw9.place(x=50,y=80,height=30,width=90)   
                za10 = Entry(CNOTGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs6)
                za10.place(x=70,y=120,height=30,width=50)
                xz11 = Button(CNOTGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq3)
                xz11.place(x=70,y=160)


            def MeasurementGate():
                MeasurementGate = Toplevel()
                MeasurementGate.geometry("200x200+50+200")
                MeasurementGate.configure(background="#f8f8ff")
                MeasurementGate.resizable(False,False)
                MeasurementGate.title("Measurement-Gate")
                MeasurementGate.iconbitmap('photo\logo.ico')
                

                def addq5():
                    if wqs7.get() >= 10 : 
                            messagebox.showinfo("Qbit number",'The maximum number of qubits is 10 from 0 to 9')
                    wsax7 =wqs7.get()
                    circuit.append(cirq.measure(qbits[wsax7]))
                    asw.set(circuit)
                    
                    
                wqs7=IntVar() 
                zw12 = Label(MeasurementGate,text='Qbit number',bg='#f8f8ff',fg='#080808',font=2)    
                zw12.place(x=50,y=1,height=30,width=90)   
                za13 = Entry(MeasurementGate,bg='#f8f8ff',fg='#080808',font=2,textvariable=wqs7)
                za13.place(x=70,y=40,height=30,width=50)
                xz14 = Button(MeasurementGate,text=' Add ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=addq5)
                xz14.place(x=70,y=80)

                
            
            
            qqx1 = Button(Gate,text='H-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=HGate)
            qqx1.place(x=1,y=1,width='495')
            qqx2 = Button(Gate,text='Z-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=ZGate)
            qqx2.place(x=1,y=30,width='495')
            qqx3 = Button(Gate,text='SWAP-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=SWAPGate)
            qqx3.place(x=1,y=60,width='495')
            qqx4 = Button(Gate,text='C-NOT-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=CNOTGate)
            qqx4.place(x=1,y=90,width='495')
            qqx4 = Button(Gate,text='Measurement-Gate',bg='#537FE7',fg='#E9F8F9',font=2,command=MeasurementGate)
            qqx4.place(x=1,y=120,width='495')
            #----------------------------
        #------Simulation-------------
        def Simulation():
            if sad.get() == '': 
                  messagebox.showinfo("Simulation",'Add a Measurement-Gate to each qubit')
            sim = cirq.Simulator()
            rr = sim.run(circuit)    
            sad.set(rr)
        #--------------------------------------    
        
        asw=StringVar()
        sad=StringVar()    
        
        waa = Label(QuantumLab,bg='#f8f8ff',fg='#080808',font=2,text="0.0",height=24,width=95,textvariable=asw)
        waa.place(x=250,y=200)
        waa = Label(QuantumLab,bg='#f8f8ff',fg='#080808',font=2,text="0.0",height=10,width=10,textvariable=sad)
        waa.place(x=850,y=50)
        waa1 = Label(QuantumLab,bg='#f8f8ff',fg='#080808',text="Simulation",font=4)
        waa1.place(x=780,y=60)
        #--------------------------------------
        lw = Button(wfdw, text="Gate",font=('Bold',20),bd=0,bg="#DFDFE6",fg='#3F61B0',activebackground='#3F61B0',activeforeground='#E9F8F9',command=Gate)
        lw.place(x=20,y= 20)
        lw2 = Button(wfdw, text="Simulation",font=('Bold',20),bd=0,bg="#DFDFE6",fg='#3F61B0',activebackground='#3F61B0',activeforeground='#E9F8F9',command=Simulation)
        lw2.place(x=20,y= 80)
        #--------------------------------------
        h4f.pack_propagate(False)
        l4f = Label(h4f,text='Quantum Lab', bg="#3F61B0",fg='#E9F8F9',font=('Bold',20))
        l4f.pack(side=LEFT)