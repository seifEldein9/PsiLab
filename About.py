import webbrowser as w
from tkinter import*
#----------------------------------------------------------------
class About():
    def About(home):
        def facebook():
            w.open("https://www.facebook.com/PsiLab-117171724639795")
        Abouts = Frame(home,bg='#f8f8ff',width='250',height='700')
        Abouts.place(x=0,y=0)
        Abouts2 = Frame(home,bg='#E3EAFC',width='250',height='700')
        Abouts2.place(x=0,y=0)
        Facebook_Button = Button(Abouts2, text="Facebook",font=('Bold',20),bd=0,bg="#E3EAFC",fg='#3F61B0',activebackground='#3F61B0',activeforeground='#E9F8F9',command=facebook)
        Facebook_Button.place(x=55,y= 130)      
        Aboutstop = Frame(home , bg="#3F61B0",width='250',height='100')
        Aboutstop.place(x=0,y=0)
        textAboutstop = Label(Aboutstop,text='About', bg="#3F61B0",fg='#f8f8ff',font=('Bold',20))
        textAboutstop.place(x=90,y=55)