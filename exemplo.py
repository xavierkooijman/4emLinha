from tkinter import *
#https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_oval.html

def criar_board():

    i = IntVar()
    j = IntVar()
    for i in range(0,6):
        for j in range(0,7):
            canvas = Canvas(window,width=85,height=85, bg="black")
            canvas.create_oval(20,20,70,70, fill="", outline="white")
            canvas.grid(row=i,column=j)

def jogada(coluna):
        canvas = Canvas(window,width=85,height=85, bg="black")
        canvas.create_oval(20,20,70,70, fill="red", outline="")
        canvas.grid(row=5,column=coluna)

window = Tk()
window.geometry("1200x900")
window.title("4 em linha")
window.configure(bg="black")

coluna = IntVar()

criar_board()

label_coluna = Label(window, text="Coluna(1 a 7): ")
label_coluna.place(x=40,y=600)
entry_coluna = Entry(window, textvariable=coluna)
entry_coluna.place(x=140, y=600)

botao_jogar = Button(window, text="Jogar", width=31, height=5, command=lambda:jogada(coluna))
botao_jogar.place(x=40,y=650)

window.mainloop()