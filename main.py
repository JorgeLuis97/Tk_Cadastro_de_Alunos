from tkinter import messagebox
from tkinter import ttk

from customtkinter import *

# Storage
matriculas = []
index = 0
matricula = 0

app = CTk()
set_appearance_mode("System")
app.title("Matriculas")


# Funções
def atualizartabela() -> None:
    for linha in tabela.get_children():
        tabela.delete(linha)

    for aluno in matriculas:
        tabela.insert("", END, values=(aluno["Matricula"],
                                       aluno["Nome"],
                                       aluno["Curso"],
                                       aluno["Status"]))


def adicionar(matricula_nova: int, matriculas: list) -> None:
    global matricula
    nome = nome_entry.get()
    curso = cb_curso.get()
    status = cb_status.get()
    matricula = matricula_nova
    if nome == "":
        messagebox.showinfo("Erro!",
                            "Nome vazio")
    elif curso == "":
        messagebox.showinfo("Erro!",
                            "Curso Vazio")
    elif status == "":
        messagebox.showinfo("Erro!",
                            "Status Vazio")
    else:
        if matricula in matriculas:
            messagebox.showinfo("Erro!", "Matricula já existe")
            matricula += 1
        else:
            matricula += 1
            aluno = {
                "Matricula": matricula,
                "Nome": nome,
                "Curso": curso,
                "Status": status
            }
            matriculas.append(aluno)
            atualizartabela()
            limparcampos()
            messagebox.showinfo("SUCESSO!!",
                                "Adicionado com Sucesso!")


def limparcampos():
    nome_entry.delete(0, END)
    cb_curso.set("")
    cb_status.set("")


def listaclique(event) -> None:
    selecionar = tabela.selection()
    global index
    index = tabela.index(selecionar[0])
    aluno = matriculas[index]
    limparcampos()
    nome_entry.insert(0, aluno['Nome'])
    cb_curso.insert(0, aluno['Curso'])
    cb_status.insert(0, aluno['Status'])


def editaraluno():
    matriculas[index] = {
        "Nome": nome_entry,
        "Curso": cb_curso,
        "Status": cb_status
    }
    limparcampos()
    atualizartabela()
    messagebox.showinfo("Sucesso!",
                        "Alteração realizada com sucesso!")


# Frames
registro_frame = CTkFrame(master=app, width=475, height=55)
registro_frame.grid(pady=8)

# Labels
nome_label = CTkLabel(master=registro_frame, text="Nome:", font=("Tahoma", 12))
nome_label.grid(row=0, columns=1)

curso_label = CTkLabel(master=registro_frame, text="Curso:", font=("Tahoma", 12))
curso_label.grid(row=0, column=2)

status_label = CTkLabel(master=registro_frame, text="Status:", font=("Tahoma", 12))
status_label.grid(row=0, column=3)

# Tabela
colunas = ["Matricula", "Nome", "Curso", "Status"]
tabela = ttk.Treeview(app, columns=colunas, show="headings")
for colunas in colunas:
    tabela.heading(colunas, text=colunas)

tabela.grid(pady=8, padx=8)
tabela.bind("<ButtonRelease-1>", listaclique)

# Entry
nome_entry = CTkEntry(master=registro_frame, font=("Tahoma", 10), height=18, corner_radius=0)
nome_entry.grid(row=1, columns=1, padx=5)

# combobox
categorias = ["Java", "Python(Ciencia de Dados)", "Delphi 10", "JavaScript", "React"]
cb_curso = ttk.Combobox(registro_frame, values=categorias, font=("Tahoma", 10))
cb_curso.grid(row=1, column=2, padx=5)

categorias_status = ["Não iniciado", "Em andamento", "Finalizado", "Cancelado"]
cb_status = ttk.Combobox(master=registro_frame, values=categorias_status, font=("Tahoma", 10))
cb_status.grid(row=1, column=3, padx=5)

cb_curso.set("")
cb_status.set("")

# Button
adicionar_botao = CTkButton(master=registro_frame, text="Adicionar", width=130,
                            command=lambda: adicionar(matricula, matriculas), hover=True,
                            hover_color=("#DB3E39", "#821D1A"))
adicionar_botao.grid(row=2, columns=1, pady=8)

editar_botao = CTkButton(master=registro_frame, text="Editar", width=130,
                         hover=True,
                         hover_color=("#DB3E39", "#821D1A"),
                         command=lambda: editaraluno())
editar_botao.grid(row=2, columns=4, pady=8)

app.mainloop()
