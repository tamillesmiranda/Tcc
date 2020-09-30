import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#interface

window = Tk()
window.title("Sistema")
window.geometry("1200x900")
window.configure(background="white")
window.resizable(width=False,height=False)
window.attributes("-alpha",0.8)
#window.iconbitmap(default="icons/LogoIcon.ico")

#logo = PhotoImage(file="icons/tcc.png")

LeftFrame = Frame(window, width=1100, height=860, bg= "#000000", relief="raise")
LeftFrame.pack(side=TOP)

UserLabel = Label(LeftFrame, text = "Usuário", font = ("Century Gothic", 20), bg = "#000000", fg = "white")
UserLabel.place(x=500, y=100)

UserEntry = ttk.Entry(LeftFrame, width=30)
UserEntry.place(x=450, y=150)

PassLabel = Label(LeftFrame, text = "Senha", font = ("Century Gothic", 20), bg = "#000000", fg = "white")
PassLabel.place(x=500, y=200)

PassEntry = ttk.Entry(LeftFrame, width=30, show = "•")
PassEntry.place(x=450, y=250)


#buttons

LoginButton = ttk.Button(LeftFrame, text="Login", width=29)
LoginButton.place(x=450, y= 325)

def Register():
    #oculta label
    LoginButton.place(x = 5000)
    RegisterButton.place(x = 5000)
    UserLabel.place(x=5000)
    UserEntry.place(x=5000)
    PassLabel.place(x=5000)
    PassEntry.place(x=5000)

    #dados pessoais
    DadosLabel = Label(LeftFrame,text = "Informações Pessoais", font = ("Century Gothic", 18), bg = "#000000", fg = "white")
    DadosLabel.place(x = 450, y = 5)

    NameLabel = Label(LeftFrame,text = "Nome", font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    NameLabel.place(x = 280, y = 40)

    NameEntry = Entry(LeftFrame, width = 39,font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    NameEntry.place(x = 350, y = 40)

    RgLabel = Label(LeftFrame, text = "RG", font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    RgLabel.place(x = 300, y = 70)

    RgEntry = Entry(LeftFrame, width = 39,font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    RgEntry.place(x = 350, y = 70)

    CPFLabel = Label(LeftFrame, text = "CPF", font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    CPFLabel.place(x = 295, y = 100)

    CPFEntry = Entry(LeftFrame, width = 39,font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    CPFEntry.place(x = 350, y = 100) 

    RuaLabel = Label(LeftFrame, text = "Rua", font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    RuaLabel.place(x = 295, y = 130)

    RuaEntry = Entry(LeftFrame, width = 20,font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    RuaEntry.place(x = 350, y = 130)  

    nLabel = Label(LeftFrame, text = "N°", font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    nLabel.place(x = 620, y = 130)

    nEntry = Entry(LeftFrame, width = 11,font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    nEntry.place(x = 659, y = 130)

    compLabel = Label(LeftFrame, text = "Complemento", font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    compLabel.place(x = 200, y = 160)

    compEntry = Entry(LeftFrame, width = 20,font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    compEntry.place(x = 350, y = 160)  

    cepLabel = Label(LeftFrame, text = "CEP", font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    cepLabel.place(x = 610, y = 160)

    cepEntry = Entry(LeftFrame, width = 11,font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    cepEntry.place(x = 659, y = 160)  

    cityLabel = Label(LeftFrame, text = "Cidade", font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    cityLabel.place(x = 270, y = 190)

    cityEntry = Entry(LeftFrame, width = 12,font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    cityEntry.place(x = 350, y = 190)  

    ufLabel = Label(LeftFrame, text = "UF", width = 20,font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    ufLabel.place(x = 515, y = 190)

    ufEntry = ttk.Combobox(LeftFrame, width = 5,font = ("Century Gothic", 15), values =["AC", "AL","AP","AM","BA","CE","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO","DF"])
    ufEntry.place(x = 670, y = 190)      

     #dados financeiros
    CtLabel = Label(LeftFrame,text = "Informações Financeiras", font = ("Century Gothic", 18), bg = "#000000", fg = "white")
    CtLabel.place(x = 450, y = 260) 

    NcLabel = Label(LeftFrame,text = "N° do Cartão", font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    NcLabel.place(x = 200, y = 300)

    NcEntry = Entry(LeftFrame, width = 39,font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    NcEntry.place(x = 350, y = 300)

    NamecLabel = Label(LeftFrame,text = "Nome", font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    NamecLabel.place(x = 200, y = 300)

    NamecEntry = Entry(LeftFrame, width = 39,font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    NamecEntry.place(x = 350, y = 300)

    #EmailLabel = Label(LeftFrame, text = "E-mail", font = ("Century Gothic", 15), bg = "#000000", fg = "white")
    #EmailLabel.place(x = 5, y = 100)

    #EmailEntry = Entry(LeftFrame, width = 39)
    #EmailEntry.place(x = 100, y = 100)

    Register = ttk.Button(LeftFrame, text = "Salvar", width = 20)
    Register.place(x =950, y = 800)

    def BackToLogin():
        #oculta
        NameLabel.place(x=5000)
        NameEntry.place(x=5000)
        EmailEntry.place(x=5000)
        EmailLabel.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)


        LoginButton.place(x=100)
        RegisterButton.place(x=125)


    Back = ttk.Button(LeftFrame, text = "Voltar", width = 20, command = BackToLogin)
    Back.place(x=20, y= 800)


RegisterButton = ttk.Button(LeftFrame, text="Cadastrar", width=20, command = Register)
RegisterButton.place(x=476, y= 380)





window.mainloop()

