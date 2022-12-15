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

window = Tk()
window.geometry("1200x900")
window.title("4 em linha")
window.configure(bg="black")

criar_board()

label_linha = Label(window, text="Linha: ")
label_linha.place(x=40,y=600)
entry_linha = Entry(window)
entry_linha.place(x=100, y=600)
label_coluna = Label(window, text="Coluna: ")
label_coluna.place(x=40,y=650)
entry_coluna = Entry(window)
entry_coluna.place(x=100, y=650)



window.mainloop()