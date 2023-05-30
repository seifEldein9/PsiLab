from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import time
from tkinter import ttk
from main import*
w=Tk()

width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1) 

q = Frame(w, width=425, height=250, bg='#3F61B0').place(x=0,y=0)
label1=Label(w, text='PsiLab', fg='#f8f8ff', bg='#3F61B0')  
label1.configure(font=("Game Of Squids", 28, "bold"))   
label1.place(x=170,y=90)

ffd = PhotoImage(file="photo\logo-02-04.png")
ewwd42 = Label(q,bg='#3F61B0',fg='#f8f8ff',font=2,height=50,width=50)
ewwd42.place(x=110,y=80)
ewwd42.config(image = ffd)

label2=Label(w, text='Loading...', fg='#f8f8ff', bg='#3F61B0') 
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

image_a=ImageTk.PhotoImage(Image.open('photo\c2.png'))
image_b=ImageTk.PhotoImage(Image.open('photo\c1.png'))


for i in range(5): 
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)



w.destroy()
new_win()
w.mainloop()