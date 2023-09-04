from tkinter import *

from CRUD import create

app = Tk()
app.title("Lista")
app.geometry("300x200")
app.configure(bg="#CCCCCC")
display = Entry(app, font="Arial 10 bold")

button = Button(app, text="Adicionar", command=create.ADD())
display.pack()
button.pack(side=TOP)
frame = Frame(app)

frame_lista = Frame(app, pady=5)
frame_lista.pack(side=BOTTOM)

lista = Listbox(frame_lista, width=40)
lista.pack(side=TOP, padx=5)


app.mainloop()
