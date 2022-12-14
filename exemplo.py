from tkinter import *
#https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_oval.html

window = Tk()
window.geometry("1200x900")
window.title("4 em linha")
window.configure(bg="black")

botao_circular_imagem = PhotoImage(file="circulo_vermelho.ppm")

img_label = Label(image=botao_circular_imagem)

butao_circular = Button(window, image=botao_circular_imagem, borderwidth=0)
butao_circular.pack(pady=30)

window.mainloop()