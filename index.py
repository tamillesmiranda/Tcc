from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#interface

window = Tk()
window.title("Sistema")
window.geometry("600x300")
window.configure(background="white")
window.resizable(width=False,height=False)

#logo = PhotoImage(file="icons/tcc.png")

LeftFrame = Frame(window, width=200, height=300, bg= "#D5EDF2", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(window, width=395, height=300, bg= "#D5EDF2", relief="raise")
RightFrame.pack(side=RIGHT)

logoLabel = Label(LeftFrame, bg="#D5EDF2")
logoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text = "Usuário:", font = ("Century Gothic", 20), bg = "#D5EDF2", fg = "black")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text = "Senha:", font = ("Century Gothic", 20), bg = "#D5EDF2", fg = "black")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30)
PassEntry.place(x=150, y=160)



window.mainloop()

