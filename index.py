from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#interface

window = Tk()
window.title("Sistema")
window.geometry("600x300")
window.configure(background="white")
window.resizable(width=False,height=False)
window.attributes("-alpha",0.7)
#window.iconbitmap(default="icons/LogoIcon.ico")

#logo = PhotoImage(file="icons/tcc.png")

LeftFrame = Frame(window, width=200, height=300, bg= "#000000", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(window, width=395, height=300, bg= "#000000", relief="raise")
RightFrame.pack(side=RIGHT)

logoLabel = Label(LeftFrame, bg="#000000")
logoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text = "Usuário", font = ("Century Gothic", 20), bg = "#000000", fg = "white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text = "Senha", font = ("Century Gothic", 20), bg = "#000000", fg = "white")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show = "•")
PassEntry.place(x=150, y=160)

#buttons

LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=100, y= 225)

def Register():

    LoginButton.place(x = 5000)
    RegisterButton.place(x = 5000)

    NameLabel = Label(RightFrame, text = "Nome", font = ("Century Gothic", 20), bg = "#000000", fg = "white")
    NameLabel.place(x = 5, y = 5)

    NameEntry = Entry(RightFrame, width = 39)
    NameEntry.place(x = 100, y = 16)

    EmailLabel = Label(RightFrame, text = "E-mail", font = ("Century Gothic", 20), bg = "#000000", fg = "white")
    EmailLabel.place(x = 5, y = 55)

    EmailEntry = Entry(RightFrame, width = 39)
    EmailEntry.place(x = 100, y = 66)

    Register = ttk.Button(RightFrame, text = "Cadastrar", width = 30)
    Register.place(x =100, y = 225)

    def BackToLogin():
        NameLabel.place(x=5000)
        NameEntry.place(x=5000)
        EmailEntry.place(x=5000)
        EmailLabel.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)

        LoginButton.place(x=100)
        RegisterButton.place(x=125)


    Back = ttk.Button(RightFrame, text = "Back", width = 20, command = BackToLogin)
    Back.place(x=125, y= 260)


RegisterButton = ttk.Button(RightFrame, text="Cadastrar", width=20, command = Register)
RegisterButton.place(x=125, y= 260)





window.mainloop()

