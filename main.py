#---------modules--------------------------
import cirq
import numpy as np
from tkinter import*
from moudules.physics import*
import webbrowser as w
from matplotlib import*
from tkinter import ttk
from numpy import sin, cos
from sympy import symbols
from sympy import simplify
from collections import deque
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
#--------------------------------------------
from Home import*
from QuantumLab import*
from PhysicsLab import*
from About import*
#--------------------------------------------
home = Tk()
home.geometry("1350x700+300+200")
home.title("PsiLab")
home.iconbitmap('photo\logo.ico')
home.configure(background="#f8f8ff")
home.resizable(False,False)
#----------------------------------------------------------------
fr1 = Frame(home,bg='#f8f8ff',width='1100',height='650')
fr1.place(x=250,y=50)
#----------------------------------------------------------------
ff = PhotoImage(file="photo\logo-01.png")
eww42 = Label(home,bg='#f8f8ff',fg='#080808',font=2,height=1100,width=650)
eww42.place(x=458,y=-170)
eww42.config(image = ff)
#----------------------------------------------------------------
About.About(home)
#======================================================================================
def Homea():
     Home.Home(home)
def PhysicsLaba():
     PhysicsLab.PhysicsLab(home)   
def QuantumLaba():
     QuantumLab.QuantumLab(home)
###--------------------------------------------------------------
def existing_open():
    def existing_close():
        existing1.destroy()
        existing_Button.config(text='☰')
        existing_Button.config(command=existing_open)
    existing1 = Frame(home,height=home.winfo_height(),width=250,bg="#3F61B0")
    existing1.place(x=0,y=50)
    existing_Button.config(text='X')
    existing_Button.config(command=existing_close)
    #------------Button-----------------------
    l = Button(existing1, text="Home",font=('Bold',20),bd=0,bg="#3F61B0",fg='#E9F8F9',activebackground='#3F61B0',activeforeground='#E9F8F9',command=Homea)
    l.place(x=40,y= 20)
    l2 = Button(existing1, text="Physics Lab",font=('Bold',20),bd=0,bg="#3F61B0",fg='#E9F8F9',activebackground='#3F61B0',activeforeground='#E9F8F9',command=PhysicsLaba)
    l2.place(x=40,y= 80) 
    l3 = Button(existing1, text="Quantum Lab",font=('Bold',20),bd=0,bg="#3F61B0",fg='#E9F8F9',activebackground='#3F61B0',activeforeground='#E9F8F9',command=QuantumLaba)
    l3.place(x=40,y= 140)
########################
def quita():
     em = messagebox.askyesno("close",'do you want to close')
     if em == 1 :
          home.quit()
mn = Menu(home)
f = Menu(mn,tearoff=0)
f.add_separator()
f.add_command(label='Exit',command=quita)
mn.add_cascade(label='File',menu=f)
home.config(menu=mn)
##################
existing = Frame(home,bg="#537FE7",height=50,highlightbackground='#537FE7',highlightthickness=2)
existing_Button = Button(existing,text="☰" , bg="#537FE7",fg='#E9F8F9',font=('Bold',20), bd=0,activebackground='#537FE7',activeforeground='#E9F8F9',command=existing_open)
existing_Button.pack(side=LEFT)
existing.pack(side=TOP,fill=X)
existing.pack_propagate(False)
Program_name = Label(existing,text='PsiLab', bg="#537FE7",fg='#E9F8F9',font=('Bold',20))
Program_name.pack(side=LEFT)
home.mainloop()





