import numpy as np
from tkinter import*
from moudules.physics import*
from matplotlib import*
from tkinter import ttk
from numpy import sin, cos
from sympy import symbols
from sympy import simplify
from PIL import ImageTk, Image 
from collections import deque
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from tkinter import messagebox
#----------------------------------------------------------------
from hide import*
from popup_menu import*
#----------------------------------------------------------------
class PhysicsLab():   
    def PhysicsLab(home):
        PhysicsLab = Frame(home,bg='#f8f8ff',width='1800',height='1000')
        PhysicsLab.place(x=250,y=50)
        h3f = Frame(PhysicsLab , bg="#3F61B0",height=50,width=1850)
        h3f.place(x=0,y=0)
        h3f.pack_propagate(False)
        l3f = Label(h3f,text='Physics Lab', bg="#3F61B0",fg='#E9F8F9',font=('Bold',20))
        l3f.pack(side=LEFT)
        wfd = Frame(PhysicsLab , bg="#DFDFE6",height=1000,width=250)
        wfd.place(x=0,y=50)
        wfd.pack_propagate(False)
        wfd2 = Frame(PhysicsLab , bg="#f8f8ff",height=1000,width=1000)
        wfd2.place(x=250,y=50)
        #-------------------------------------------------------
        d3np = ttk.Notebook(wfd2)
    #----------------------MechanicalPhysics--------------------------------------
    #------------------------------------data------------------
    #------------------------------statica-----------------
        def functionssetphysics1():

            if wr1.get() == '' or dr1.get() == '' or fr1.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p1 =float(wr1.get())
            p2 =float(dr1.get())
            p3 =float(fr1.get())
            q = volume(p1,p2,p3)
            p.set(q)
        
        wr1=StringVar()
        dr1=StringVar()
        fr1=StringVar()
        p=StringVar()


        def mm():
            if wr1.get() == '' or dr1.get() == '' or fr1.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            x = int(wr1.get())
            y = int(dr1.get())
            z = int(fr1.get())
            cube = np.ones((x,z,y), dtype = 'bool')
            fig =plt.figure()
            ax = plt.axes(projection = '3d')
            ax.voxels(cube, facecolor = '#f8f8ff',edgecolors ='k')
            plt.show()

        volume1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til = Frame(volume1,width='250',height='1000',bg='#EDEDF5')
        bqit = Button(til,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(volume1,ew,ew2,ew3,p))
        lw = Label(til,text='length',bg='#EDEDF5',fg='#080808',font=2)
        ew = Entry(til,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr1)
        lw2 = Label(til,text='height',bg='#EDEDF5',fg='#080808',font=2)
        ew2 = Entry(til,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr1)
        lw3 = Label(til,text='Width',bg='#EDEDF5',fg='#080808',font=2)
        ew3 = Entry(til,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr1)
        ba = Button(til,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics1)
        aa = Button(til,text='simulation',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=mm)
        aa2a = Button(til,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew,ew2,ew3,p))
        la =Label(volume1,text="volume = ",bg='#f8f8ff',fg='#080808',font=20,)
        lla = Label(volume1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p)
        popup_menu(ew,d3np)
        popup_menu(ew2,d3np)
        popup_menu(ew3,d3np)
        #-------------------------------------------

        def functionssetphysics2():

            if wr2.get() == '' or dr2.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p4 =float(wr2.get())
            p5 =float(dr2.get())
            q2 =  density(p4, p5)
            p2.set(q2)
            
        wr2=StringVar()
        dr2=StringVar()
        p2=StringVar()

        Density1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til2 = Frame(Density1,width='250',height='1000',bg='#EDEDF5')
        bqit2 = Button(til2,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(Density1,ew4,ew5,p2))
        lw4 = Label(til2,text='mass',bg='#EDEDF5',fg='#080808',font=2)
        ew4 = Entry(til2,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr2)
        lw5 = Label(til2,text='volume',bg='#EDEDF5',fg='#080808',font=2)
        ew5 = Entry(til2,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr2)
        aa2a2 = Button(til2,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew4,ew5,p2))
        ba2 = Button(til2,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics2)
        la2 =Label(Density1,text="Density = ",bg='#f8f8ff',fg='#080808',font=20,)
        lla2 = Label(Density1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p2)
        popup_menu(ew4,d3np)
        popup_menu(ew5,d3np)
        #-------------------------------------------

        def functionssetphysics3():

            if wr3.get() == '' or dr3.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p5 =float(wr3.get())
            p6 =float(dr3.get())
            q3 =  force(p5, p6)
            p3.set(q3)
            
        wr3=StringVar()
        dr3=StringVar()
        p3=StringVar()


        Force1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til3 = Frame(Force1,width='250',height='1000',bg='#EDEDF5')
        bqit3 = Button(til3,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(Force1,ew6,ew7,p3))
        lw6 = Label(til3,text='mass',bg='#EDEDF5',fg='#080808',font=2)
        ew6 = Entry(til3,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr3)
        lw7 = Label(til3,text='acceleration',bg='#EDEDF5',fg='#080808',font=2)
        ew7 = Entry(til3,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr3)
        aa2a3 = Button(til3,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew6,ew7,p3))
        ba3 = Button(til3,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics3)
        la3 =Label(Force1,text="Force = ",bg='#f8f8ff',fg='#080808',font=20,)
        lla3 = Label(Force1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p3)
        popup_menu(ew6,d3np)
        popup_menu(ew7,d3np)
        #-------------------------------------------

        def functionssetphysics4():

            if wr4.get() == '' or dr4.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p7 =float(wr4.get())
            p8 =float(dr4.get())
            q4 =  work(p7, p8)
            
            p4.set(q4)
            
        wr4=StringVar()
        dr4=StringVar()
        p4=StringVar()

        Work1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til4 = Frame(Work1,width='250',height='1000',bg='#EDEDF5')
        bqit4 = Button(til4,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(Work1,ew8,ew9,p4))
        lw8 = Label(til4,text='Force',bg='#EDEDF5',fg='#080808',font=2)
        ew8 = Entry(til4,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr4)
        lw9 = Label(til4,text='distance',bg='#EDEDF5',fg='#080808',font=2)
        ew9 = Entry(til4,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr4)
        ww2sa = Button(til4,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew8,ew9,p4))
        ba4 = Button(til4,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics4)
        la4 =Label(Work1,text="Work = ",bg='#f8f8ff',fg='#080808',font=20)
        lla4 = Label(Work1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p4)
        popup_menu(ew8,d3np)
        popup_menu(ew9,d3np)
        #-------------------------------------------

        def functionssetphysics5():

            if wr5.get() == '' or dr5.get() == '' or fr2.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p9 =float(wr5.get())
            p10 =float(dr5.get())
            p11 =float(fr2.get())
            q5 =  workTheta(p9, p10 , p11)
            
            p5.set(q5)
            
        wr5=StringVar()
        dr5=StringVar()
        fr2=StringVar()
        p5=StringVar()

        WorkTheta1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til5 = Frame(WorkTheta1,width='250',height='1000',bg='#EDEDF5')
        bqit5 = Button(til5,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(WorkTheta1,ew10,ew11,ew12,p5))
        lw10 = Label(til5,text='Force',bg='#EDEDF5',fg='#080808',font=2)
        ew10 = Entry(til5,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr5)
        lw11 = Label(til5,text='distance',bg='#EDEDF5',fg='#080808',font=2)
        ew11 = Entry(til5,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr5)
        lw12 = Label(til5,text='theta',bg='#EDEDF5',fg='#080808',font=2)
        ew12 = Entry(til5,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr2)
        ww2sa2 = Button(til5,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew10,ew11,ew12,p5))
        ba5 = Button(til5,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics5)
        la5 =Label(WorkTheta1,text="Work = ",bg='#f8f8ff',fg='#080808',font=20,)
        lla5 = Label(WorkTheta1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p5)
        popup_menu(ew10,d3np)
        popup_menu(ew11,d3np)
        popup_menu(ew12,d3np)
        #-------------------------------------------

        def functionssetphysics6():

            if wr6.get() == '' or dr6.get() == '' or fr3.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p12 =float(wr6.get())
            p13 =float(dr6.get())
            p14 =float(fr3.get())
            q6 =  resultantOftwoForces(p12, p13 , p14)
            
            p6.set(q6)
            
        wr6=StringVar()
        dr6=StringVar()
        fr3=StringVar()
        p6=StringVar()

        def mm2():

            if wr6.get() == '' or dr6.get() == '' or fr3.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            force1 = int(wr6.get())
            force2 = int(dr6.get())
            theta = int(fr3.get())
            r = int(float(p6.get()))
            x = [0,force1]
            y = [0,force2]
            e = [0,r]
            theta = [0,theta]
            plt.plot(theta,x)
            plt.plot(theta,y)
            plt.plot(theta,e)
            
            plt.show()

        resultantOftwoForces1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til6 = Frame(resultantOftwoForces1,width='250',height='1000',bg='#EDEDF5')
        bqit6 = Button(til6,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(resultantOftwoForces1,ew13,ew14,ew15,p6))
        lw13 = Label(til6,text='force1',bg='#EDEDF5',fg='#080808',font=2)
        ew13 = Entry(til6,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr6)
        lw14 = Label(til6,text='force2',bg='#EDEDF5',fg='#080808',font=2)
        ew14 = Entry(til6,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr6)
        lw15 = Label(til6,text='theta',bg='#EDEDF5',fg='#080808',font=2)
        ew15 = Entry(til6,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr3)
        aa2a5 = Button(til6,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew13,ew14,ew15,p6))
        ba6 = Button(til6,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics6)
        aa2 = Button(til6,text='simulation',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=mm2)
        la6 =Label(resultantOftwoForces1,text="Result = ",bg='#f8f8ff',fg='#080808',font=20)
        lla6 = Label(resultantOftwoForces1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p6)
        popup_menu(ew13,d3np)
        popup_menu(ew14,d3np)
        popup_menu(ew15,d3np)
        #-------------------------------------------

        def functionssetphysics7():

            if wr7.get() == '' or dr7.get() == '' or fr4.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p15 =float(wr7.get())
            p16 =float(dr7.get())
            p17 =float(fr4.get())
            q7 =  directionOfTheResultant(p15, p16 , p17)
            
            p7.set(q7)
            
        wr7=StringVar()
        dr7=StringVar()
        fr4=StringVar()
        p7=StringVar()

        directionOfTheResultant1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til7 = Frame(directionOfTheResultant1,width='250',height='1000',bg='#EDEDF5')
        bqit7 = Button(til7,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(directionOfTheResultant1,ew16,ew17,ew18,p7))
        lw16 = Label(til7,text='force1',bg='#EDEDF5',fg='#080808',font=2)
        ew16 = Entry(til7,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr7)
        lw17 = Label(til7,text='force2',bg='#EDEDF5',fg='#080808',font=2)
        ew17 = Entry(til7,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr7)
        lw18 = Label(til7,text='theta',bg='#EDEDF5',fg='#080808',font=2)
        ew18 = Entry(til7,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr4)
        aa2a6 = Button(til7,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew16,ew17,ew18,p7))
        ba7 = Button(til7,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics7)
        la7 =Label(directionOfTheResultant1,text="direction = ",bg='#f8f8ff',fg='#080808',font=20)
        lla7 = Label(directionOfTheResultant1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p7)
        popup_menu(ew16,d3np)
        popup_menu(ew17,d3np)
        popup_menu(ew18,d3np)
        #-------------------------------------------

        def functionssetphysics8():

            if wr8.get() == '' or dr8.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p18 =float(wr8.get())
            p19 =float(dr8.get())
            q8 =  forceAnalysisInTwoOrthogonalDirections(p18, p19)
            
            p8.set(q8)
            
        wr8=StringVar()
        dr8=StringVar()
        p8=StringVar()

        forceAnalysisInTwoOrthogonalDirections1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til8 = Frame(forceAnalysisInTwoOrthogonalDirections1,width='250',height='1000',bg='#EDEDF5')
        bqit8 = Button(til8,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(forceAnalysisInTwoOrthogonalDirections1,ew19,ew20,p8))
        lw19 = Label(til8,text='force',bg='#EDEDF5',fg='#080808',font=2)
        ew19 = Entry(til8,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr8)
        lw20 = Label(til8,text='theta',bg='#EDEDF5',fg='#080808',font=2)
        ew20 = Entry(til8,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr8)
        aa2a7 = Button(til8,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew19,ew20,p8))
        ba8 = Button(til8,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics8)
        la8 =Label(forceAnalysisInTwoOrthogonalDirections1,text="Result = ",bg='#f8f8ff',fg='#080808',font=20)
        lla8 = Label(forceAnalysisInTwoOrthogonalDirections1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p8)
        popup_menu(ew19,d3np)
        popup_menu(ew20,d3np)
        #-------------------------------------------

        def functionssetphysics9():

            if wr9.get() == '' or dr9.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p20 =float(wr9.get())
            p21 =float(dr9.get())
            q9 =  directionOfTheResultantTwoForce(p20, p21)
            
            p9.set(q9)
            
        wr9=StringVar()
        dr9=StringVar()
        p9=StringVar()

        directionOfTheResultantTwoForce1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til9 = Frame(directionOfTheResultantTwoForce1,width='250',height='1000',bg='#EDEDF5')
        bqit9 = Button(til9,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(directionOfTheResultantTwoForce1,ew21,ew22,p9))
        lw21 = Label(til9,text='Rx',bg='#EDEDF5',fg='#080808',font=2)
        ew21 = Entry(til9,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr9)
        lw22 = Label(til9,text='Ry',bg='#EDEDF5',fg='#080808',font=2)
        ew22 = Entry(til9,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr9)
        aa2a8 = Button(til9,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew21,ew22,p9))
        ba9 = Button(til9,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics9)
        la9 =Label(directionOfTheResultantTwoForce1,text="Result = ",bg='#f8f8ff',fg='#080808',font=20)
        lla9 = Label(directionOfTheResultantTwoForce1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p9)
        popup_menu(ew21,d3np)
        popup_menu(ew22,d3np)
        #-------------------------------------------

        def functionssetphysics10():

            if wr10.get() == '' or dr10.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p22 =float(wr10.get())
            p23 =float(dr10.get())
            q10 =  torque(p22, p23)
            
            p10.set(q10)
            
        wr10=StringVar()
        dr10=StringVar()
        p10=StringVar()


        def mm3():

            if dx10.get() == '' or dx11.get() == '' or dx12.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            ll = float(dx10.get())
            ll2 = float(dx11.get())
            mm = float(dx12.get())
            G = 9.8  # acceleration due to gravity, in m/s^2
            L1 = ll # length of pendulum 1 in m
            L2 = ll2  # length of pendulum 2 in m
            L = L1 + L2  # maximal length of the combined pendulum
            M1 = mm  # mass of pendulum 1 in kg
            M2 = 1.0  # mass of pendulum 2 in kg
            t_stop = 60  # how many seconds to simulate
            history_len = 500  # how many trajectory points to display


            def derivs(t, state):
                dydx = np.zeros_like(state)

                dydx[0] = state[1]

                delta = state[2] - state[0]
                den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
                dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                            + M2 * G * sin(state[2]) * cos(delta)
                            + M2 * L2 * state[3] * state[3] * sin(delta)
                            - (M1+M2) * G * sin(state[0]))
                        / den1)

                dydx[2] = state[3]

                den2 = (L2/L1) * den1
                dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                            + (M1+M2) * G * sin(state[0]) * cos(delta)
                            - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                            - (M1+M2) * G * sin(state[2]))
                        / den2)

                return dydx

            # create a time array from 0..t_stop sampled at 0.02 second steps
            dt = 0.01
            t = np.arange(0, t_stop, dt)

            # th1 and th2 are the initial angles (degrees)
            # w10 and w20 are the initial angular velocities (degrees per second)
            th1 = 120.0
            w1 = 0.0
            th2 = -10.0
            w2 = 0.0

            # initial state
            state = np.radians([th1, w1, th2, w2])

            # integrate the ODE using Euler's method
            y = np.empty((len(t), 4))
            y[0] = state
            for i in range(1, len(t)):
                y[i] = y[i - 1] + derivs(t[i - 1], y[i - 1]) * dt

            # A more accurate estimate could be obtained e.g. using scipy:
        

            x1 = L1*sin(y[:, 0])
            y1 = -L1*cos(y[:, 0])

            x2 = L2*sin(y[:, 2]) + x1
            y2 = -L2*cos(y[:, 2]) + y1

            fig = plt.figure(figsize=(5, 4))
            ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(-L, 1.))
            ax.set_aspect('equal')
            ax.grid()

            line, = ax.plot([], [], 'o-', lw=2)
            trace, = ax.plot([], [], '.-', lw=1, ms=2)
            time_template = 'time = %.1fs'
            time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
            history_x, history_y = deque(maxlen=history_len), deque(maxlen=history_len)


            def animate(i):
                thisx = [0, x1[i], x2[i]]
                thisy = [0, y1[i], y2[i]]

                if i == 0:
                    history_x.clear()
                    history_y.clear()

                history_x.appendleft(thisx[2])
                history_y.appendleft(thisy[2])

                line.set_data(thisx, thisy)
                trace.set_data(history_x, history_y)
                time_text.set_text(time_template % (i*dt))
                return line, trace, time_text


            ani = animation.FuncAnimation(
                fig, animate, len(y), interval=dt*1000, blit=True)
            plt.show()

        dx10=StringVar()
        dx11=StringVar()
        dx12=StringVar()

        torque1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til10 = Frame(torque1,width='250',height='1000',bg='#EDEDF5')
        bqit10 = Button(til10,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide5(torque1,ew23,ew24,exx24,exx26,exx25,p10))
        lw23 = Label(til10,text='force',bg='#EDEDF5',fg='#080808',font=2)
        ew23 = Entry(til10,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr10)
        lw24 = Label(til10,text='height',bg='#EDEDF5',fg='#080808',font=2)
        ew24 = Entry(til10,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr10)
        aa2a9 = Button(til10,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew23,ew24,p10))
        aa2a292 = Button(til10,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(exx24,exx26,exx25,p10))
        ba10 = Button(til10,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics10)
        lxx24 = Label(til10,text='length of pendulum 1',bg='#EDEDF5',fg='#080808',font=2)
        exx24 = Entry(til10,bg='#f8f8ff',fg='#080808',font=2,textvariable=dx10)
        lxx25 = Label(til10,text='length of pendulum 2',bg='#EDEDF5',fg='#080808',font=2)
        exx25 = Entry(til10,bg='#f8f8ff',fg='#080808',font=2,textvariable=dx11)
        lxx26 = Label(til10,text='mass of pendulum',bg='#EDEDF5',fg='#080808',font=2)
        exx26 = Entry(til10,bg='#f8f8ff',fg='#080808',font=2,textvariable=dx12)
        aa3 = Button(til10,text='simulation',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=mm3)
        la10 =Label(torque1,text="torque = ",bg='#f8f8ff',fg='#080808',font=20)
        lla10 = Label(torque1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p10)
        popup_menu(ew23,d3np)
        popup_menu(ew24,d3np)
        popup_menu(exx24,d3np)
        popup_menu(exx25,d3np)
        popup_menu(exx26,d3np)
        #-------------------------------------------

        def functionssetphysics11():

            if wr11.get() == '' or dr11.get() == '' or fr5.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p24 =float(wr11.get())
            p25 =float(dr11.get())
            p26 =float(fr5.get())
            q11 =  torqueWithTheta(p24, p25,p26)
            
            p11.set(q11)
            
        wr11=StringVar()
        dr11=StringVar()
        fr5=StringVar()
        p11=StringVar()

        torqueWithTheta1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til11 = Frame(torqueWithTheta1,width='250',height='1000',bg='#EDEDF5')
        bqit11 = Button(til11,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(torqueWithTheta1,ew25,ew26,ew27,p11))
        lw25 = Label(til11,text='force',bg='#EDEDF5',fg='#080808',font=2)
        ew25 = Entry(til11,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr11)
        lw26 = Label(til11,text='height',bg='#EDEDF5',fg='#080808',font=2)
        ew26 = Entry(til11,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr11)
        lw27 = Label(til11,text='theta',bg='#EDEDF5',fg='#080808',font=2)
        ew27 = Entry(til11,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr5)
        aa2a10 = Button(til11,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew25,ew26,ew27,p11))
        ba11 = Button(til11,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics11)
        la11 =Label(torqueWithTheta1,text="torque = ",bg='#f8f8ff',fg='#080808',font=20)
        lla11 = Label(torqueWithTheta1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p11)
        popup_menu(ew25,d3np)
        popup_menu(ew26,d3np)
        popup_menu(ew27,d3np)
        #-------------------------------------------

        def functionssetphysics12():

            if wr12.get() == '' or dr12.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p27 =float(wr12.get())
            p28 =float(dr12.get())
            q12 =  frictionforce(p27, p28)
            
            p12.set(q12)
            
        wr12=StringVar()
        dr12=StringVar()
        p12=StringVar()

        friction1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til12 = Frame(friction1,width='250',height='1000',bg='#EDEDF5')
        bqit12 = Button(til12,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(friction1,ew28,ew29,p12))
        lw28 = Label(til12,text='frictionCoefficient',bg='#EDEDF5',fg='#080808',font=2)
        ew28 = Entry(til12,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr12)
        lw29 = Label(til12,text='fn',bg='#EDEDF5',fg='#080808',font=2)
        ew29 = Entry(til12,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr12)
        aa2a11 = Button(til12,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew28,ew29,p12))
        ba12 = Button(til12,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics12)
        la12 =Label(friction1,text="force = ",bg='#f8f8ff',fg='#080808',font=20)
        lla12 = Label(friction1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p12)
        popup_menu(ew28,d3np)
        popup_menu(ew29,d3np)
        #-------------------------------------------

        def functionssetphysics13():

            if wr13.get() == '' or dr13.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p29 =float(wr13.get())
            p30 =float(dr13.get())
            q13 =  frictionCoefficient(p29,p30)
            
            p13.set(q13)
            
        wr13=StringVar()
        dr13=StringVar()
        p13=StringVar()

        frictionCoefficient1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til13 = Frame(frictionCoefficient1,width='250',height='1000',bg='#EDEDF5')
        bqit13 = Button(til13,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(frictionCoefficient1,ew30,ew31,p13))
        lw30 = Label(til13,text='Ff',bg='#EDEDF5',fg='#080808',font=2)
        ew30 = Entry(til13,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr13)
        lw31 = Label(til13,text='Fn',bg='#EDEDF5',fg='#080808',font=2)
        ew31 = Entry(til13,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr13)
        aa2a12 = Button(til13,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew30,ew31,p13))
        ba13 = Button(til13,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics13)
        la13 =Label(frictionCoefficient1,text="frictionCoefficient = ",bg='#f8f8ff',fg='#080808',font=20)
        lla13 = Label(frictionCoefficient1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p13)
        popup_menu(ew30,d3np)
        popup_menu(ew31,d3np)
        #-------------------------------------------

        def functionssetphysics14():

            if wr14.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p31 =float(wr14.get())
            q14 =  gravitationalForce(p31)
            
            p14.set(q14)
            
        wr14=StringVar()
        p14=StringVar()

        gravitationalForce1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til14 = Frame(gravitationalForce1,width='250',height='1000',bg='#EDEDF5')
        bqit14 = Button(til14,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(gravitationalForce1,ew32,p14))
        lw32 = Label(til14,text='Mass',bg='#EDEDF5',fg='#080808',font=2)
        ew32 = Entry(til14,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr14)
        la14 =Label(gravitationalForce1,text="force = ",bg='#f8f8ff',fg='#080808',font=20)
        aa2a13 = Button(til14,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew32,p14))
        ba14 = Button(til14,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics14)
        lla14 = Label(gravitationalForce1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p14)
        popup_menu(ew32,d3np)
        #-------------------------------------------

        def functionssetphysics15():

            if wr15.get() == '' or dr15.get() == '' or fr6.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p32 =float(wr15.get())
            p33 =float(dr15.get())
            p34 =float(fr6.get())
            q15 =  generalLawOfAttraction(p32, p33,p34)
            
            p15.set(q15)
            
        wr15=StringVar()
        dr15=StringVar()
        fr6=StringVar()
        p15=StringVar()

        generalLawOfAttraction1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til15 = Frame(generalLawOfAttraction1,width='250',height='1000',bg='#EDEDF5')
        bqit15 = Button(til15,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(generalLawOfAttraction1,ew33,ew34,ew35,p15))
        lw33 = Label(til15,text='Mass1',bg='#EDEDF5',fg='#080808',font=2)
        ew33 = Entry(til15,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr15)
        lw34 = Label(til15,text='Mass2',bg='#EDEDF5',fg='#080808',font=2)
        ew34 = Entry(til15,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr15)
        lw35 = Label(til15,text='height',bg='#EDEDF5',fg='#080808',font=2)
        ew35 = Entry(til15,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr6)
        aa2a14 = Button(til15,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew33,ew34,ew35,p15))
        ba15 = Button(til15,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics15)
        la15 =Label(generalLawOfAttraction1,text="force = ",bg='#f8f8ff',fg='#080808',font=20)
        lla15 = Label(generalLawOfAttraction1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p15)
        popup_menu(ew33,d3np)
        popup_menu(ew34,d3np)
        popup_menu(ew35,d3np)
        #-------------------------------------------

        def functionssetphysics16():
            
            if wr16.get() == '' or dr16.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p35 =float(wr16.get())
            p36 =float(dr16.get())
            q16 =  power(p35, p36)
            
            p16.set(q16)
            
        wr16=StringVar()
        dr16=StringVar()
        p16=StringVar()

        Power1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til16 = Frame(Power1,width='250',height='1000',bg='#EDEDF5')
        bqit16 = Button(til16,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(Power1,ew36,ew37,p16))
        lw36 = Label(til16,text='work',bg='#EDEDF5',fg='#080808',font=2)
        ew36 = Entry(til16,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr16)
        lw37 = Label(til16,text='time',bg='#EDEDF5',fg='#080808',font=2)
        ew37 = Entry(til16,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr16)
        aa2a15 = Button(til16,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew36,ew37,p16))
        ba16 = Button(til16,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics16)
        la16 =Label(Power1,text="Power = ",bg='#f8f8ff',fg='#080808',font=20)
        lla16 = Label(Power1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p16)
        popup_menu(ew36,d3np)
        popup_menu(ew37,d3np)
        #-------------------------------------------

        def functionssetphysics17():
            
            if wr17.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p37 =float(wr17.get())
            q17 =  conversionFromHorsepowerToJoules(p37)
            
            p17.set(q17)
            
        wr17=StringVar()
        p17=StringVar()

        conversionFromHorsepowerToJoules1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til17 = Frame(conversionFromHorsepowerToJoules1,width='250',height='1000',bg='#EDEDF5')
        bqit17 = Button(til17,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(conversionFromHorsepowerToJoules1,ew38,p17))
        lw38 = Label(til17,text='hp',bg='#EDEDF5',fg='#080808',font=2)
        ew38 = Entry(til17,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr17)
        la17 =Label(conversionFromHorsepowerToJoules1,text="w = ",bg='#f8f8ff',fg='#080808',font=20)
        aa2a16 = Button(til17,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew38,p17))
        ba17 = Button(til17,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics17)
        lla17 = Label(conversionFromHorsepowerToJoules1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p17)
        popup_menu(ew38,d3np)
        #-------------------------------------------

        def functionssetphysics18():
            
            if wr18.get() == '' or dr18.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p38 =float(wr18.get())
            p39 =float(dr18.get())
            q18 =  graphicAbility(p38, p39)
            
            p18.set(q18)
            
        wr18=StringVar()
        dr18=StringVar()
        p18=StringVar()

        graphicAbility1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til18 = Frame(graphicAbility1,width='250',height='1000',bg='#EDEDF5')
        bqit18 = Button(til18,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(graphicAbility1,ew39,ew40,p18))
        lw39 = Label(til18,text='BP',bg='#EDEDF5',fg='#080808',font=2)
        ew39 = Entry(til18,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr18)
        lw40 = Label(til18,text='FP',bg='#EDEDF5',fg='#080808',font=2)
        ew40 = Entry(til18,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr18)
        aa2a17 = Button(til18,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew39,ew40,p18))
        ba18 = Button(til18,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics18)
        la18 =Label(graphicAbility1,text="IP = ",bg='#f8f8ff',fg='#080808',font=20)
        lla18 = Label(graphicAbility1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p18)
        popup_menu(ew39,d3np)
        popup_menu(ew40,d3np)
        #------------------------------------------------------------------------------------
        #------------------------------dynamicsa-----------------

        def functionssetphysics19():
            
            if wr19.get() == '' or dr19.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p40 =float(wr19.get())
            p41 =float(dr19.get())
            q19 =  velocity(p40, p41)
            
            p19.set(q19)
            
        wr19=StringVar()
        dr19=StringVar()
        p19=StringVar()

        velocity1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til19 = Frame(velocity1,width='250',height='1000',bg='#EDEDF5')
        bqit19 = Button(til19,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(velocity1,ew41,ew42,p19))
        lw41 = Label(til19,text='distance',bg='#EDEDF5',fg='#080808',font=2)
        ew41 = Entry(til19,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr19)
        lw42 = Label(til19,text='time',bg='#EDEDF5',fg='#080808',font=2)
        ew42 = Entry(til19,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr19)
        aa2a18 = Button(til19,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew41,ew42,p19))
        ba19 = Button(til19,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics19)
        la19 =Label(velocity1,text="velocity = ",bg='#f8f8ff',fg='#080808',font=20)
        lla19 = Label(velocity1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p19)
        popup_menu(ew41,d3np)
        popup_menu(ew42,d3np)
        #-------------------------------------------

        def functionssetphysics20():
            
            if wr20.get() == '' or dr20.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p42 =float(wr20.get())
            p43 =float(dr20.get())
            q20 =  time(p42, p43)
            
            p20.set(q20)
            
        wr20=StringVar()
        dr20=StringVar()
        p20=StringVar()

        time1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til20 = Frame(time1,width='250',height='1000',bg='#EDEDF5')
        bqit20 = Button(til20,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(time1,ew43,ew44,p20))
        lw43 = Label(til20,text='distance',bg='#EDEDF5',fg='#080808',font=2)
        ew43 = Entry(til20,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr20)
        lw44 = Label(til20,text='velocity',bg='#EDEDF5',fg='#080808',font=2)
        ew44 = Entry(til20,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr20)
        aa2a19 = Button(til20,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew43,ew44,p20))
        ba20 = Button(til20,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics20)
        la20 =Label(time1,text="time = ",bg='#f8f8ff',fg='#080808',font=20)
        lla20 = Label(time1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p20)
        popup_menu(ew43,d3np)
        popup_menu(ew44,d3np)
        #-------------------------------------------

        def functionssetphysics21():
            
            if wr21.get() == '' or dr21.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p44 =float(wr21.get())
            p45 =float(dr21.get())
            q21 =  distance(p44, p45)
            
            p21.set(q21)
            
        wr21=StringVar()
        dr21=StringVar()
        p21=StringVar()

        distance1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til21 = Frame(distance1,width='250',height='1000',bg='#EDEDF5')
        bqit21 = Button(til21,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(distance1,ew45,ew46,p21))
        lw45 = Label(til21,text='velocity',bg='#EDEDF5',fg='#080808',font=2)
        ew45 = Entry(til21,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr21)
        lw46 = Label(til21,text='time',bg='#EDEDF5',fg='#080808',font=2)
        ew46 = Entry(til21,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr21)
        aa2a20 = Button(til21,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew45,ew46,p21))
        ba21 = Button(til21,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics21)
        la21 =Label(distance1,text="distance = ",bg='#f8f8ff',fg='#080808',font=20)
        lla21 = Label(distance1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p21)
        popup_menu(ew45,d3np)
        popup_menu(ew46,d3np)
        #-------------------------------------------

        def functionssetphysics22():
            
            if wr22.get() == '' or dr22.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p46 =float(wr22.get())
            p47 =float(dr22.get())
            q22 =  acceleration(p46, p47)
            
            p22.set(q22)
            
        wr22=StringVar()
        dr22=StringVar()
        p22=StringVar()

        acceleration1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til22 = Frame(acceleration1,width='250',height='1000',bg='#EDEDF5')
        bqit22 = Button(til22,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(acceleration1,ew47,ew48,p22))
        lw47 = Label(til22,text='velocity',bg='#EDEDF5',fg='#080808',font=2)
        ew47 = Entry(til22,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr22)
        lw48 = Label(til22,text='time',bg='#EDEDF5',fg='#080808',font=2)
        ew48 = Entry(til22,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr22)
        aa2a21 = Button(til22,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew47,ew48,p22))
        ba22 = Button(til22,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics22)
        la22 =Label(acceleration1,text="acceleration = ",bg='#f8f8ff',fg='#080808',font=20)
        lla22 = Label(acceleration1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p22)
        popup_menu(ew47,d3np)
        popup_menu(ew48,d3np)
        #-------------------------------------------

        def functionssetphysics23():
            
            if wr23.get() == '' or dr23.get() == '' or fr7.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p48 =float(wr23.get())
            p49 =float(dr23.get())
            p50 =float(fr7.get())
            q23 =  linearDistance(p48, p49,p50)
            
            p23.set(q23)
            
        wr23=StringVar()
        dr23=StringVar()
        fr7=StringVar()
        p23=StringVar()

        linearDistance1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til23 = Frame(linearDistance1,width='250',height='1000',bg='#EDEDF5')
        bqit23 = Button(til23,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(linearDistance1,ew49,ew50,ew51,p23))
        lw49 = Label(til23,text='velocity',bg='#EDEDF5',fg='#080808',font=2)
        ew49 = Entry(til23,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr23)
        lw50 = Label(til23,text='time',bg='#EDEDF5',fg='#080808',font=2)
        ew50 = Entry(til23,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr23)
        lw51 = Label(til23,text='acceleration',bg='#EDEDF5',fg='#080808',font=2)
        ew51 = Entry(til23,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr7)
        aa2a22 = Button(til23,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew49,ew50,ew51,p23))
        ba23 = Button(til23,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics23)
        la23 =Label(linearDistance1,text="linearDistance = ",bg='#f8f8ff',fg='#080808',font=20)
        lla23 = Label(linearDistance1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p23)
        popup_menu(ew49,d3np)
        popup_menu(ew50,d3np)
        popup_menu(ew51,d3np)
        #-------------------------------------------

        def functionssetphysics24():
            
            if wr24.get() == '' or dr24.get() == '' or fr8.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p51 =float(wr24.get())
            p52 =float(dr24.get())
            p53 =float(fr8.get())
            q24 =  linearTime(p51, p52,p53)
            
            p24.set(q24)
            
        wr24=StringVar()
        dr24=StringVar()
        fr8=StringVar()
        p24=StringVar()

        linearTime1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til24 = Frame(linearTime1,width='250',height='1000',bg='#EDEDF5')
        bqit24 = Button(til24,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(linearTime1,ew52,ew53,ew54,p24))
        lw52 = Label(til24,text='velocity',bg='#EDEDF5',fg='#080808',font=2)
        ew52 = Entry(til24,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr24)
        lw53 = Label(til24,text='initialvelocity',bg='#EDEDF5',fg='#080808',font=2)
        ew53 = Entry(til24,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr24)
        lw54 = Label(til24,text='acceleration',bg='#EDEDF5',fg='#080808',font=2)
        ew54 = Entry(til24,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr8)
        aa2a23 = Button(til24,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew52,ew53,ew54,p24))
        ba24 = Button(til24,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics24)
        la24 =Label(linearTime1,text="Time = ",bg='#f8f8ff',fg='#080808',font=20)
        lla24 = Label(linearTime1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p24)
        popup_menu(ew52,d3np)
        popup_menu(ew53,d3np)
        popup_menu(ew54,d3np)
        #-------------------------------------------

        def functionssetphysics25():
            
            if wr25.get() == '' or dr25.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p54 =float(wr25.get())
            p55 =float(dr25.get())
            q25 =  circularTime(p54, p55)
            
            p25.set(q25)
            
        wr25=StringVar()
        dr25=StringVar()
        p25=StringVar()

        circularTime1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til25 = Frame(circularTime1,width='250',height='1000',bg='#EDEDF5')
        bqit25 = Button(til25,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(circularTime1,ew55,ew56,p25))
        lw55 = Label(til25,text='theta',bg='#EDEDF5',fg='#080808',font=2)
        ew55 = Entry(til25,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr25)
        lw56 = Label(til25,text='Omega',bg='#EDEDF5',fg='#080808',font=2)
        ew56 = Entry(til25,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr25)
        aa2a24 = Button(til25,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew55,ew56,p25))
        ba25 = Button(til25,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics25)
        la25 =Label(circularTime1,text="Time = ",bg='#f8f8ff',fg='#080808',font=20)
        lla25 = Label(circularTime1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p25)
        popup_menu(ew55,d3np)
        popup_menu(ew56,d3np)
        #-------------------------------------------

        def functionssetphysics26():
            
            if wr26.get() == '' or dr26.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p56 =float(wr26.get())
            p57 =float(dr26.get())
            q26 =  periodicDisplacement(p56, p57)
            
            p26.set(q26)
            
        wr26=StringVar()
        dr26=StringVar()
        p26=StringVar()

        periodicDisplacement1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til26 = Frame(periodicDisplacement1,width='250',height='1000',bg='#EDEDF5')
        bqit26 = Button(til26,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(periodicDisplacement1,ew57,ew58,p26))
        lw57 = Label(til26,text='Omega',bg='#EDEDF5',fg='#080808',font=2)
        ew57 = Entry(til26,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr26)
        lw58 = Label(til26,text='time',bg='#EDEDF5',fg='#080808',font=2)
        ew58 = Entry(til26,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr26)
        aa2a25 = Button(til26,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew57,ew58,p26))
        ba26 = Button(til26,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics26)
        la26 =Label(periodicDisplacement1,text="theta = ",bg='#f8f8ff',fg='#080808',font=20)
        lla26 = Label(periodicDisplacement1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p26)
        popup_menu(ew57,d3np)
        popup_menu(ew58,d3np)
        #-------------------------------------------

        def functionssetphysics27():
            
            if wr27.get() == '' or dr27.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p58 =float(wr27.get())
            p59 =float(dr27.get())
            q27 =  omega(p58, p59)
            
            p27.set(q27)
            
        wr27=StringVar()
        dr27=StringVar()
        p27=StringVar()

        omega1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til27 = Frame(omega1,width='250',height='1000',bg='#EDEDF5')
        bqit27 = Button(til27,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(omega1,ew59,ew60,p27))
        lw59 = Label(til27,text='theta',bg='#EDEDF5',fg='#080808',font=2)
        ew59 = Entry(til27,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr27)
        lw60 = Label(til27,text='time',bg='#EDEDF5',fg='#080808',font=2)
        ew60 = Entry(til27,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr27)
        aa2a26 = Button(til27,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew59,ew60,p27))
        ba27 = Button(til27,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics27)
        la27 =Label(omega1,text="omega = ",bg='#f8f8ff',fg='#080808',font=20)
        lla27 = Label(omega1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p27)
        popup_menu(ew59,d3np)
        popup_menu(ew60,d3np)
        #-------------------------------------------

        def functionssetphysics28():
            
            if wr28.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p60 =float(wr28.get())
            q28 =  frequency(p60)
            
            p28.set(q28)
            
        wr28=StringVar()
        p28=StringVar()


        def mm4():

            if p28.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            wwq = float(p28.get())
            x = np.linspace(0,wwq * np.pi, 100)
            fig, ax = plt.subplots()
            (ln,) = ax.plot(x, np.sin(x), animated=True)
            plt.show(block=False)
            plt.pause(0.1)
            bg = fig.canvas.copy_from_bbox(fig.bbox)
            ax.draw_artist(ln)
            fig.canvas.blit(fig.bbox)
            for j in range(100000):  
                fig.canvas.restore_region(bg)   
                ln.set_ydata(np.sin(x + (j / 100) * np.pi))     
                ax.draw_artist(ln)        
                fig.canvas.blit(fig.bbox)
                fig.canvas.flush_events()



        frequency1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til28 = Frame(frequency1,width='250',height='1000',bg='#EDEDF5')
        bqit28 = Button(til28,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(frequency1,ew61,p28))
        lw61 = Label(til28,text='Omega',bg='#EDEDF5',fg='#080808',font=2)
        ew61 = Entry(til28,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr28)
        aa4 = Button(til28,text='simulation',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=mm4)
        aa2a27 = Button(til28,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew61,p28))
        ba28 = Button(til28,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics28)
        la28 =Label(frequency1,text="omega = ",bg='#f8f8ff',fg='#080808',font=20)
        lla28 = Label(frequency1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p28)
        popup_menu(ew61,d3np)
        #-------------------------------------------

        def functionssetphysics29():
            
            if wr29.get() == '' or dr29.get() == '' or fr9.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p61 =float(wr29.get())
            p62 =float(dr29.get())
            p63 =float(fr9.get())
            q29 =  angularVelocity(p61, p62,p63)
            
            p29.set(q29)
            
        wr29=StringVar()
        dr29=StringVar()
        fr9=StringVar()
        p29=StringVar()

        angularVelocity1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til29 = Frame(angularVelocity1,width='250',height='1000',bg='#EDEDF5')
        bqit29 = Button(til29,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(angularVelocity1,ew62,ew63,ew64,p29))
        lw62 = Label(til29,text='theta',bg='#EDEDF5',fg='#080808',font=2)
        ew62 = Entry(til29,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr29)
        lw63 = Label(til29,text='time',bg='#EDEDF5',fg='#080808',font=2)
        ew63 = Entry(til29,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr29)
        lw64 = Label(til29,text='frequency',bg='#EDEDF5',fg='#080808',font=2)
        ew64 = Entry(til29,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr9)
        aa2a28 = Button(til29,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew62,ew63,ew64,p29))
        ba29 = Button(til29,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics29)
        la29 =Label(angularVelocity1,text="angularVelocity = ",bg='#f8f8ff',fg='#080808',font=20)
        lla29 = Label(angularVelocity1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p29)
        popup_menu(ew62,d3np)
        popup_menu(ew63,d3np)
        popup_menu(ew64,d3np)
        #-------------------------------------------

        def functionssetphysics30():
            
            if wr30.get() == '' or dr30.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p64 =float(wr30.get())
            p65 =float(dr30.get())
            q30 =  linearAcceleration(p64, p65)
            
            p30.set(q30)
            
        wr30=StringVar()
        dr30=StringVar()
        p30=StringVar()

        linearAcceleration1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til30 = Frame(linearAcceleration1,width='250',height='1000',bg='#EDEDF5')
        bqit30 = Button(til30,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(linearAcceleration1,ew65,ew66,p30))
        lw65 = Label(til30,text='Omega',bg='#EDEDF5',fg='#080808',font=2)
        ew65 = Entry(til30,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr30)
        lw66 = Label(til30,text='time',bg='#EDEDF5',fg='#080808',font=2)
        ew66 = Entry(til30,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr30)
        aa2a29 = Button(til30,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew65,ew66,p30))
        ba30 = Button(til30,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics30)
        la30 =Label(linearAcceleration1,text="linearAcceleration = ",bg='#f8f8ff',fg='#080808',font=20)
        lla30 = Label(linearAcceleration1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p30)
        popup_menu(ew65,d3np)
        popup_menu(ew66,d3np)
        #-------------------------------------------

        def functionssetphysics31():
            
            if wr31.get() == '' or dr31.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p66 =float(wr31.get())
            p67 =float(dr31.get())
            q31 =  tangentialVelocity(p66, p67)
            
            p31.set(q31)
            
        wr31=StringVar()
        dr31=StringVar()
        p31=StringVar()

        tangentialVelocity1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til31 = Frame(tangentialVelocity1,width='250',height='1000',bg='#EDEDF5')
        bqit31 = Button(til31,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(tangentialVelocity1,ew67,ew68,p31))
        lw67 = Label(til31,text='Omega',bg='#EDEDF5',fg='#080808',font=2)
        ew67 = Entry(til31,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr31)
        lw68 = Label(til31,text='height',bg='#EDEDF5',fg='#080808',font=2)
        ew68 = Entry(til31,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr31)
        aa2a30 = Button(til31,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew67,ew68,p31))
        ba31 = Button(til31,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics31)
        la31 =Label(tangentialVelocity1,text="tangentialVelocity = ",bg='#f8f8ff',fg='#080808',font=20)
        lla31 = Label(tangentialVelocity1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p31)
        popup_menu(ew67,d3np)
        popup_menu(ew68,d3np)
        #-------------------------------------------

        def functionssetphysics32():
            
            if wr32.get() == '' or dr32.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p68 =float(wr32.get())
            p69 =float(dr32.get())
            q32 =  kineticEnergy(p68, p69)
            
            p32.set(q32)
            
        wr32=StringVar()
        dr32=StringVar()
        p32=StringVar()


        kineticEnergy1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til32 = Frame(kineticEnergy1,width='250',height='1000',bg='#EDEDF5')
        bqit32 = Button(til32,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(kineticEnergy1,ew69,ew70,p32))
        lw69 = Label(til32,text='Mass',bg='#EDEDF5',fg='#080808',font=2)
        ew69 = Entry(til32,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr32)
        lw70 = Label(til32,text='velocity',bg='#EDEDF5',fg='#080808',font=2)
        ew70 = Entry(til32,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr32)
        aa2a31 = Button(til32,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew69,ew70,p32))
        ba32 = Button(til32,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics32)
        la32 =Label(kineticEnergy1,text="KE = ",bg='#f8f8ff',fg='#080808',font=20)
        lla32 = Label(kineticEnergy1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p32)
        popup_menu(ew69,d3np)
        popup_menu(ew70,d3np)
        #-------------------------------------------

        def functionssetphysics33():
            
            if wr33.get() == '' or dr33.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p70 =float(wr33.get())
            p71 =float(dr33.get())
            q33 =  energySituation(p70, p71)
            
            p33.set(q33)
            
        wr33=StringVar()
        dr33=StringVar()
        p33=StringVar()


        energySituation1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til33 = Frame(energySituation1,width='250',height='1000',bg='#EDEDF5')
        bqit33 = Button(til33,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(energySituation1,ew71,ew72,p33))
        lw71 = Label(til33,text='work',bg='#EDEDF5',fg='#080808',font=2)
        ew71 = Entry(til33,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr33)
        lw72 = Label(til33,text='height',bg='#EDEDF5',fg='#080808',font=2)
        ew72 = Entry(til33,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr33)
        aa2a32 = Button(til33,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew71,ew72,p33))
        ba33 = Button(til33,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics33)
        la33 =Label(energySituation1,text="PE = ",bg='#f8f8ff',fg='#080808',font=20)
        lla33 = Label(energySituation1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p33)
        popup_menu(ew71,d3np)
        popup_menu(ew72,d3np)
        #-------------------------------------------

        def functionssetphysics34():
            
            if wr34.get() == '' or dr34.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p72 =float(wr34.get())
            p73 =float(dr34.get())
            q34 =  hookeIsLaw(p72, p73)
            
            p34.set(q34)
            
        wr34=StringVar()
        dr34=StringVar()
        p34=StringVar()

        hookeIsLaw1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til34 = Frame(hookeIsLaw1,width='250',height='1000',bg='#EDEDF5')
        bqit34 = Button(til34,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(hookeIsLaw1,ew73,ew74,p34))
        lw73 = Label(til34,text='k',bg='#EDEDF5',fg='#080808',font=2)
        ew73 = Entry(til34,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr34)
        lw74 = Label(til34,text='x',bg='#EDEDF5',fg='#080808',font=2)
        ew74 = Entry(til34,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr34)
        aa2a33 = Button(til34,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew73,ew74,p34))
        ba34 = Button(til34,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics34)
        la34 =Label(hookeIsLaw1,text="F = ",bg='#f8f8ff',fg='#080808',font=20)
        lla34 = Label(hookeIsLaw1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p34)
        popup_menu(ew73,d3np)
        popup_menu(ew74,d3np)
        #-------------------------------------------

        def functionssetphysics35():
            
            if wr35.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p74 =float(wr35.get())
            q35 =  periodicTime(p74)
            
            p35.set(q35)
            
        wr35=StringVar()
        p35=StringVar()

        periodicTime1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til35 = Frame(periodicTime1,width='250',height='1000',bg='#EDEDF5')
        bqit35 = Button(til35,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(periodicTime1,ew75,p35))
        lw75 = Label(til35,text='Omega',bg='#EDEDF5',fg='#080808',font=2)
        ew75 = Entry(til35,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr35)
        aa2a34 = Button(til35,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew75,p35))
        ba35 = Button(til35,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics35)
        la35 =Label(periodicTime1,text="periodicTime = ",bg='#f8f8ff',fg='#080808',font=20)
        lla35 = Label(periodicTime1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p35)
        popup_menu(ew75,d3np)
        #==================================================================
        #------------------------------statica-----------------
        def s1():
            d3np.add(volume1, text='volume')
            til.place(x=1,y=1)
            bqit.place(x=1,y=1)
            lw.place(x=95,y=40)
            ew.place(x=30,y=80)
            lw2.place(x=95,y=120)
            ew2.place(x=30,y=160)
            lw3.place(x=95,y=200)
            ew3.place(x=30,y=240)
            ba.place(x=30,y=280,width='90')
            aa.place(x=125,y=280,width='90')
            aa2a.place(x=30,y=315,width='185')
            lla.place(x=380,y=20)
            la.place(x=300,y=20)
        def s2():
            d3np.add(Density1, text='Density')
            til2.place(x=1,y=1)
            bqit2.place(x=1,y=1)
            lw4.place(x=95,y=40)
            ew4.place(x=30,y=80)
            lw5.place(x=95,y=120)
            ew5.place(x=30,y=160)
            ba2.place(x=30,y=280,width='90')
            aa2a2.place(x=130,y=280,width='90')
            lla2.place(x=380,y=20)
            la2.place(x=300,y=20)
        def s3():
            d3np.add(Force1, text='Force')
            til3.place(x=1,y=1)
            bqit3.place(x=1,y=1)
            lw6.place(x=95,y=40)
            ew6.place(x=30,y=80)
            lw7.place(x=75,y=120)
            ew7.place(x=30,y=160)
            ba3.place(x=30,y=280,width='90')
            aa2a3.place(x=130,y=280,width='90')
            lla3.place(x=380,y=20)
            la3.place(x=300,y=20)
        def s4():
            d3np.add(Work1, text='Work')
            til4.place(x=1,y=1)
            bqit4.place(x=1,y=1)
            lw8.place(x=95,y=40)
            ew8.place(x=30,y=80)
            lw9.place(x=90,y=120)
            ew9.place(x=30,y=160)
            ba4.place(x=30,y=280,width='90')
            ww2sa.place(x=130,y=280,width='90')
            lla4.place(x=380,y=20)
            la4.place(x=300,y=20)
        def s5():
            d3np.add(WorkTheta1, text='WorkTheta')
            til5.place(x=1,y=1)
            bqit5.place(x=1,y=1)
            lw10.place(x=95,y=40)
            ew10.place(x=30,y=80)
            lw11.place(x=90,y=120)
            ew11.place(x=30,y=160)
            lw12.place(x=100,y=200)
            ew12.place(x=30,y=240)
            ba5.place(x=30,y=280,width='90')
            ww2sa2.place(x=130,y=280,width='90')
            lla5.place(x=380,y=20)
            la5.place(x=300,y=20)
        def s6():
            d3np.add(resultantOftwoForces1, text='The resultant of two forces between them is an angle')
            til6.place(x=1,y=1)
            bqit6.place(x=1,y=1)
            lw13.place(x=95,y=40)
            ew13.place(x=30,y=80)
            lw14.place(x=95,y=120)
            ew14.place(x=30,y=160)
            lw15.place(x=95,y=200)
            ew15.place(x=30,y=240)
            ba6.place(x=30,y=280,width='90')
            aa2.place(x=125,y=280,width='90')
            aa2a5.place(x=30,y=315,width='185')
            lla6.place(x=380,y=20)
            la6.place(x=300,y=20)
        def s7():
            d3np.add(directionOfTheResultant1, text='The direction of the resultant force between two forces is an angle') 
            til7.place(x=1,y=1)
            bqit7.place(x=1,y=1)
            lw16.place(x=95,y=40)
            ew16.place(x=30,y=80)
            lw17.place(x=95,y=120)
            ew17.place(x=30,y=160)
            lw18.place(x=95,y=200)
            ew18.place(x=30,y=240)
            ba7.place(x=30,y=280,width='90')
            aa2a6.place(x=130,y=280,width='90')
            lla7.place(x=380,y=20)
            la7.place(x=300,y=20)
        def s8():
            d3np.add(forceAnalysisInTwoOrthogonalDirections1, text='Two perpendicular force analysis')  
            til8.place(x=1,y=1)
            bqit8.place(x=1,y=1)
            lw19.place(x=95,y=40)
            ew19.place(x=30,y=80)
            lw20.place(x=95,y=120)
            ew20.place(x=30,y=160)
            ba8.place(x=30,y=280,width='90')
            aa2a7.place(x=130,y=280,width='90')
            lla8.place(x=380,y=20)
            la8.place(x=300,y=20)  
        def s9():
            d3np.add(directionOfTheResultantTwoForce1, text='Direction of two forces perpendicular analysis')   
            til9.place(x=1,y=1)
            bqit9.place(x=1,y=1)
            lw21.place(x=100,y=40)
            ew21.place(x=30,y=80)
            lw22.place(x=100,y=120)
            ew22.place(x=30,y=160)
            ba9.place(x=30,y=280,width='90')
            aa2a8.place(x=130,y=280,width='90')
            lla9.place(x=380,y=20)
            la9.place(x=300,y=20)
        def s10():
            d3np.add(torque1, text='torque') 
            til10.place(x=1,y=1)
            bqit10.place(x=1,y=1)
            lw23.place(x=95,y=40)
            ew23.place(x=30,y=80)
            lw24.place(x=95,y=120)
            ew24.place(x=30,y=160)
            ba10.place(x=30,y=200,width='90')
            aa2a9.place(x=130,y=200,width='90')
            lxx24.place(x=50,y=240)
            exx24.place(x=30,y=280)
            lxx25.place(x=50,y=320)
            exx25.place(x=30,y=360)
            lxx26.place(x=50,y=400)
            exx26.place(x=30,y=440)
            aa3.place(x=30,y=480,width='90')
            aa2a292.place(x=130,y=480,width='90')
            lla10.place(x=380,y=20)
            la10.place(x=300,y=20)
        def s11():
            d3np.add(torqueWithTheta1, text='torqueWithTheta')
            til11.place(x=1,y=1)
            bqit11.place(x=1,y=1)
            lw25.place(x=95,y=40)
            ew25.place(x=30,y=80)
            lw26.place(x=95,y=120)
            ew26.place(x=30,y=160)
            lw27.place(x=95,y=200)
            ew27.place(x=30,y=240)
            ba11.place(x=30,y=280,width='90')
            aa2a10.place(x=130,y=280,width='90')
            lla11.place(x=380,y=20)
            la11.place(x=300,y=20) 
        def s12():
            d3np.add(friction1, text='friction') 
            til12.place(x=1,y=1)
            bqit12.place(x=1,y=1)
            lw28.place(x=50,y=40)
            ew28.place(x=30,y=80)
            lw29.place(x=110,y=120)
            ew29.place(x=30,y=160)
            ba12.place(x=30,y=200,width='90')
            aa2a11.place(x=130,y=200,width='90')
            lla12.place(x=380,y=20)
            la12.place(x=300,y=20)
        def s13():
            d3np.add(frictionCoefficient1, text='friction coefficient')  
            til13.place(x=1,y=1)
            bqit13.place(x=1,y=1)
            lw30.place(x=100,y=40)
            ew30.place(x=30,y=80)
            lw31.place(x=100,y=120)
            ew31.place(x=30,y=160)
            ba13.place(x=30,y=200,width='90')
            aa2a12.place(x=130,y=200,width='90')
            lla13.place(x=450,y=20)
            la13.place(x=300,y=20)
        def s14():
            d3np.add(gravitationalForce1, text='gravitational force')  
            til14.place(x=1,y=1)
            bqit14.place(x=1,y=1)
            lw32.place(x=100,y=40)
            ew32.place(x=30,y=80)
            ba14.place(x=30,y=180,width='90')
            aa2a13.place(x=130,y=180,width='90')
            lla14.place(x=350,y=20)
            la14.place(x=300,y=20)
        def s15():
            d3np.add(generalLawOfAttraction1, text='The general law of attraction') 
            til15.place(x=1,y=1)
            bqit15.place(x=1,y=1)
            lw33.place(x=95,y=40)
            ew33.place(x=30,y=80)
            lw34.place(x=95,y=120)
            ew34.place(x=30,y=160)
            lw35.place(x=95,y=200)
            ew35.place(x=30,y=240)
            ba15.place(x=30,y=280,width='90')
            aa2a14.place(x=130,y=280,width='90')
            lla15.place(x=350,y=20)
            la15.place(x=300,y=20)
        def s16():
            d3np.add(Power1, text='Power') 
            til16.place(x=1,y=1)
            bqit16.place(x=1,y=1)
            lw36.place(x=100,y=40)
            ew36.place(x=30,y=80)
            lw37.place(x=100,y=120)
            ew37.place(x=30,y=160)
            ba16.place(x=30,y=200,width='90')
            aa2a15.place(x=130,y=200,width='90')
            lla16.place(x=400,y=20)
            la16.place(x=300,y=20) 
        def s17():
            d3np.add(conversionFromHorsepowerToJoules1, text='Convert from horsepower to watts')  
            til17.place(x=1,y=1)
            bqit17.place(x=1,y=1)
            lw38.place(x=100,y=40)
            ew38.place(x=30,y=80)
            ba17.place(x=30,y=180,width='90')
            aa2a16.place(x=130,y=180,width='90')
            lla17.place(x=350,y=20)
            la17.place(x=300,y=20)
        def s18():
            d3np.add(graphicAbility1, text='Graphic ability')  
            til18.place(x=1,y=1)
            bqit18.place(x=1,y=1)
            lw39.place(x=100,y=40)
            ew39.place(x=30,y=80)
            lw40.place(x=100,y=120)
            ew40.place(x=30,y=160)
            ba18.place(x=30,y=200,width='90')
            aa2a17.place(x=130,y=200,width='90')
            lla18.place(x=350,y=20)
            la18.place(x=300,y=20) 
        #-------------------------------dynamicsa-----------------------------
        def s19():
            d3np.add(velocity1, text='velocity')  
            til19.place(x=1,y=1)
            bqit19.place(x=1,y=1)
            lw41.place(x=90,y=40)
            ew41.place(x=30,y=80)
            lw42.place(x=100,y=120)
            ew42.place(x=30,y=160)
            ba19.place(x=30,y=200,width='90')
            aa2a18.place(x=130,y=200,width='90')
            lla19.place(x=400,y=20)
            la19.place(x=300,y=20) 
        def s20():
            d3np.add(time1, text='time')  
            til20.place(x=1,y=1)
            bqit20.place(x=1,y=1)
            lw43.place(x=90,y=40)
            ew43.place(x=30,y=80)
            lw44.place(x=100,y=120)
            ew44.place(x=30,y=160)
            ba20.place(x=30,y=200,width='90')
            aa2a19.place(x=130,y=200,width='90')
            lla20.place(x=350,y=20)
            la20.place(x=300,y=20)
        def s21():
            d3np.add(distance1, text='distance') 
            til21.place(x=1,y=1)
            bqit21.place(x=1,y=1)
            lw45.place(x=90,y=40)
            ew45.place(x=30,y=80)
            lw46.place(x=100,y=120)
            ew46.place(x=30,y=160)
            ba21.place(x=30,y=200,width='90')
            aa2a20.place(x=130,y=200,width='90')
            lla21.place(x=400,y=20)
            la21.place(x=300,y=20)
        def s22():
            d3np.add(acceleration1, text='acceleration') 
            til22.place(x=1,y=1)
            bqit22.place(x=1,y=1)
            lw47.place(x=90,y=40)
            ew47.place(x=30,y=80)
            lw48.place(x=100,y=120)
            ew48.place(x=30,y=160)
            ba22.place(x=30,y=200,width='90')
            aa2a21.place(x=130,y=200,width='90')
            lla22.place(x=450,y=20)
            la22.place(x=300,y=20)
        def s23():
            d3np.add(linearDistance1, text='linear Distance')
            til23.place(x=1,y=1)
            bqit23.place(x=1,y=1)
            lw49.place(x=90,y=40)
            ew49.place(x=30,y=80)
            lw50.place(x=100,y=120)
            ew50.place(x=30,y=160)
            lw51.place(x=80,y=200)
            ew51.place(x=30,y=240)
            ba23.place(x=30,y=280,width='90')
            aa2a22.place(x=130,y=280,width='90')
            lla23.place(x=450,y=20)
            la23.place(x=300,y=20) 
        def s24():
            d3np.add(linearTime1, text='linear Time')
            til24.place(x=1,y=1)
            bqit24.place(x=1,y=1)
            lw52.place(x=90,y=40)
            ew52.place(x=30,y=80)
            lw53.place(x=80,y=120)
            ew53.place(x=30,y=160)
            lw54.place(x=80,y=200)
            ew54.place(x=30,y=240)
            ba24.place(x=30,y=280,width='90')
            aa2a23.place(x=130,y=280,width='90')
            lla24.place(x=350,y=20)
            la24.place(x=300,y=20) 
        def s25():
            d3np.add(circularTime1, text='circular Time')
            til25.place(x=1,y=1)
            bqit25.place(x=1,y=1)
            lw55.place(x=90,y=40)
            ew55.place(x=30,y=80)
            lw56.place(x=90,y=120)
            ew56.place(x=30,y=160)
            ba25.place(x=30,y=200,width='90')
            aa2a24.place(x=130,y=200,width='90')
            lla25.place(x=350,y=20)
            la25.place(x=300,y=20)
        def s26():
            d3np.add(periodicDisplacement1, text='periodic Displacement')
            til26.place(x=1,y=1)
            bqit26.place(x=1,y=1)
            lw57.place(x=90,y=40)
            ew57.place(x=30,y=80)
            lw58.place(x=100,y=120)
            ew58.place(x=30,y=160)
            ba26.place(x=30,y=200,width='90')
            aa2a25.place(x=130,y=200,width='90')
            lla26.place(x=350,y=20)
            la26.place(x=300,y=20)
        def s27():
            d3np.add(omega1, text='omega')
            til27.place(x=1,y=1)
            bqit27.place(x=1,y=1)
            lw59.place(x=93,y=40)
            ew59.place(x=30,y=80)
            lw60.place(x=100,y=120)
            ew60.place(x=30,y=160)
            ba27.place(x=30,y=200,width='90')
            aa2a26.place(x=130,y=200,width='90')
            lla27.place(x=350,y=20)
            la27.place(x=300,y=20)
        def s28():
            d3np.add(frequency1, text='frequency')
            til28.place(x=1,y=1)
            bqit28.place(x=1,y=1)
            lw61.place(x=90,y=40)
            ew61.place(x=30,y=80)  
            ba28.place(x=30,y=120,width='90')
            aa4.place(x=125,y=120,width='90')
            aa2a27.place(x=30,y=160,width='185')
            lla28.place(x=400,y=20)
            la28.place(x=300,y=20)
        def s29():
            d3np.add(angularVelocity1, text='angularVelocity')
            til29.place(x=1,y=1)
            bqit29.place(x=1,y=1)
            lw62.place(x=90,y=40)
            ew62.place(x=30,y=80)
            lw63.place(x=95,y=120)
            ew63.place(x=30,y=160)
            lw64.place(x=80,y=200)
            ew64.place(x=30,y=240)
            ba29.place(x=30,y=280,width='90')
            aa2a28.place(x=130,y=280,width='90')
            lla29.place(x=450,y=20)
            la29.place(x=300,y=20)
        def s30():
            d3np.add(linearAcceleration1, text='linearAcceleration')
            til30.place(x=1,y=1)
            bqit30.place(x=1,y=1)
            lw65.place(x=90,y=40)
            ew65.place(x=30,y=80)
            lw66.place(x=100,y=120)
            ew66.place(x=30,y=160)
            ba30.place(x=30,y=200,width='90')
            aa2a29.place(x=130,y=200,width='90')    
            lla30.place(x=450,y=20)
            la30.place(x=300,y=20)
        def s31():
            d3np.add(tangentialVelocity1, text='tangentialVelocity')
            til31.place(x=1,y=1)
            bqit31.place(x=1,y=1)
            lw67.place(x=90,y=40)
            ew67.place(x=30,y=80)
            lw68.place(x=100,y=120)
            ew68.place(x=30,y=160)
            ba31.place(x=30,y=200,width='90')
            aa2a30.place(x=130,y=200,width='90')
            lla31.place(x=450,y=20)
            la31.place(x=300,y=20)
        def s32():
            d3np.add(kineticEnergy1, text='kineticEnergy')
            til32.place(x=1,y=1)
            bqit32.place(x=1,y=1)
            lw69.place(x=90,y=40)
            ew69.place(x=30,y=80)
            lw70.place(x=90,y=120)
            ew70.place(x=30,y=160)
            ba32.place(x=30,y=200,width='90')
            aa2a31.place(x=130,y=200,width='90')
            lla32.place(x=350,y=20)
            la32.place(x=300,y=20)
        def s33():
            d3np.add(energySituation1, text='energySituation')
            til33.place(x=1,y=1)
            bqit33.place(x=1,y=1)
            lw71.place(x=90,y=40)
            ew71.place(x=30,y=80)
            lw72.place(x=90,y=120)
            ew72.place(x=30,y=160)
            ba33.place(x=30,y=200,width='90')
            aa2a32.place(x=130,y=200,width='90')
            lla33.place(x=350,y=20)
            la33.place(x=300,y=20)
        def s34():
            d3np.add(hookeIsLaw1, text='hookeIsLaw')
            til34.place(x=1,y=1)
            bqit34.place(x=1,y=1)
            lw73.place(x=100,y=40)
            ew73.place(x=30,y=80)
            lw74.place(x=100,y=120)
            ew74.place(x=30,y=160)
            ba34.place(x=30,y=200,width='90')
            aa2a33.place(x=130,y=200,width='90')
            lla34.place(x=350,y=20)
            la34.place(x=300,y=20)
        def s35():
            d3np.add(periodicTime1, text='periodicTime')
            til35.place(x=1,y=1)
            bqit35.place(x=1,y=1)
            lw75.place(x=90,y=40)
            ew75.place(x=30,y=80)
            ba35.place(x=30,y=120,width='90')
            aa2a34.place(x=130,y=120,width='90')
            lla35.place(x=420,y=20)
            la35.place(x=300,y=20)
        #-----------------------
        def MechanicalPhysics():
            MechanicalPhysics = Toplevel(home)
            MechanicalPhysics.geometry("500x700+50+200")
            MechanicalPhysics.configure(background="#f8f8ff")
            MechanicalPhysics.resizable(False,False)
            MechanicalPhysics.title("Mechanical Physics")
            MechanicalPhysics.iconbitmap('photo\logo.ico')
            MechanicalPhysics.protocol("WM_DELETE_WINDOW", lambda: close_window(MechanicalPhysics))
            l.config(state='disabled')
            def close_window(window):
                window.destroy()
                l.config(state='normal')
            ####----------------------------------------
            nb = ttk.Notebook(MechanicalPhysics)
            nb.pack()   
            frame_statica = Frame(nb, width='500',height='400',bg='#f8f8ff')
            nb.add(frame_statica, text='static')   
            frame_dynamicsa = Frame(nb, width='500',height='400',bg='#f8f8ff')
            nb.add(frame_dynamicsa, text='dynamics')
            frame_FluidMechanicsa = Frame(nb, width='500',height='400',bg='#f8f8ff')
            nb.add(frame_FluidMechanicsa, text='Fluid Mechanics')
        #--------------------------------------------------------
        #----------------------------Button----------------------------
        #------------------------------statica-----------------
            bm1 = Button(frame_statica,text='volume',command=s1,bg='#537FE7',fg='#E9F8F9',font=2)
            bm1.pack(fill=X)
            bm2 = Button(frame_statica,text='Density',command=s2,bg='#537FE7',fg='#E9F8F9',font=2)
            bm2.pack(fill=X)
            bm3 = Button(frame_statica,text='Force',command=s3,bg='#537FE7',fg='#E9F8F9',font=2)
            bm3.pack(fill=X)
            bm4 = Button(frame_statica,text='Work',command=s4,bg='#537FE7',fg='#E9F8F9',font=2)
            bm4.pack(fill=X)
            bm5 = Button(frame_statica,text='Work Theta',command=s5,bg='#537FE7',fg='#E9F8F9',font=2)
            bm5.pack(fill=X)
            bm6 = Button(frame_statica,text='The resultant of two forces between them is an angle',command=s6,bg='#537FE7',fg='#E9F8F9',font=2)
            bm6.pack(fill=X)
            bm7 = Button(frame_statica,text='The direction of the resultant force between two forces is an angle',command=s7,bg='#537FE7',fg='#E9F8F9',font=2)
            bm7.pack(fill=X)
            bm8 = Button(frame_statica,text='Two perpendicular force analysis',command=s8,bg='#537FE7',fg='#E9F8F9',font=2)
            bm8.pack(fill=X)
            bm9 = Button(frame_statica,text='Direction of two forces perpendicular analysis',command=s9,bg='#537FE7',fg='#E9F8F9',font=2)
            bm9.pack(fill=X)
            bm10 = Button(frame_statica,text='torque',command=s10,bg='#537FE7',fg='#E9F8F9',font=2)
            bm10.pack(fill=X)
            bm11 = Button(frame_statica,text='torque With Theta',command=s11,bg='#537FE7',fg='#E9F8F9',font=2)
            bm11.pack(fill=X)
            bm12 = Button(frame_statica,text='friction',command=s12,bg='#537FE7',fg='#E9F8F9',font=2)
            bm12.pack(fill=X)
            bm13 = Button(frame_statica,text='friction coefficient',command=s13,bg='#537FE7',fg='#E9F8F9',font=2)
            bm13.pack(fill=X)
            bm14 = Button(frame_statica,text='gravitational force',command=s14,bg='#537FE7',fg='#E9F8F9',font=2)
            bm14.pack(fill=X)
            bm15 = Button(frame_statica,text='The general law of attraction',command=s15,bg='#537FE7',fg='#E9F8F9',font=2)
            bm15.pack(fill=X)
            bm16 = Button(frame_statica,text='Power',command=s16,bg='#537FE7',fg='#E9F8F9',font=2)
            bm16.pack(fill=X)
            bm17 = Button(frame_statica,text='Convert from horsepower to watts',command=s17,bg='#537FE7',fg='#E9F8F9',font=2)
            bm17.pack(fill=X)
            bm18 = Button(frame_statica,text='Graphic ability',command=s18,bg='#537FE7',fg='#E9F8F9',font=2)
            bm18.pack(fill=X)
            #------------------------------------------dynamicsa-----------------------------------------------
            bm19 = Button(frame_dynamicsa,text='velocity',command=s19,bg='#537FE7',fg='#E9F8F9',font=2)
            bm19.pack(fill=X)
            bm20 = Button(frame_dynamicsa,text='time',command=s20,bg='#537FE7',fg='#E9F8F9',font=2)
            bm20.pack(fill=X)
            bm21 = Button(frame_dynamicsa,text='distance',command=s21,bg='#537FE7',fg='#E9F8F9',font=2)
            bm21.pack(fill=X)
            bm22 = Button(frame_dynamicsa,text='acceleration',command=s22,bg='#537FE7',fg='#E9F8F9',font=2)
            bm22.pack(fill=X)
            bm23 = Button(frame_dynamicsa,text='linear Distance',command=s23,bg='#537FE7',fg='#E9F8F9',font=2)
            bm23.pack(fill=X)
            bm24 = Button(frame_dynamicsa,text='linear Time',command=s24,bg='#537FE7',fg='#E9F8F9',font=2)
            bm24.pack(fill=X)
            bm25 = Button(frame_dynamicsa,text='circular Time',command=s25,bg='#537FE7',fg='#E9F8F9',font=2)
            bm25.pack(fill=X)
            bm26 = Button(frame_dynamicsa,text='periodic Displacement',command=s26,bg='#537FE7',fg='#E9F8F9',font=2)
            bm26.pack(fill=X)
            bm27 = Button(frame_dynamicsa,text='omega',command=s27,bg='#537FE7',fg='#E9F8F9',font=2)
            bm27.pack(fill=X)
            bm28 = Button(frame_dynamicsa,text='frequency',command=s28,bg='#537FE7',fg='#E9F8F9',font=2)
            bm28.pack(fill=X)
            bm29 = Button(frame_dynamicsa,text='angular Velocity',command=s29,bg='#537FE7',fg='#E9F8F9',font=2)
            bm29.pack(fill=X)
            bm30 = Button(frame_dynamicsa,text='linear Acceleration',command=s30,bg='#537FE7',fg='#E9F8F9',font=2)
            bm30.pack(fill=X)
            bm31 = Button(frame_dynamicsa,text='tangential Velocity',command=s31,bg='#537FE7',fg='#E9F8F9',font=2)
            bm31.pack(fill=X)
            bm32 = Button(frame_dynamicsa,text='kinetic Energy',command=s32,bg='#537FE7',fg='#E9F8F9',font=2)
            bm32.pack(fill=X)
            bm33 = Button(frame_dynamicsa,text='Energy Situation',command=s33,bg='#537FE7',fg='#E9F8F9',font=2)
            bm33.pack(fill=X)
            bm34 = Button(frame_dynamicsa,text='hooke Is Law',command=s34,bg='#537FE7',fg='#E9F8F9',font=2)
            bm34.pack(fill=X)
            bm35 = Button(frame_dynamicsa,text='periodic Time',command=s35,bg='#537FE7',fg='#E9F8F9',font=2)
            bm35.pack(fill=X)
            #----------------------------------------------------------------------
            d3np.pack()
        #####-------------------Electrophysics------------------------------

        def functionssetphysics36():

            if wr36.get() == '' or dr36.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p75 =float(wr36.get())
            p76 =float(dr36.get())
            q36 =  electricWork(p75,p76)
            
            p36.set(q36)
        wr36=StringVar()    
        dr36=StringVar()
        p36=StringVar()

        electricWork1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til36 = Frame(electricWork1,width='250',height='1000',bg='#EDEDF5')
        bqit36 = Button(til36,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(electricWork1,ew76,ew77,p36))
        lw76 = Label(til36,text='coulomb',bg='#EDEDF5',fg='#080808',font=2)
        ew76 = Entry(til36,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr36)
        lw77 = Label(til36,text='volt',bg='#EDEDF5',fg='#080808',font=2)
        ew77 = Entry(til36,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr36)
        aa2a35 = Button(til36,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew76,ew77,p36))
        ba36 = Button(til36,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics36)
        la36 =Label(electricWork1,text="electricWork = ",bg='#f8f8ff',fg='#080808',font=20)
        lla36 = Label(electricWork1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p36)
        popup_menu(ew76,d3np)
        popup_menu(ew77,d3np)
        #-------------------------------------------------

        def functionssetphysics37():
            
            if wr37.get() == '' or dr37.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p77 =float(wr37.get())
            p78 =float(dr37.get())
            q37 =  coulomb(p77,p78)
            
            p37.set(q37)
        wr37=StringVar()    
        dr37=StringVar()
        p37=StringVar()

        coulomb1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til37 = Frame(coulomb1,width='250',height='1000',bg='#EDEDF5')
        bqit37 = Button(til37,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(coulomb1,ew78,ew79,p37))
        lw78 = Label(til37,text='work',bg='#EDEDF5',fg='#080808',font=2)
        ew78 = Entry(til37,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr37)
        lw79 = Label(til37,text='volt',bg='#EDEDF5',fg='#080808',font=2)
        ew79 = Entry(til37,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr37)
        aa2a36 = Button(til37,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew78,ew79,p37))
        ba37 = Button(til37,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics37)
        la37 =Label(coulomb1,text="coulomb = ",bg='#f8f8ff',fg='#080808',font=20)
        lla37 = Label(coulomb1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p37)
        popup_menu(ew78,d3np)
        popup_menu(ew79,d3np)
        #-------------------------------------------------

        def functionssetphysics38():
            
            if wr38.get() == '' or dr38.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p79 =float(wr38.get())
            p80 =float(dr38.get())
            q38 =  current(p79,p80)
            
            p38.set(q38)
        wr38=StringVar()    
        dr38=StringVar()
        p38=StringVar()

        current1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til38 = Frame(current1,width='250',height='1000',bg='#EDEDF5')
        bqit38 = Button(til38,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(current1,ew80,ew81,p38))
        lw80 = Label(til38,text='volt',bg='#EDEDF5',fg='#080808',font=2)
        ew80 = Entry(til38,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr38)
        lw81 = Label(til38,text='resistance',bg='#EDEDF5',fg='#080808',font=2)
        ew81 = Entry(til38,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr38)
        aa2a37 = Button(til38,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew80,ew81,p38))
        ba38 = Button(til38,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics38)
        la38 =Label(current1,text="current = ",bg='#f8f8ff',fg='#080808',font=20)
        lla38 = Label(current1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p38)
        popup_menu(ew80,d3np)
        popup_menu(ew81,d3np)
        #-------------------------------------------------

        def functionssetphysics39():
            
            if wr39.get() == '' or dr39.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p81 =float(wr39.get())
            p82 =float(dr39.get())
            q39 =  electricalPower(p81,p82)
            
            p39.set(q39)
        wr39=StringVar()    
        dr39=StringVar()
        p39=StringVar()

        electricalPower1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til39 = Frame(electricalPower1,width='250',height='1000',bg='#EDEDF5')
        bqit39 = Button(til39,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(electricalPower1,ew82,ew83,p39))
        lw82 = Label(til39,text='work',bg='#EDEDF5',fg='#080808',font=2)
        ew82 = Entry(til39,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr39)
        lw83 = Label(til39,text='time',bg='#EDEDF5',fg='#080808',font=2)
        ew83 = Entry(til39,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr39)
        aa2a38 = Button(til39,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew82,ew83,p39))
        ba39 = Button(til39,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics39)
        la39 =Label(electricalPower1,text="electricalPower = ",bg='#f8f8ff',fg='#080808',font=20)
        lla39 = Label(electricalPower1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p39)
        popup_menu(ew82,d3np)
        popup_menu(ew83,d3np)
        #-------------------------------------------------

        def functionssetphysics40():
            
            if wr40.get() == '' or dr40.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p83 =float(wr40.get())
            p84 =float(dr40.get())
            q40 =  volt(p83,p84)
            
            p40.set(q40)
        wr40=StringVar()    
        dr40=StringVar()
        p40=StringVar()

        volt1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til40 = Frame(volt1,width='250',height='1000',bg='#EDEDF5')
        bqit40 = Button(til40,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(volt1,ew84,ew85,p40))
        lw84 = Label(til40,text='current',bg='#EDEDF5',fg='#080808',font=2)
        ew84 = Entry(til40,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr40)
        lw85 = Label(til40,text='resistance',bg='#EDEDF5',fg='#080808',font=2)
        ew85 = Entry(til40,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr40)
        aa2a39 = Button(til40,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew84,ew85,p40))
        ba40 = Button(til40,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics40)
        la40 =Label(volt1,text="volt = ",bg='#f8f8ff',fg='#080808',font=20)
        lla40 = Label(volt1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p40)
        popup_menu(ew84,d3np)
        popup_menu(ew85,d3np)
        #-------------------------------------------------

        def functionssetphysics41():
            
            if wr41.get() == '' or dr41.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p85 =float(wr41.get())
            p86 =float(dr41.get())
            q41 =  resistance(p85,p86)
            
            p41.set(q41)
        wr41=StringVar()    
        dr41=StringVar()
        p41=StringVar()

        resistance1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til41 = Frame(resistance1,width='250',height='1000',bg='#EDEDF5')
        bqit41 = Button(til41,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(resistance1,ew86,ew87,p41))
        lw86 = Label(til41,text='volt',bg='#EDEDF5',fg='#080808',font=2)
        ew86 = Entry(til41,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr41)
        lw87 = Label(til41,text='current',bg='#EDEDF5',fg='#080808',font=2)
        ew87 = Entry(til41,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr41)
        aa2a40 = Button(til41,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew86,ew87,p41))
        ba41 = Button(til41,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics41)
        la41 =Label(resistance1,text="Resistance = ",bg='#f8f8ff',fg='#080808',font=20)
        lla41 = Label(resistance1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p41)
        popup_menu(ew86,d3np)
        popup_menu(ew87,d3np)
        #-------------------------------------------------

        def functionssetphysics42():
            
            if wr42.get() == '' or dr42.get() == '' or fr10.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p87 =float(wr42.get())
            p88 =float(dr42.get())
            p89 =float(fr10.get())
            q42 =  conductorResistance(p87,p88,p89)
            
            p42.set(q42)

        wr42=StringVar()    
        dr42=StringVar()
        fr10=StringVar()
        p42=StringVar()

        conductorResistance1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til42 = Frame(conductorResistance1,width='250',height='1000',bg='#EDEDF5')
        bqit42 = Button(til42,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(conductorResistance1,ew88,ew89,ew90,p42))
        lw88 = Label(til42,text='conductiveMaterial',bg='#EDEDF5',fg='#080808',font=2)
        ew88 = Entry(til42,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr42)
        lw89 = Label(til42,text='height',bg='#EDEDF5',fg='#080808',font=2)
        ew89 = Entry(til42,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr42)
        lw90 = Label(til42,text='space',bg='#EDEDF5',fg='#080808',font=2)
        ew90 = Entry(til42,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr10)
        aa2a41 = Button(til42,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew88,ew89,ew90,p42))
        ba42 = Button(til42,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics42)
        la42 =Label(conductorResistance1,text="Resistance = ",bg='#f8f8ff',fg='#080808',font=20)
        lla42 = Label(conductorResistance1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p42)
        popup_menu(ew88,d3np)
        popup_menu(ew89,d3np)
        popup_menu(ew90,d3np)
        #-------------------------------------------------

        def functionssetphysics43():
            
            if wr43.get() == '' or dr43.get() == '' or fr11.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p90 =float(wr43.get())
            p91 =float(dr43.get())
            p92 =float(fr11.get())
            q43 =  conductorMaterialType(p90,p91,p92)
            
            p43.set(q43)

        wr43=StringVar()    
        dr43=StringVar()
        fr11=StringVar()
        p43=StringVar()

        conductorMaterialType1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til43 = Frame(conductorMaterialType1,width='250',height='1000',bg='#EDEDF5')
        bqit43 = Button(til43,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(conductorMaterialType1,ew91,ew92,ew93,p43))
        lw91 = Label(til43,text='resistance',bg='#EDEDF5',fg='#080808',font=2)
        ew91 = Entry(til43,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr43)
        lw92 = Label(til43,text='height',bg='#EDEDF5',fg='#080808',font=2)
        ew92 = Entry(til43,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr43)
        lw93 = Label(til43,text='space',bg='#EDEDF5',fg='#080808',font=2)
        ew93 = Entry(til43,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr11)
        aa2a42 = Button(til43,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew91,ew92,ew93,p43))
        ba43 = Button(til43,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics43)
        la43 =Label(conductorMaterialType1,text="conductorMaterialType = ",bg='#f8f8ff',fg='#080808',font=20)
        lla43 = Label(conductorMaterialType1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p43)
        popup_menu(ew91,d3np)
        popup_menu(ew92,d3np)
        popup_menu(ew93,d3np)
        #-------------------------------------------------

        def functionssetphysics44():
            
            if wr44.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p93 =float(wr44.get())
            q44 =  electricalConductivity(p93)
            
            p44.set(q44)

        wr44=StringVar()    
        p44=StringVar()

        electricalConductivity1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til44 = Frame(electricalConductivity1,width='250',height='1000',bg='#EDEDF5')
        bqit44 = Button(til44,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(electricalConductivity1,ew94,p44))
        lw94 = Label(til44,text='conductorMaterialType',bg='#EDEDF5',fg='#080808',font=2)
        ew94 = Entry(til44,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr44)
        aa2a43 = Button(til44,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew94,p44))
        ba44 = Button(til44,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics44)
        la44 =Label(electricalConductivity1,text="electricalConductivity = ",bg='#f8f8ff',fg='#080808',font=20)
        lla44 = Label(electricalConductivity1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p44)
        popup_menu(ew94,d3np)
        #-------------------------------------------------

        def functionssetphysics45():
            
            if wr45.get() == '' or dr45.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p94 =float(wr45.get())
            p95 =float(dr45.get())
            q45 =  capacitorCapacitance(p94,p95)
            
            p45.set(q45)
        wr45=StringVar()    
        dr45=StringVar()
        p45=StringVar()

        capacitorCapacitance1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til45 = Frame(capacitorCapacitance1,width='250',height='1000',bg='#EDEDF5')
        bqit45 = Button(til45,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(capacitorCapacitance1,ew95,ew96,p45))
        lw95 = Label(til45,text='coulomb',bg='#EDEDF5',fg='#080808',font=2)
        ew95 = Entry(til45,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr45)
        lw96 = Label(til45,text='volt',bg='#EDEDF5',fg='#080808',font=2)
        ew96 = Entry(til45,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr45)
        aa2a44 = Button(til45,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew95,ew96,p45))
        ba45 = Button(til45,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics45)
        la45 =Label(capacitorCapacitance1,text="capacitorCapacitance = ",bg='#f8f8ff',fg='#080808',font=20)
        lla45 = Label(capacitorCapacitance1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p45)
        popup_menu(ew95,d3np)
        popup_menu(ew96,d3np)
        #-------------------------------------------------

        def functionssetphysics46():
            
            if wr46.get() == '' or dr46.get() == '' or fr12.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p96 =float(wr46.get())
            p97 =float(dr46.get())
            p98 =float(fr12.get())
            q46 =  capacitorCharge(p96,p97,p98)
            
            p46.set(q46)

        wr46=StringVar()    
        dr46=StringVar()
        fr12=StringVar()
        p46=StringVar()

        capacitorCharge1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til46 = Frame(capacitorCharge1,width='250',height='1000',bg='#EDEDF5')
        bqit46 = Button(til46,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(capacitorCharge1,ew97,ew98,ew99,p46))
        lw97 = Label(til46,text='absoluteInsulationConstant',bg='#EDEDF5',fg='#080808',font=2)
        ew97 = Entry(til46,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr46)
        lw98 = Label(til46,text='plateSpace',bg='#EDEDF5',fg='#080808',font=2)
        ew98 = Entry(til46,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr46)
        lw99 = Label(til46,text='TheDistanceBetweenThePanels',bg='#EDEDF5',fg='#080808',font=2)
        ew99 = Entry(til46,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr12)
        aa2a45 = Button(til46,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew97,ew98,ew99,p46))
        ba46 = Button(til46,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics46)
        la46 =Label(capacitorCharge1,text="conductorMaterialType = ",bg='#f8f8ff',fg='#080808',font=20)
        lla46 = Label(capacitorCharge1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p46)
        popup_menu(ew97,d3np)
        popup_menu(ew98,d3np)
        popup_menu(ew99,d3np)
        #-------------------------------------------------

        def functionssetphysics47():
            
            if wr47.get() == '' or dr47.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p99 =float(wr47.get())
            p100 =float(dr47.get())
            q47 =  waveSpeed(p99,p100)
            
            p47.set(q47)
        wr47=StringVar()    
        dr47=StringVar()
        p47=StringVar()

        waveSpeed1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til47 = Frame(waveSpeed1,width='250',height='1000',bg='#EDEDF5')
        bqit47 = Button(til47,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(waveSpeed1,ew100,ew101,p47))
        lw100 = Label(til47,text='frequencie',bg='#EDEDF5',fg='#080808',font=2)
        ew100 = Entry(til47,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr47)
        lw101 = Label(til47,text='waveLength',bg='#EDEDF5',fg='#080808',font=2)
        ew101 = Entry(til47,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr47)
        aa2a46 = Button(til47,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew100,ew101,p47))
        ba47 = Button(til47,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics47)
        la47 =Label(waveSpeed1,text="waveSpeed = ",bg='#f8f8ff',fg='#080808',font=20)
        lla47 = Label(waveSpeed1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p47)
        popup_menu(ew100,d3np)
        popup_menu(ew101,d3np)
        #-------------------------------------------------

        def functionssetphysics48():
            
            if wr48.get() == '' or dr48.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p101 =float(wr48.get())
            p102 =float(dr48.get())
            q48 =  electronVolt(p101,p102)
            
            p48.set(q48)
        wr48=StringVar()    
        dr48=StringVar()
        p48=StringVar()

        electronVolt1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til48 = Frame(electronVolt1,width='250',height='1000',bg='#EDEDF5')
        bqit48 = Button(til48,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(electronVolt1,ew102,ew103,p48))
        lw102 = Label(til48,text='mass',bg='#EDEDF5',fg='#080808',font=2)
        ew102 = Entry(til48,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr48)
        lw103 = Label(til48,text='velocity',bg='#EDEDF5',fg='#080808',font=2)
        ew103 = Entry(til48,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr48)
        aa2a47 = Button(til48,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew102,ew103,p48))
        ba48 = Button(til48,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics48)
        la48 =Label(electronVolt1,text="Ve  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla48 = Label(electronVolt1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p48)
        popup_menu(ew102,d3np)
        popup_menu(ew103,d3np)
        #-------------------------------------------------

        def functionssetphysics49():
            
            if wr49.get() == '' or dr49.get() == '' or fr13.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p103 =float(wr49.get())
            p104 =float(dr49.get())
            p105 =float(fr13.get())
            q49 =  CoulombIsLaw(p103,p104,p105)
            
            p49.set(q49)

        wr49=StringVar()    
        dr49=StringVar()
        fr13=StringVar()
        p49=StringVar()

        CoulombIsLaw1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til49 = Frame(CoulombIsLaw1,width='250',height='1000',bg='#EDEDF5')
        bqit49 = Button(til49,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(CoulombIsLaw1,ew104,ew105,ew106,p49))
        lw104 = Label(til49,text='Coulomb1',bg='#EDEDF5',fg='#080808',font=2)
        ew104 = Entry(til49,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr49)
        lw105 = Label(til49,text='Coulomb2',bg='#EDEDF5',fg='#080808',font=2)
        ew105 = Entry(til49,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr49)
        lw106 = Label(til49,text='length',bg='#EDEDF5',fg='#080808',font=2)
        ew106 = Entry(til49,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr13)
        aa2a48 = Button(til49,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew104,ew105,ew106,p49))
        ba49 = Button(til49,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics49)
        la49 =Label(CoulombIsLaw1,text="F  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla49 = Label(CoulombIsLaw1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p49)
        popup_menu(ew104,d3np)
        popup_menu(ew105,d3np)
        popup_menu(ew106,d3np)
        #----------------------------Electromagnetism---------------------

        def functionssetphysics50():
            
            if wr50.get() == '' or dr50.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p106 =float(wr50.get())
            p107 =float(dr50.get())
            q50 =  magneticField(p106,p107)
            
            p50.set(q50)
        wr50=StringVar()    
        dr50=StringVar()
        p50=StringVar()

        magneticField1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til50 = Frame(magneticField1,width='250',height='1000',bg='#EDEDF5')
        bqit50 = Button(til50,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(magneticField1,ew107,ew108,p50))
        lw107 = Label(til50,text='magneticFlux',bg='#EDEDF5',fg='#080808',font=2)
        ew107 = Entry(til50,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr50)
        lw108 = Label(til50,text='space',bg='#EDEDF5',fg='#080808',font=2)
        ew108 = Entry(til50,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr50)
        aa2a49 = Button(til50,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew107,ew108,p50))
        ba50 = Button(til50,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics50)
        la50 =Label(magneticField1,text="B  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla50 = Label(magneticField1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p50)
        popup_menu(ew107,d3np)
        popup_menu(ew108,d3np)
        #-------------------------------------------------

        def functionssetphysics51():
            
            if wr51.get() == '' or dr51.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p108 =float(wr51.get())
            p109 =float(dr51.get())
            q51 =  magneticFlux(p108,p109)
            
            p51.set(q51)
        wr51=StringVar()    
        dr51=StringVar()
        p51=StringVar()

        magneticFlux1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til51 = Frame(magneticFlux1,width='250',height='1000',bg='#EDEDF5')
        bqit51 = Button(til51,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(magneticFlux1,ew109,ew110,p51))
        lw109 = Label(til51,text='magneticField',bg='#EDEDF5',fg='#080808',font=2)
        ew109 = Entry(til51,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr51)
        lw110 = Label(til51,text='space',bg='#EDEDF5',fg='#080808',font=2)
        ew110 = Entry(til51,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr51)
        aa2a50 = Button(til51,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew109,ew110,p51))
        ba51 = Button(til51,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics51)
        la51 =Label(magneticFlux1,text="magneticFlux  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla51 = Label(magneticFlux1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p51)
        popup_menu(ew109,d3np)
        popup_menu(ew110,d3np)
        #-------------------------------------------------

        def functionssetphysics52():
            
            if wr52.get() == '' or dr52.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p110 =float(wr52.get())
            p111 =float(dr52.get())
            q52 =  magneticFluxArea(p110,p111)
            
            p52.set(q52)
        wr52=StringVar()    
        dr52=StringVar()
        p52=StringVar()

        magneticFluxArea1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til52 = Frame(magneticFluxArea1,width='250',height='1000',bg='#EDEDF5')
        bqit52 = Button(til52,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(magneticFluxArea1,ew111,ew112,p52))
        lw111 = Label(til52,text='magneticFlux',bg='#EDEDF5',fg='#080808',font=2)
        ew111 = Entry(til52,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr52)
        lw112 = Label(til52,text='magneticField',bg='#EDEDF5',fg='#080808',font=2)
        ew112 = Entry(til52,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr52)
        aa2a51 = Button(til52,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew111,ew112,p52))
        ba52 = Button(til52,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics52)
        la52 =Label(magneticFluxArea1,text="space  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla52 = Label(magneticFluxArea1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p52)
        popup_menu(ew111,d3np)
        popup_menu(ew112,d3np)
        #-------------------------------------------------

        def functionssetphysics53():
            
            if wr53.get() == '' or dr53.get() == '' or dr54.get() == '' or wr54.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p112 =float(wr53.get())
            p113 =float(dr53.get())
            p114 =float(dr54.get())
            p115 =float(wr54.get())
            q53 =  magneticFluxDensity(p112,p113,p114,p115)
            
            p53.set(q53)

        wr53=StringVar()    
        dr53=StringVar()
        wr54=StringVar()    
        dr54=StringVar()
        p53=StringVar()

        magneticFluxDensity1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til53 = Frame(magneticFluxDensity1,width='250',height='1000',bg='#EDEDF5')
        bqit53 = Button(til53,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide4(magneticFluxDensity1,ew113,ew114,ew115,ew116,p53))
        lw113 = Label(til53,text='current',bg='#EDEDF5',fg='#080808',font=2)
        ew113 = Entry(til53,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr53)
        lw114 = Label(til53,text='numberOfTurns',bg='#EDEDF5',fg='#080808',font=2)
        ew114 = Entry(til53,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr53)
        lw115 = Label(til53,text='magneticPermeability',bg='#EDEDF5',fg='#080808',font=2)
        ew115 = Entry(til53,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr54)
        lw116 = Label(til53,text='RadiusLength',bg='#EDEDF5',fg='#080808',font=2)
        ew116 = Entry(til53,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr54)
        aa2a52 = Button(til53,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide44(ew113,ew114,ew115,ew116,p53))
        ba53 = Button(til53,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics53)
        la53 =Label(magneticFluxDensity1,text="B  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla53 = Label(magneticFluxDensity1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p53)
        popup_menu(ew113,d3np)
        popup_menu(ew114,d3np)
        popup_menu(ew115,d3np)
        popup_menu(ew116,d3np)
        #-------------------------------------------------

        def functionssetphysics54():
            
            if wr55.get() == '' or dr55.get() == '' or fr14.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p116 =float(wr55.get())
            p117 =float(dr55.get())
            p118 =float(fr14.get())
            q54 =  magneticFieldForce(p116,p117,p118)
            
            p54.set(q54)

        wr55=StringVar()    
        dr55=StringVar()
        fr14=StringVar()    
        p54=StringVar()

        magneticFieldForce1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til54 = Frame(magneticFieldForce1,width='250',height='1000',bg='#EDEDF5')
        bqit54 = Button(til54,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(magneticFieldForce1,ew117,ew118,ew119,p54))
        lw117 = Label(til54,text='magneticField',bg='#EDEDF5',fg='#080808',font=2)
        ew117 = Entry(til54,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr55)
        lw118 = Label(til54,text='current',bg='#EDEDF5',fg='#080808',font=2)
        ew118 = Entry(til54,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr55)
        lw119 = Label(til54,text='height',bg='#EDEDF5',fg='#080808',font=2)
        ew119 = Entry(til54,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr14)
        aa2a53 = Button(til54,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew117,ew118,ew119,p54))
        ba54 = Button(til54,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics54)
        la54 =Label(magneticFieldForce1,text="magneticFieldForce  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla54 = Label(magneticFieldForce1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p54)
        popup_menu(ew117,d3np)
        popup_menu(ew118,d3np)
        popup_menu(ew119,d3np)
        #-------------------------------------------------

        def functionssetphysics55():
            
            if wr56.get() == '' or dr56.get() == '' or dr57.get() == '' or wr57.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p119 =float(wr56.get())
            p120 =float(dr56.get())
            p121 =float(dr57.get())
            p122 =float(wr57.get())
            q55 =  magneticFieldForceWithTheta(p119,p120,p121,p122)
            
            p55.set(q55)

        wr56=StringVar()    
        dr56=StringVar()
        wr57=StringVar()    
        dr57=StringVar()
        p55=StringVar()

        magneticFieldForceWithTheta1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til55 = Frame(magneticFieldForceWithTheta1,width='250',height='1000',bg='#EDEDF5')
        bqit55 = Button(til55,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide4(magneticFieldForceWithTheta1,ew120,ew121,ew122,ew123,p55))
        lw120 = Label(til55,text='magneticFieldForce',bg='#EDEDF5',fg='#080808',font=2)  
        ew120 = Entry(til55,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr56)
        lw121 = Label(til55,text='current',bg='#EDEDF5',fg='#080808',font=2)
        ew121 = Entry(til55,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr56)
        lw122 = Label(til55,text='height',bg='#EDEDF5',fg='#080808',font=2)
        ew122 = Entry(til55,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr57)
        lw123 = Label(til55,text='theta',bg='#EDEDF5',fg='#080808',font=2)
        ew123 = Entry(til55,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr57)
        aa2a54 = Button(til55,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide44(ew120,ew121,ew122,ew123,p55))
        ba55 = Button(til55,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics55)
        la55 =Label(magneticFieldForceWithTheta1,text="magneticFieldForce  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla55 = Label(magneticFieldForceWithTheta1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p55)
        popup_menu(ew120,d3np)
        popup_menu(ew121,d3np)
        popup_menu(ew122,d3np)
        popup_menu(ew123,d3np)
        #-------------------------------------------------

        def functionssetphysics56():
            
            if wr58.get() == '' or dr58.get() == '' or dr59.get() == '' or wr59.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p123 =float(wr58.get())
            p124 =float(dr58.get())
            p125 =float(dr59.get())
            p126 =float(wr59.get())
            q56 =  fluxDensity(p123,p124,p125,p126)
            
            p56.set(q56)

        wr58=StringVar()    
        dr58=StringVar()
        wr59=StringVar()    
        dr59=StringVar()
        p56=StringVar()

        fluxDensity1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til56 = Frame(fluxDensity1,width='250',height='1000',bg='#EDEDF5')
        bqit56 = Button(til56,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide4(fluxDensity1,ew124,ew125,ew126,ew127,p56))
        lw124 = Label(til56,text='magneticFieldForce',bg='#EDEDF5',fg='#080808',font=2)  
        ew124 = Entry(til56,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr58)
        lw125 = Label(til56,text='current',bg='#EDEDF5',fg='#080808',font=2)
        ew125 = Entry(til56,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr58)
        lw126 = Label(til56,text='height',bg='#EDEDF5',fg='#080808',font=2)
        ew126 = Entry(til56,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr59)
        lw127 = Label(til56,text='theta',bg='#EDEDF5',fg='#080808',font=2)
        ew127 = Entry(til56,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr59)
        aa2a55 = Button(til56,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide44(ew124,ew125,ew126,ew127,p56))
        ba56 = Button(til56,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics56)
        la56 =Label(fluxDensity1,text="fluxDensity  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla56 = Label(fluxDensity1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p56)
        popup_menu(ew124,d3np)
        popup_menu(ew125,d3np)
        popup_menu(ew126,d3np)
        popup_menu(ew127,d3np)
        #-------------------------------------------------

        def functionssetphysics57():
            
            if wr60.get() == '' or dr60.get() == '' or fr15.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p127 =float(wr60.get())
            p128 =float(dr60.get())
            p129 =float(fr15.get())
            q57 =  magneticMoment(p127,p128,p129)
            
            p57.set(q57)

        wr60=StringVar()    
        dr60=StringVar()
        fr15=StringVar()    
        p57=StringVar()

        magneticMoment1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til57 = Frame(magneticMoment1,width='250',height='1000',bg='#EDEDF5')
        bqit57 = Button(til57,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(magneticMoment1,ew128,ew129,ew130,p57))
        lw128 = Label(til57,text='current',bg='#EDEDF5',fg='#080808',font=2)  
        ew128 = Entry(til57,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr60)
        lw129 = Label(til57,text='area',bg='#EDEDF5',fg='#080808',font=2)
        ew129 = Entry(til57,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr60)
        lw130 = Label(til57,text='numberOfTurns',bg='#EDEDF5',fg='#080808',font=2)
        ew130 = Entry(til57,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr15)
        aa2a56 = Button(til57,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew128,ew129,ew130,p57))
        ba57 = Button(til57,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics57)
        la57 =Label(magneticMoment1,text="fluxDensity  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla57 = Label(magneticMoment1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p57)
        popup_menu(ew128,d3np)
        popup_menu(ew129,d3np)
        popup_menu(ew130,d3np)
        #-------------------------------------------------

        def functionssetphysics58():
            
            if wr61.get() == '' or dr61.get() == '' or fr16.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p130 =float(wr61.get())
            p131 =float(dr61.get())
            p132 =float(fr16.get())
            q58 =  averageElectromotiveForceGeneratedByAChargedCoil(p130,p131,p132)
            
            p58.set(q58)

        wr61=StringVar()    
        dr61=StringVar()
        fr16=StringVar()    
        p58=StringVar()

        averageElectromotiveForceGeneratedByAChargedCoil1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til58 = Frame(averageElectromotiveForceGeneratedByAChargedCoil1,width='250',height='1000',bg='#EDEDF5')
        bqit58 = Button(til58,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(averageElectromotiveForceGeneratedByAChargedCoil1,ew131,ew132,ew133,p58))
        lw131 = Label(til58,text='magneticFlux',bg='#EDEDF5',fg='#080808',font=2)  
        ew131 = Entry(til58,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr61)
        lw132 = Label(til58,text='time',bg='#EDEDF5',fg='#080808',font=2)
        ew132 = Entry(til58,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr61)
        lw133 = Label(til58,text='numberOfTurns',bg='#EDEDF5',fg='#080808',font=2)
        ew133 = Entry(til58,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr16)
        aa2a57 = Button(til58,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew131,ew132,ew133,p58))
        ba58 = Button(til58,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics58)
        la58 =Label(averageElectromotiveForceGeneratedByAChargedCoil1,text="fluxDensity  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla58 = Label(averageElectromotiveForceGeneratedByAChargedCoil1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p58)
        popup_menu(ew131,d3np)
        popup_menu(ew132,d3np)
        popup_menu(ew133,d3np)
        #-------------------------------------------------

        def functionssetphysics59():
            
            if wr62.get() == '' or dr62.get() == '' or fr17.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p133 =float(wr62.get())
            p134 =float(dr62.get())
            p135 =float(fr17.get())
            q59 =  mutualInduction(p133,p134,p135)
            
            p59.set(q59)

        wr62=StringVar()    
        dr62=StringVar()
        fr17=StringVar()    
        p59=StringVar()

        mutualInduction1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til59 = Frame(mutualInduction1,width='250',height='1000',bg='#EDEDF5')
        bqit59 = Button(til59,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(mutualInduction1,ew134,ew135,ew136,p59))
        lw134 = Label(til59,text='factorAffecting',bg='#EDEDF5',fg='#080808',font=2)            
        lwx = Label(til59,text='TheInductanceCoefficient',bg='#EDEDF5',fg='#080808',font=2)  
        ew134 = Entry(til59,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr62)
        lw135 = Label(til59,text='current',bg='#EDEDF5',fg='#080808',font=2)
        ew135 = Entry(til59,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr62)
        lw136 = Label(til59,text='time',bg='#EDEDF5',fg='#080808',font=2)
        ew136 = Entry(til59,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr17)
        aa2a58 = Button(til59,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew134,ew135,ew136,p59))
        ba59 = Button(til59,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics59)
        la59 =Label(mutualInduction1,text="mutualInduction  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla59 = Label(mutualInduction1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p59)
        popup_menu(ew134,d3np)
        popup_menu(ew135,d3np)
        popup_menu(ew136,d3np)
        #-------------------------------------------------

        def functionssetphysics60():
            
            if wr63.get() == '' or dr63.get() == '' or fr18.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p136 =float(wr63.get())
            p137 =float(dr63.get())
            p138 =float(fr18.get())
            q60 =  factorAffectingTheInductanceCoefficient(p136,p137,p138)
            
            p60.set(q60)

        wr63=StringVar()    
        dr63=StringVar()
        fr18=StringVar()    
        p60=StringVar()

        factorAffectingTheInductanceCoefficient1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til60 = Frame(factorAffectingTheInductanceCoefficient1,width='250',height='1000',bg='#EDEDF5')
        bqit60 = Button(til60,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide3(factorAffectingTheInductanceCoefficient1,ew137,ew138,ew139,p60))
        lw137 = Label(til60,text='mutualInduction',bg='#EDEDF5',fg='#080808',font=2)    
        ew137 = Entry(til60,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr63)
        lw138 = Label(til60,text='current',bg='#EDEDF5',fg='#080808',font=2)
        ew138 = Entry(til60,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr63)
        lw139 = Label(til60,text='time',bg='#EDEDF5',fg='#080808',font=2)
        ew139 = Entry(til60,bg='#f8f8ff',fg='#080808',font=2,textvariable=fr18)
        aa2a59 = Button(til60,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide33(ew137,ew138,ew139,p60))
        ba60 = Button(til60,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics60)
        la60 =Label(factorAffectingTheInductanceCoefficient1,text="factorAffectingTheInductanceCoefficient  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla60 = Label(factorAffectingTheInductanceCoefficient1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p60)
        popup_menu(ew137,d3np)
        popup_menu(ew138,d3np)
        popup_menu(ew139,d3np)
        #-------------------------------------------------

        def functionssetphysics61():
            
            if wr64.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p139 =float(wr64.get())
            q61 =  coulombIsEqualToHowManyElectrons(p139)
            
            p61.set(q61)

        wr64=StringVar()     
        p61=StringVar()

        coulombIsEqualToHowManyElectrons1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til61 = Frame(coulombIsEqualToHowManyElectrons1,width='250',height='1000',bg='#EDEDF5')
        bqit61 = Button(til61,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(coulombIsEqualToHowManyElectrons1,ew140,p61))
        lw140 = Label(til61,text='coulomb',bg='#EDEDF5',fg='#080808',font=2)    
        ew140 = Entry(til61,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr64)
        aa2a60 = Button(til61,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew140,p61))
        ba61 = Button(til61,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics61)
        la61 =Label(coulombIsEqualToHowManyElectrons1,text="Electrons  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla61 = Label(coulombIsEqualToHowManyElectrons1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p61)
        popup_menu(ew140,d3np)
        #-------------------------------------------------

        def functionssetphysics62():
            
            if wr65.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p140 =float(wr65.get())
            q62 =  electronsEqualToTheNumberOfCoulombs(p140)
            
            p62.set(q62)

        wr65=StringVar()     
        p62=StringVar()

        electronsEqualToTheNumberOfCoulombs1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til62 = Frame(electronsEqualToTheNumberOfCoulombs1,width='250',height='1000',bg='#EDEDF5')
        bqit62 = Button(til62,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(electronsEqualToTheNumberOfCoulombs1,ew141,p62))
        lw141 = Label(til62,text='coulomb',bg='#EDEDF5',fg='#080808',font=2)    
        ew141 = Entry(til62,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr65)
        aa2a61 = Button(til62,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew141,p62))
        ba62 = Button(til62,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics62)
        la62 =Label(electronsEqualToTheNumberOfCoulombs1,text="Coulombs  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla62 = Label(electronsEqualToTheNumberOfCoulombs1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p62)
        popup_menu(ew141,d3np)
        #-------------------------------------------------

        def functionssetphysics63():

            if wr66.get() == '':
                  messagebox.showinfo("EROR",'Fill the cell')
            p141 =float(wr66.get())
            q63 =  conversionFromElectronVoltsToJoules(p141)
            
            
            p63.set(q63)

        wr66=StringVar()     
        p63=StringVar()
        
        
        conversionFromElectronVoltsToJoules1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til63 = Frame(conversionFromElectronVoltsToJoules1,width='250',height='1000',bg='#EDEDF5')
        bqit63 = Button(til63,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(conversionFromElectronVoltsToJoules1,ew142,p63))
        lw142 = Label(til63,text='ElectronVolts',bg='#EDEDF5',fg='#080808',font=2)    
        ew142 = Entry(til63,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr66)
        aa2a62 = Button(til63,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew142,p63))
        ba63 = Button(til63,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics63)
        la63 =Label(conversionFromElectronVoltsToJoules1,text="Joule  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla63 = Label(conversionFromElectronVoltsToJoules1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p63)
        popup_menu(ew142,d3np)
        #-------------------------------------------------

        def functionssetphysics64():
            
            if wr67.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p142 =float(wr67.get())
            q64 =  conversionFromJoulesToElectronVolts(p142)
            
            p64.set(q64)

        wr67=StringVar()     
        p64=StringVar()

        conversionFromJoulesToElectronVolts1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til64 = Frame(conversionFromJoulesToElectronVolts1,width='250',height='1000',bg='#EDEDF5')
        bqit64 = Button(til64,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(conversionFromJoulesToElectronVolts1,ew143,p64))
        lw143 = Label(til64,text='Joule',bg='#EDEDF5',fg='#080808',font=2)    
        ew143 = Entry(til64,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr67)
        aa2a63 = Button(til64,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew143,p64))
        ba64 = Button(til64,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics64)
        la64 =Label(conversionFromJoulesToElectronVolts1,text="ElectronVolts  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla64 = Label(conversionFromJoulesToElectronVolts1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p64)
        popup_menu(ew143,d3np)
        #####-------------------Electrophysics------------------------------
        def e1():
            d3np.add(electricWork1, text='electricWork')
            til36.place(x=1,y=1)
            bqit36.place(x=1,y=1)
            lw76.place(x=90,y=40)
            ew76.place(x=30,y=80)
            lw77.place(x=105,y=120)
            ew77.place(x=30,y=160)
            ba36.place(x=30,y=200,width='90')
            aa2a35.place(x=130,y=200,width='90')
            lla36.place(x=420,y=20)
            la36.place(x=300,y=20)
        def e2():
            d3np.add(coulomb1, text='coulomb')
            til37.place(x=1,y=1)
            bqit37.place(x=1,y=1)
            lw78.place(x=95,y=40)
            ew78.place(x=30,y=80)
            lw79.place(x=105,y=120)
            ew79.place(x=30,y=160)
            ba37.place(x=30,y=200,width='90')
            aa2a36.place(x=130,y=200,width='90')
            lla37.place(x=420,y=20)
            la37.place(x=300,y=20)
        def e3():
            d3np.add(current1, text='current')
            til38.place(x=1,y=1)
            bqit38.place(x=1,y=1)
            lw80.place(x=100,y=40)
            ew80.place(x=30,y=80)
            lw81.place(x=80,y=120)
            ew81.place(x=30,y=160)
            ba38.place(x=30,y=200,width='90')
            aa2a37.place(x=130,y=200,width='90')
            lla38.place(x=400,y=20)
            la38.place(x=300,y=20)
        def e4():
            d3np.add(electricalPower1, text='electricalPower')
            til39.place(x=1,y=1)
            bqit39.place(x=1,y=1)
            lw82.place(x=100,y=40)
            ew82.place(x=30,y=80)
            lw83.place(x=100,y=120)
            ew83.place(x=30,y=160)
            ba39.place(x=30,y=200,width='90')
            aa2a38.place(x=130,y=200,width='90')
            lla39.place(x=430,y=20)
            la39.place(x=300,y=20)
        def e5():
            d3np.add(volt1, text='volt')
            til40.place(x=1,y=1)
            bqit40.place(x=1,y=1)
            lw84.place(x=100,y=40)
            ew84.place(x=30,y=80)
            lw85.place(x=90,y=120)
            ew85.place(x=30,y=160)
            ba40.place(x=30,y=200,width='90')
            aa2a39.place(x=130,y=200,width='90')
            lla40.place(x=350,y=20)
            la40.place(x=300,y=20)
        def e6():
            d3np.add(resistance1, text='resistance')
            til41.place(x=1,y=1)
            bqit41.place(x=1,y=1)
            lw86.place(x=100,y=40)
            ew86.place(x=30,y=80)
            lw87.place(x=90,y=120)
            ew87.place(x=30,y=160)
            ba41.place(x=30,y=200,width='90')
            aa2a40.place(x=130,y=200,width='90')
            lla41.place(x=400,y=20)
            la41.place(x=300,y=20)
        def e7():
            d3np.add(conductorResistance1, text='conductorResistance')
            til42.place(x=1,y=1)
            bqit42.place(x=1,y=1)
            lw88.place(x=50,y=40)
            ew88.place(x=30,y=80)
            lw89.place(x=90,y=120)
            ew89.place(x=30,y=160)
            lw90.place(x=90,y=200)
            ew90.place(x=30,y=240)
            ba42.place(x=30,y=280,width='90')
            aa2a41.place(x=130,y=280,width='90')
            lla42.place(x=400,y=20)
            la42.place(x=300,y=20)
        def e8():
            d3np.add(conductorMaterialType1, text='conductorMaterialType')
            til43.place(x=1,y=1)
            bqit43.place(x=1,y=1)
            lw91.place(x=80,y=40)
            ew91.place(x=30,y=80)
            lw92.place(x=90,y=120)
            ew92.place(x=30,y=160)
            lw93.place(x=90,y=200)
            ew93.place(x=30,y=240)
            ba43.place(x=30,y=280,width='90')
            aa2a42.place(x=130,y=280,width='90')
            lla43.place(x=500,y=20)
            la43.place(x=300,y=20)
        def e9():
            d3np.add(electricalConductivity1, text='electricalConductivity')
            til44.place(x=1,y=1)
            bqit44.place(x=1,y=1)
            lw94.place(x=45,y=40)
            ew94.place(x=30,y=80)
            ba44.place(x=30,y=120,width='90')
            aa2a43.place(x=130,y=120,width='90')
            lla44.place(x=500,y=20)
            la44.place(x=300,y=20)
        def e10():
            d3np.add(capacitorCapacitance1, text='capacitorCapacitance')
            til45.place(x=1,y=1)
            bqit45.place(x=1,y=1)
            lw95.place(x=80,y=40)
            ew95.place(x=30,y=80)
            lw96.place(x=100,y=120)
            ew96.place(x=30,y=160)
            ba45.place(x=30,y=200,width='90')
            aa2a44.place(x=130,y=200,width='90')
            lla45.place(x=500,y=20)
            la45.place(x=300,y=20)
        def e11():
            d3np.add(capacitorCharge1, text='capacitorCharge')
            til46.place(x=1,y=1)
            bqit46.place(x=1,y=1)
            lw97.place(x=26,y=40)
            ew97.place(x=30,y=80)
            lw98.place(x=80,y=120)
            ew98.place(x=30,y=160)
            lw99.place(x=10,y=200)
            ew99.place(x=30,y=240)
            ba46.place(x=30,y=280,width='90')
            aa2a45.place(x=130,y=280,width='90')
            lla46.place(x=500,y=20)
            la46.place(x=300,y=20)
        def e12():
            d3np.add(waveSpeed1, text='waveSpeed')
            til47.place(x=1,y=1)
            bqit47.place(x=1,y=1)
            lw100.place(x=80,y=40)
            ew100.place(x=30,y=80)
            lw101.place(x=80,y=120)
            ew101.place(x=30,y=160)
            ba47.place(x=30,y=200,width='90')
            aa2a46.place(x=130,y=200,width='90')
            lla47.place(x=430,y=20)
            la47.place(x=300,y=20)
        def e13():
            d3np.add(electronVolt1, text='electronVolt')
            til48.place(x=1,y=1)
            bqit48.place(x=1,y=1)
            lw102.place(x=95,y=40)
            ew102.place(x=30,y=80)
            lw103.place(x=90,y=120)
            ew103.place(x=30,y=160)
            ba48.place(x=30,y=200,width='90')
            aa2a47.place(x=130,y=200,width='90')
            lla48.place(x=350,y=20)
            la48.place(x=300,y=20)
        def e14():
            d3np.add(CoulombIsLaw1, text='CoulombIsLaw')
            til49.place(x=1,y=1)
            bqit49.place(x=1,y=1)
            lw104.place(x=80,y=40)
            ew104.place(x=30,y=80)
            lw105.place(x=80,y=120)
            ew105.place(x=30,y=160)
            lw106.place(x=95,y=200)
            ew106.place(x=30,y=240)
            ba49.place(x=30,y=280,width='90')
            aa2a48.place(x=130,y=280,width='90')
            lla49.place(x=350,y=20)
            la49.place(x=300,y=20)
        def e15():
            d3np.add(magneticField1, text='magneticField')
            til50.place(x=1,y=1)
            bqit50.place(x=1,y=1)
            lw107.place(x=70,y=40)
            ew107.place(x=30,y=80)
            lw108.place(x=90,y=120)
            ew108.place(x=30,y=160)
            ba50.place(x=30,y=200,width='90')
            aa2a49.place(x=130,y=200,width='90')
            lla50.place(x=350,y=20)
            la50.place(x=300,y=20)
        def e16():
            d3np.add(magneticFlux1, text='magneticFlux')
            til51.place(x=1,y=1)
            bqit51.place(x=1,y=1)
            lw109.place(x=65,y=40)
            ew109.place(x=30,y=80)
            lw110.place(x=90,y=120)
            ew110.place(x=30,y=160)
            ba51.place(x=30,y=200,width='90')
            aa2a50.place(x=130,y=200,width='90')
            lla51.place(x=430,y=20)
            la51.place(x=300,y=20)
        def e17(): 
            d3np.add(magneticFluxArea1, text='magneticFluxArea')
            til52.place(x=1,y=1)
            bqit52.place(x=1,y=1)
            lw111.place(x=65,y=40)
            ew111.place(x=30,y=80)
            lw112.place(x=65,y=120)
            ew112.place(x=30,y=160)
            ba52.place(x=30,y=200,width='90')
            aa2a51.place(x=130,y=200,width='90')
            lla52.place(x=380,y=20)
            la52.place(x=300,y=20)
        def e18():
            d3np.add(magneticFluxDensity1, text='magneticFluxDensity')
            til53.place(x=1,y=1)
            bqit53.place(x=1,y=1)
            lw113.place(x=90,y=40)
            ew113.place(x=30,y=80)
            lw114.place(x=65,y=120)
            ew114.place(x=30,y=160)
            lw115.place(x=40,y=200)
            ew115.place(x=30,y=240)
            lw116.place(x=70,y=280)
            ew116.place(x=30,y=320)
            ba53.place(x=30,y=360,width='90')
            aa2a52.place(x=130,y=360,width='90')
            lla53.place(x=350,y=20)
            la53.place(x=300,y=20)
        def e19():
            d3np.add(magneticFieldForce1, text='magneticFieldForce')
            til54.place(x=1,y=1)
            bqit54.place(x=1,y=1)
            lw117.place(x=70,y=40)
            ew117.place(x=30,y=80)
            lw118.place(x=90,y=120)
            ew118.place(x=30,y=160)
            lw119.place(x=90,y=200)
            ew119.place(x=30,y=240)
            ba54.place(x=30,y=280,width='90')
            aa2a53.place(x=130,y=280,width='90')
            lla54.place(x=480,y=20)
            la54.place(x=300,y=20)
        def e20():
            d3np.add(magneticFieldForceWithTheta1, text='magneticFieldForceWithTheta')
            til55.place(x=1,y=1)
            bqit55.place(x=1,y=1)
            lw120.place(x=45,y=40)
            ew120.place(x=30,y=80)
            lw121.place(x=90,y=120)
            ew121.place(x=30,y=160)
            lw122.place(x=90,y=200)
            ew122.place(x=30,y=240)
            lw123.place(x=95,y=280)
            ew123.place(x=30,y=320)
            ba55.place(x=30,y=360,width='90')
            aa2a54.place(x=130,y=360,width='90')
            lla55.place(x=480,y=20)
            la55.place(x=300,y=20)
        def e21():
            d3np.add(fluxDensity1, text='fluxDensity')
            til56.place(x=1,y=1)
            bqit56.place(x=1,y=1)
            lw124.place(x=45,y=40)
            ew124.place(x=30,y=80)
            lw125.place(x=90,y=120)
            ew125.place(x=30,y=160)
            lw126.place(x=90,y=200)
            ew126.place(x=30,y=240)
            lw127.place(x=95,y=280)
            ew127.place(x=30,y=320)
            ba56.place(x=30,y=360,width='90')
            aa2a55.place(x=130,y=360,width='90')
            lla56.place(x=480,y=20)
            la56.place(x=300,y=20)
        def e22():
            d3np.add(magneticMoment1, text='magneticMoment')
            til57.place(x=1,y=1)
            bqit57.place(x=1,y=1)
            lw128.place(x=90,y=40)
            ew128.place(x=30,y=80)
            lw129.place(x=100,y=120)
            ew129.place(x=30,y=160)
            lw130.place(x=70,y=200)
            ew130.place(x=30,y=240)
            ba57.place(x=30,y=280,width='90')
            aa2a56.place(x=130,y=280,width='90')
            lla57.place(x=400,y=20)
            la57.place(x=300,y=20)
        def e23():
            d3np.add(averageElectromotiveForceGeneratedByAChargedCoil1, text='averageElectromotiveForceGeneratedByAChargedCoil')
            til58.place(x=1,y=1)
            bqit58.place(x=1,y=1)
            lw131.place(x=75,y=40)
            ew131.place(x=30,y=80)
            lw132.place(x=100,y=120)
            ew132.place(x=30,y=160)
            lw133.place(x=70,y=200)
            ew133.place(x=30,y=240)
            ba58.place(x=30,y=280,width='90')
            aa2a57.place(x=130,y=280,width='90')
            lla58.place(x=400,y=20)
            la58.place(x=300,y=20)
        def e24():
            d3np.add(mutualInduction1, text='mutualInduction')
            til59.place(x=1,y=1)
            bqit59.place(x=1,y=1)
            lw134.place(x=65,y=16)
            lwx.place(x=30,y=40)
            ew134.place(x=30,y=80)
            lw135.place(x=100,y=120)
            ew135.place(x=30,y=160)
            lw136.place(x=105,y=200)
            ew136.place(x=30,y=240)
            ba59.place(x=30,y=280,width='90')
            aa2a58.place(x=130,y=280,width='90')
            lla59.place(x=430,y=20)
            la59.place(x=300,y=20)
        def e25():
            d3np.add(factorAffectingTheInductanceCoefficient1, text='factorAffectingTheInductanceCoefficient')
            til60.place(x=1,y=1)
            bqit60.place(x=1,y=1)
            lw137.place(x=65,y=40)
            ew137.place(x=30,y=80)
            lw138.place(x=100,y=120)
            ew138.place(x=30,y=160)
            lw139.place(x=105,y=200)
            ew139.place(x=30,y=240)
            ba60.place(x=30,y=280,width='90')
            aa2a59.place(x=130,y=280,width='90')
            lla60.place(x=600,y=20)
            la60.place(x=300,y=20)
        def e26():
            d3np.add(coulombIsEqualToHowManyElectrons1, text='coulombIsEqualToHowManyElectrons')
            til61.place(x=1,y=1)
            bqit61.place(x=1,y=1)
            lw140.place(x=90,y=40)
            ew140.place(x=30,y=80)
            ba61.place(x=30,y=120,width='90')
            aa2a60.place(x=130,y=120,width='90')
            lla61.place(x=400,y=20)
            la61.place(x=300,y=20)
        def e27():
            d3np.add(electronsEqualToTheNumberOfCoulombs1, text='electronsEqualToTheNumberOfCoulombs')
            til62.place(x=1,y=1)
            bqit62.place(x=1,y=1)
            lw141.place(x=90,y=40)
            ew141.place(x=30,y=80)
            ba62.place(x=30,y=120,width='90')
            aa2a61.place(x=130,y=120,width='90')
            lla62.place(x=400,y=20)
            la62.place(x=300,y=20)
        def e28():
            d3np.add(conversionFromElectronVoltsToJoules1, text='conversionFromElectronVoltsToJoules')
            til63.place(x=1,y=1)
            bqit63.place(x=1,y=1)
            lw142.place(x=70,y=40)
            ew142.place(x=30,y=80)
            ba63.place(x=30,y=120,width='90')
            aa2a62.place(x=130,y=120,width='90')
            lla63.place(x=370,y=20)
            la63.place(x=300,y=20)
        def e29():
            d3np.add(conversionFromJoulesToElectronVolts1, text='conversionFromJoulesToElectronVolts')
            til64.place(x=1,y=1)
            bqit64.place(x=1,y=1)
            lw143.place(x=100,y=40)
            ew143.place(x=30,y=80)
            ba64.place(x=30,y=120,width='90')
            aa2a63.place(x=130,y=120,width='90')
            lla64.place(x=430,y=20)
            la64.place(x=300,y=20)
        #-----------------------
        def Electrophysics():
            Electrophysics = Toplevel(home)
            Electrophysics.geometry("500x700+50+200")
            Electrophysics.configure(background="#f8f8ff")
            Electrophysics.resizable(False,False)
            Electrophysics.title("Electro Physics")
            Electrophysics.iconbitmap('photo\logo.ico')
            Electrophysics.protocol("WM_DELETE_WINDOW", lambda: close_window(Electrophysics))
            l2.config(state='disabled')
            def close_window(window):
                window.destroy()
                l2.config(state='normal')
            #================================
            nb2 = ttk.Notebook(Electrophysics)
            nb2.pack()
            frame_Electricity = Frame(nb2, width='500',height='700',bg='#f8f8ff')
            nb2.add(frame_Electricity, text='Electricity')
            frame_Electromagnetism = Frame(nb2, width='500',height='700',bg='#f8f8ff')
            nb2.add(frame_Electromagnetism, text='Electromagnetism')
            frame_transformation = Frame(nb2, width='500',height='700',bg='#f8f8ff')
            nb2.add(frame_transformation, text='Transfers')
            #--------------------------------------------------------
            #----------------------------Button----------------------------
            #------------------------------Electricity-----------------
            b1 = Button(frame_Electricity,text='electricWork',command=e1,bg='#537FE7',fg='#E9F8F9',font=2)
            b1.pack(fill=X)
            b2 = Button(frame_Electricity,text='coulomb',command=e2,bg='#537FE7',fg='#E9F8F9',font=2)
            b2.pack(fill=X)
            b3 = Button(frame_Electricity,text='current',command=e3,bg='#537FE7',fg='#E9F8F9',font=2)
            b3.pack(fill=X)
            b4 = Button(frame_Electricity,text='electrical Power',command=e4,bg='#537FE7',fg='#E9F8F9',font=2)
            b4.pack(fill=X)
            b5 = Button(frame_Electricity,text='volt',command=e5,bg='#537FE7',fg='#E9F8F9',font=2)
            b5.pack(fill=X)
            b6 = Button(frame_Electricity,text='Resistance',command=e6,bg='#537FE7',fg='#E9F8F9',font=2)
            b6.pack(fill=X)
            b7 = Button(frame_Electricity,text='conductorResistance',command=e7,bg='#537FE7',fg='#E9F8F9',font=2)
            b7.pack(fill=X)
            b8 = Button(frame_Electricity,text='conductorMaterialType',command=e8,bg='#537FE7',fg='#E9F8F9',font=2)
            b8.pack(fill=X)
            b9 = Button(frame_Electricity,text='electricalConductivity',command=e9,bg='#537FE7',fg='#E9F8F9',font=2)
            b9.pack(fill=X)
            b10 = Button(frame_Electricity,text='capacitor Capacitance',command=e10,bg='#537FE7',fg='#E9F8F9',font=2)
            b10.pack(fill=X)
            b11 = Button(frame_Electricity,text='capacitor Charge',command=e11,bg='#537FE7',fg='#E9F8F9',font=2)
            b11.pack(fill=X)
            b12 = Button(frame_Electricity,text='wave Speed',command=e12,bg='#537FE7',fg='#E9F8F9',font=2)
            b12.pack(fill=X)
            b13 = Button(frame_Electricity,text='electron Volt',command=e13,bg='#537FE7',fg='#E9F8F9',font=2)
            b13.pack(fill=X)
            b14 = Button(frame_Electricity,text='Coulomb Is Law',command=e14,bg='#537FE7',fg='#E9F8F9',font=2)
            b14.pack(fill=X)
            #------------------------------Electromagnetism-----------------
            b15 = Button(frame_Electromagnetism,text='magnetic Field',command=e15,bg='#537FE7',fg='#E9F8F9',font=2)
            b15.pack(fill=X)
            b16 = Button(frame_Electromagnetism,text='magnetic Flux',command=e16,bg='#537FE7',fg='#E9F8F9',font=2)
            b16.pack(fill=X)
            b17 = Button(frame_Electromagnetism,text='magnetic FluxArea',command=e17,bg='#537FE7',fg='#E9F8F9',font=2)
            b17.pack(fill=X)
            b18 = Button(frame_Electromagnetism,text='magnetic Flux Density',command=e18,bg='#537FE7',fg='#E9F8F9',font=2)
            b18.pack(fill=X)
            b19 = Button(frame_Electromagnetism,text='magnetic Field Force',command=e19,bg='#537FE7',fg='#E9F8F9',font=2)
            b19.pack(fill=X)
            b20 = Button(frame_Electromagnetism,text='magnetic Field Force With Theta',command=e20,bg='#537FE7',fg='#E9F8F9',font=2)
            b20.pack(fill=X)
            b21 = Button(frame_Electromagnetism,text='flux Density',command=e21,bg='#537FE7',fg='#E9F8F9',font=2)
            b21.pack(fill=X)
            b22 = Button(frame_Electromagnetism,text='magnetic Moment',command=e22,bg='#537FE7',fg='#E9F8F9',font=2)
            b22.pack(fill=X)
            b23 = Button(frame_Electromagnetism,text='averageElectromotiveForceGeneratedByAChargedCoil',command=e23,bg='#537FE7',fg='#E9F8F9',font=2)
            b23.pack(fill=X)
            b24 = Button(frame_Electromagnetism,text='mutualInduction',command=e24,bg='#537FE7',fg='#E9F8F9',font=2)
            b24.pack(fill=X)
            b25 = Button(frame_Electromagnetism,text='factorAffectingTheInductanceCoefficient',command=e25,bg='#537FE7',fg='#E9F8F9',font=2)
            b25.pack(fill=X)
            #------------------------------transformation-----------------
            b26 = Button(frame_transformation,text='coulombIsEqualToHowManyElectrons',command=e26,bg='#537FE7',fg='#E9F8F9',font=2)
            b26.place(x=1,y=1,width='495')
            b27 = Button(frame_transformation,text='electronsEqualToTheNumberOfCoulombs',command=e27,bg='#537FE7',fg='#E9F8F9',font=2)
            b27.place(x=1,y=30,width='495')
            b28 = Button(frame_transformation,text='conversionFromElectronVoltsToJoules',command=e28,bg='#537FE7',fg='#E9F8F9',font=2)
            b28.place(x=1,y=60,width='495')
            b29 = Button(frame_transformation,text='conversionFromJoulesToElectronVolts',command=e29,bg='#537FE7',fg='#E9F8F9',font=2)
            b29.place(x=1,y=90,width='495')
            #----------------------------------------------------------------------
            d3np.pack()
        ###---------------------------------------ModernPhysics---------------------------------------------

        def functionssetphysics65():
            
            if wr68.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p143 =float(wr68.get())
            q65 =  photonEnergy(p143)
            
            p65.set(q65)

        wr68=StringVar()     
        p65=StringVar()

        photonEnergy1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til65 = Frame(photonEnergy1,width='250',height='1000',bg='#EDEDF5')
        bqit65 = Button(til65,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(photonEnergy1,ew144,p65))
        lw144 = Label(til65,text='frequencie',bg='#EDEDF5',fg='#080808',font=2)    
        ew144 = Entry(til65,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr68)
        aa2a64 = Button(til65,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew144,p65))
        ba65 = Button(til65,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics65)
        la65 =Label(photonEnergy1,text="photonEnergy  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla65 = Label(photonEnergy1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p65)
        popup_menu(ew144,d3np)
        #---------------------------------------------------

        def functionssetphysics66():
            
            if wr69.get() == '' or dr69.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p144 =float(wr69.get())
            p145 =float(dr69.get())
            q66 =  futonSpeed(p144,p145)
            
            p66.set(q66)

        wr69=StringVar() 
        dr69=StringVar()    
        p66=StringVar()


        futonSpeed1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til66 = Frame(futonSpeed1,width='250',height='1000',bg='#EDEDF5')
        bqit66 = Button(til66,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide2(futonSpeed1,ew145,ew146,p66))
        lw145 = Label(til66,text='mass',bg='#EDEDF5',fg='#080808',font=2)    
        ew145 = Entry(til66,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr69)
        lw146 = Label(til66,text='energy',bg='#EDEDF5',fg='#080808',font=2)    
        ew146 = Entry(til66,bg='#f8f8ff',fg='#080808',font=2,textvariable=dr69)
        aa2a65 = Button(til66,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide22(ew145,ew146,p66))
        ba66 = Button(til66,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics66)
        la66 =Label(futonSpeed1,text="futonSpeed  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla66 = Label(futonSpeed1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p66)
        popup_menu(ew145,d3np)
        popup_menu(ew146,d3np)
        #---------------------------------------------------

        def functionssetphysics67():
            
            if wr70.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p146 =float(wr70.get())
            p147 = 300000
            q67 =  LawOfConservationOfMassAndEnergy(p146,p147)
            
            p67.set(q67)

        wr70=StringVar()    
        p67=StringVar()

        LawOfConservationOfMassAndEnergy1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til67 = Frame(LawOfConservationOfMassAndEnergy1,width='250',height='1000',bg='#EDEDF5')
        bqit67 = Button(til67,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(LawOfConservationOfMassAndEnergy1,ew147,p67))
        lw147 = Label(til67,text='mass',bg='#EDEDF5',fg='#080808',font=2)    
        ew147 = Entry(til67,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr70)
        aa2a66 = Button(til67,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew147,p67))
        ba67 = Button(til67,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics67)
        la67 =Label(LawOfConservationOfMassAndEnergy1,text="E  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla67 = Label(LawOfConservationOfMassAndEnergy1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p67)
        popup_menu(ew147,d3np)
        #---------------------------------------------------

        def functionssetphysics68():
            
            if wr71.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p148 =float(wr71.get())
            p149 = 300000
            q68 =  photonMomentum(p148,p149)
            
            p68.set(q68)

        wr71=StringVar()    
        p68=StringVar()

        photonMomentum1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til68 = Frame(photonMomentum1,width='250',height='1000',bg='#EDEDF5')
        bqit68 = Button(til68,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(photonMomentum1,ew148,p68))
        lw148 = Label(til68,text='mass',bg='#EDEDF5',fg='#080808',font=2)    
        ew148 = Entry(til68,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr71)
        aa2a67 = Button(til68,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew148,p68))
        ba68 = Button(til68,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics68)
        la68 =Label(photonMomentum1,text="photonMomentum  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla68 = Label(photonMomentum1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p68)
        popup_menu(ew148,d3np)
        #---------------------------------------------------

        def functionssetphysics69():
            
            if wr72.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p150 =float(wr72.get())
            p151 = 300000
            q69 =  PhotonEnergyInMotion(p150,p151)
            
            p69.set(q69)

        wr72=StringVar()    
        p69=StringVar()

        PhotonEnergyInMotion1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til69 = Frame(PhotonEnergyInMotion1,width='250',height='1000',bg='#EDEDF5')
        bqit69 = Button(til69,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(PhotonEnergyInMotion1,ew149,p69))
        lw149 = Label(til69,text='Energy',bg='#EDEDF5',fg='#080808',font=2)    
        ew149 = Entry(til69,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr72)
        aa2a68 = Button(til69,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew149,p69))
        ba69 = Button(til69,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics69)
        la69 =Label(PhotonEnergyInMotion1,text="PhotonEnergyInMotion  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla69 = Label(PhotonEnergyInMotion1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p69)
        popup_menu(ew149,d3np)
        #---------------------------------------------------

        def functionssetphysics70():
            
            if wr73.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p152 =float(wr73.get())
            q70 =  waveLength(p152)
            
            p70.set(q70)

        wr73=StringVar()    
        p70=StringVar()

        waveLength1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til70 = Frame(waveLength1,width='250',height='1000',bg='#EDEDF5')
        bqit70 = Button(til70,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(waveLength1,ew150,p70))
        lw150 = Label(til70,text='PhotonEnergyInMotion',bg='#EDEDF5',fg='#080808',font=2)    
        ew150 = Entry(til70,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr73)
        aa2a69 = Button(til70,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew150,p70))
        ba70 = Button(til70,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics70)
        la70 =Label(waveLength1,text="λ  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla70 = Label(waveLength1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p70)
        popup_menu(ew150,d3np)
        #----------------------QuantumMechanics------------------
        def m1():
            d3np.add(photonEnergy1, text='photonEnergy')
            til65.place(x=1,y=1)
            bqit65.place(x=1,y=1)
            lw144.place(x=90,y=40)
            ew144.place(x=30,y=80)
            ba65.place(x=30,y=120,width='90')
            aa2a64.place(x=130,y=120,width='90')
            lla65.place(x=430,y=20)
            la65.place(x=300,y=20)
        def m2():
            d3np.add(futonSpeed1, text='futonSpeed')
            til66.place(x=1,y=1)
            bqit66.place(x=1,y=1)
            lw145.place(x=90,y=40)
            ew145.place(x=30,y=80)
            lw146.place(x=90,y=120)
            ew146.place(x=30,y=160)
            ba66.place(x=30,y=200,width='90')
            aa2a65.place(x=130,y=200,width='90')
            lla66.place(x=430,y=20)
            la66.place(x=300,y=20)
        def m3():
            d3np.add(LawOfConservationOfMassAndEnergy1, text='LawOfConservationOfMassAndEnergy')
            til67.place(x=1,y=1)
            bqit67.place(x=1,y=1)
            lw147.place(x=90,y=40)
            ew147.place(x=30,y=80)
            ba67.place(x=30,y=120,width='90')
            aa2a66.place(x=130,y=120,width='90')
            lla67.place(x=430,y=20)
            la67.place(x=300,y=20)
        def m4():
            d3np.add(photonMomentum1, text='photonMomentum')
            til68.place(x=1,y=1)
            bqit68.place(x=1,y=1)
            lw148.place(x=95,y=40)
            ew148.place(x=30,y=80)
            ba68.place(x=30,y=120,width='90')
            aa2a67.place(x=130,y=120,width='90')
            lla68.place(x=430,y=20)
            la68.place(x=300,y=20)
        def m5():
            d3np.add(PhotonEnergyInMotion1, text='PhotonEnergyInMotion')
            til69.place(x=1,y=1)
            bqit69.place(x=1,y=1)
            lw149.place(x=95,y=40)
            ew149.place(x=30,y=80)
            ba69.place(x=30,y=120,width='90')
            aa2a68.place(x=130,y=120,width='90')
            lla69.place(x=500,y=20)
            la69.place(x=300,y=20)
        def m6():
            d3np.add(waveLength1, text='waveLength')
            til70.place(x=1,y=1)
            bqit70.place(x=1,y=1)
            lw150.place(x=40,y=40)
            ew150.place(x=30,y=80)
            ba70.place(x=30,y=120,width='90')
            aa2a69.place(x=130,y=120,width='90')
            lla70.place(x=350,y=20)
            la70.place(x=300,y=20)
        #-------------------
        def ModernPhysics():
            ModernPhysics = Toplevel(home)
            ModernPhysics.geometry("500x700+50+200")
            ModernPhysics.configure(background="#f8f8ff")
            ModernPhysics.resizable(False,False)
            ModernPhysics.title("Modern Physics")
            ModernPhysics.iconbitmap('photo\logo.ico')
            ModernPhysics.protocol("WM_DELETE_WINDOW", lambda: close_window(ModernPhysics))
            l3.config(state='disabled')
            def close_window(window):
                window.destroy()
                l3.config(state='normal')
            #=================================
            nb3 = ttk.Notebook(ModernPhysics)
            nb3.pack()
            frame_QuantumMechanics = Frame(nb3, width='500',height='700',bg='#f8f8ff')
            nb3.add(frame_QuantumMechanics, text='Quantum mechanics')
            frame_Relativity = Frame(nb3, width='500',height='700',bg='#f8f8ff')
            nb3.add(frame_Relativity, text='Relativity')
            #-----------------------------------------
            q1 = Button(frame_QuantumMechanics,text='photon Energy',command=m1,bg='#537FE7',fg='#E9F8F9',font=2)
            q1.pack(fill=X)   
            q2 = Button(frame_QuantumMechanics,text='futon Speed',command=m2,bg='#537FE7',fg='#E9F8F9',font=2)
            q2.pack(fill=X)
            q3 = Button(frame_QuantumMechanics,text='LawOfConservationOfMassAndEnergy',command=m3,bg='#537FE7',fg='#E9F8F9',font=2)
            q3.pack(fill=X)
            q4 = Button(frame_QuantumMechanics,text='photon Momentum',command=m4,bg='#537FE7',fg='#E9F8F9',font=2)
            q4.pack(fill=X)
            q5 = Button(frame_QuantumMechanics,text='PhotonEnergyInMotion',command=m5,bg='#537FE7',fg='#E9F8F9',font=2)
            q5.pack(fill=X)
            q6 = Button(frame_QuantumMechanics,text='wave Length',command=m6,bg='#537FE7',fg='#E9F8F9',font=2)
            q6.pack(fill=X)
            #---------------------------------------------------------
            d3np.pack()
        ####---------------------------------Thermalphysics-------------------------

        def functionssetphysics71():
            
            if wr74.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p153 =float(wr74.get())
            q71 =  ConvertTemperatureFromCelsiusToKelvin(p153)
            
            p71.set(q71)

        wr74=StringVar()    
        p71=StringVar()

        ConvertTemperatureFromCelsiusToKelvin1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til71 = Frame(ConvertTemperatureFromCelsiusToKelvin1,width='250',height='1000',bg='#EDEDF5')
        bqit71 = Button(til71,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(ConvertTemperatureFromCelsiusToKelvin1,ew151,p71))
        lw151 = Label(til71,text='Celsius temperature',bg='#EDEDF5',fg='#080808',font=2)    
        ew151 = Entry(til71,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr74)
        aa2a70 = Button(til71,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew151,p71))
        ba71 = Button(til71,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics71)
        la71 =Label(ConvertTemperatureFromCelsiusToKelvin1,text="TK  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla71 = Label(ConvertTemperatureFromCelsiusToKelvin1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p71)
        popup_menu(ew151,d3np)
        #----------------------------------------------------------

        def functionssetphysics72():
            
            if wr75.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p154 =float(wr75.get())
            q72 =  FinnIslaw(p154)
            
            p72.set(q72)

        wr75=StringVar()    
        p72=StringVar()

        FinnIslaw1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til72 = Frame(FinnIslaw1,width='250',height='1000',bg='#EDEDF5')
        bqit72 = Button(til72,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(FinnIslaw1,ew152,p72))
        lw152 = Label(til72,text='Kelvin Temperature',bg='#EDEDF5',fg='#080808',font=2)    
        ew152 = Entry(til72,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr75)
        aa2a71 = Button(til72,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew152,p72))
        ba72 = Button(til72,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics72)
        la72 =Label(FinnIslaw1,text="λ_max  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla72 = Label(FinnIslaw1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p72)
        popup_menu(ew152,d3np)
        #----------------------------------------------------------

        def functionssetphysics73():
            
            if wr76.get() == '': 
                  messagebox.showinfo("EROR",'Fill the cell')
            p155 =float(wr76.get())
            q73 =  bulbFilamentTemperature(p155)
            
            p73.set(q73)

        wr76=StringVar()    
        p73=StringVar()

        bulbFilamentTemperature1 = Frame(d3np, width='1800',height='1000',bg='#f8f8ff')
        til73 = Frame(bulbFilamentTemperature1,width='250',height='1000',bg='#EDEDF5')
        bqit73 = Button(til73,text='close',bg='#EDEDF5',fg='#ff0000',bd=0,font=2,command=lambda: hide.hide1(bulbFilamentTemperature1,ew153,p73))
        lw153 = Label(til73,text='λ_max',bg='#EDEDF5',fg='#080808',font=2)    
        ew153 = Entry(til73,bg='#f8f8ff',fg='#080808',font=2,textvariable=wr76)
        aa2a72 = Button(til73,text='  Clear  ',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=lambda: hide.hide11(ew153,p73))
        ba73 = Button(til73,text='account',bg='#537FE7',fg='#E9F8F9',bd=0,font=2,command=functionssetphysics73)
        la73 =Label(bulbFilamentTemperature1,text="TK  = ",bg='#f8f8ff',fg='#080808',font=20)
        lla73 = Label(bulbFilamentTemperature1,text="0.0",bg='#f8f8ff',fg='#080808',font=20,textvariable=p73)
        popup_menu(ew153,d3np)
        #----------------------------------------------------------
        def y1():
            d3np.add(ConvertTemperatureFromCelsiusToKelvin1, text='ConvertTemperatureFromCelsiusToKelvin')
            til71.place(x=1,y=1)
            bqit71.place(x=1,y=1)
            lw151.place(x=40,y=40)
            ew151.place(x=30,y=80)
            ba71.place(x=30,y=120,width='90')
            aa2a70.place(x=130,y=120,width='90')
            lla71.place(x=350,y=20)
            la71.place(x=300,y=20)
        def y2():
            d3np.add(FinnIslaw1, text='FinnIslaw')
            til72.place(x=1,y=1)
            bqit72.place(x=1,y=1)
            lw152.place(x=40,y=40)
            ew152.place(x=30,y=80)
            ba72.place(x=30,y=120,width='90')
            aa2a71.place(x=130,y=120,width='90')
            lla72.place(x=380,y=20)
            la72.place(x=300,y=20)
        def y3():
            d3np.add(bulbFilamentTemperature1, text='bulbFilamentTemperature')
            til73.place(x=1,y=1)
            bqit73.place(x=1,y=1)
            lw153.place(x=100,y=40)
            ew153.place(x=30,y=80)
            ba73.place(x=30,y=120,width='90')
            aa2a72.place(x=130,y=120,width='90')
            lla73.place(x=350,y=20)
            la73.place(x=300,y=20)
        #===================
        def Thermalphysics():
            Thermalphysics = Toplevel(home)
            Thermalphysics.geometry("500x700+50+200")
            Thermalphysics.configure(background="#f8f8ff")
            Thermalphysics.resizable(False,False)
            Thermalphysics.title("Thermal Physics")
            Thermalphysics.iconbitmap('photo\logo.ico') 
            Thermalphysics.protocol("WM_DELETE_WINDOW", lambda: close_window(Thermalphysics))
            l4.config(state='disabled')
            def close_window(window):
                window.destroy()
                l4.config(state='normal')
            #---------------------------------------------
            nb4 = ttk.Notebook(Thermalphysics)
            nb4.pack()
            frame_Thermodynamics = Frame(nb4, width='500',height='700',bg='#f8f8ff')
            nb4.add(frame_Thermodynamics, text='Thermodynamics') 
            #---------------------------Thermodynamics-------------------------------
            w1 = Button(frame_Thermodynamics,text='ConvertTemperatureFromCelsiusToKelvin',command=y1,bg='#537FE7',fg='#E9F8F9',font=2)
            w1.place(x=1,y=1,width='495')
            w2 = Button(frame_Thermodynamics,text='FinnIslaw',command=y2,bg='#537FE7',fg='#E9F8F9',font=2)
            w2.place(x=1,y=30,width='495')
            w3 = Button(frame_Thermodynamics,text='bulbFilamentTemperature',command=y3,bg='#537FE7',fg='#E9F8F9',font=2)
            w3.place(x=1,y=60,width='495')
            #------------------------------------------------------------------------
            d3np.pack()
        #########################
        l = Button(wfd, text="Mechanical Physics",font=('Bold',15),bd=0,bg="#DFDFE6",fg='#3F61B0',activebackground='#3F61B0',activeforeground='#E9F8F9',command=MechanicalPhysics)
        l.place(x=20,y= 20)
        l2 = Button(wfd, text="Electro physics",font=('Bold',15),bd=0,bg="#DFDFE6",fg='#3F61B0',activebackground='#3F61B0',activeforeground='#E9F8F9',command=Electrophysics)
        l2.place(x=20,y= 80)
        l3 = Button(wfd, text="Modern Physics",font=('Bold',15),bd=0,bg="#DFDFE6",fg='#3F61B0',activebackground='#3F61B0',activeforeground='#E9F8F9',command=ModernPhysics)
        l3.place(x=20,y= 140)
        l4 = Button(wfd, text="Thermal physics",font=('Bold',15),bd=0,bg="#DFDFE6",fg='#3F61B0',activebackground='#3F61B0',activeforeground='#E9F8F9',command=Thermalphysics)
        l4.place(x=20,y= 200)
