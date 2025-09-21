import customtkinter as ctk # type: ignore
from core.cancelar import canc, apa_td
from core.add import add
from core.add_exist import add_tafs
from core.verificar import verificar_digitados, veri_igu
from core.classes import TarefasClas

app = ctk.CTk()
app.title("Tarefas")
ctk.set_appearance_mode("dark")
larg_janela = 400
altu_janela = 650
larg_tela = app.winfo_screenwidth()
altu_tela = app.winfo_screenheight()
pos_x = int((larg_tela / 2) - (larg_janela / 2))
pos_y = int((altu_tela / 2) - (altu_janela / 2))
app.geometry(f"{larg_janela}x{altu_janela}+{pos_x}+{pos_y}")


def cancelar():
    canc(app)
    entry.focus_set()

def add_event():
    from tkinter import messagebox
    if veri_igu(entry.get()):
        messagebox.showerror("Erro", f'Já existe uma tarefa chamada "{entry.get()}"')
        return
    if len(entry.get()) > 20:
        messagebox.showerror("Erro", "Você pode escrever até 20 caracteres")
        return

    if not verificar_digitados(app):
        messagebox.showerror("Erro", "Você precisa completar todos os campos para continuar")
        return
    add(app)
    TarefasClas(desc=tarefa.get("0.0", "end"), tabview=tabwiew, titulo=entry.get())
    canc(app)
    entry.focus_set()

def apa_td_event():
    from tkinter import messagebox
    if messagebox.askyesno(title="Confirmação", message="Você tem certeza que deseja apagar todas as suas tarefas?"):
        apa_td(tabwiew)
        app.update()
        messagebox.showinfo("Sucesso", "Tarefas apagadas com sucesso.")
    else:
        return

# ENTRY
txt_entry = ctk.CTkLabel(app, text="Título")
txt_entry.grid(padx=10, pady=(10, 0), column=0, row=0, stick="w")

entry = ctk.CTkEntry(app, placeholder_text="Digite o título aqui (1 - 20 caracteres)", width=370, border_color="gray", border_width=1)
entry.grid(padx=10, pady=(1, 10), columnspan=2, row=1)

# TAREFA
txt_tarefa = ctk.CTkLabel(app, text="Sua tarefa")
txt_tarefa.grid(padx=10, pady=(10, 0), column=0, row=2, stick="w")

tarefa = ctk.CTkTextbox(app, width=370, height=100, border_color="gray", border_width=1)
tarefa.grid(padx=10, pady=(1, 10), columnspan=2, row=3, stick="w")

# BOTÕES
btao_canc = ctk.CTkButton(app, text="Cancelar", width=140, border_color="black", border_width=1, fg_color="transparent", command=cancelar)
btao_canc.grid(padx=10, pady=10, column=0, row=4, stick="w")

btao_add = ctk.CTkButton(app, text="Adicionar Tarefa", width=220, border_color="black", border_width=1, command=add_event)
btao_add.grid(padx=10, pady=10, columnspan=2, row=4, stick="e")

btao_apa_td = ctk.CTkButton(app, text="Apagar tudo 🗑", width=100, fg_color="red", hover_color="#b40000", command=apa_td_event)
btao_apa_td.grid(padx=10, pady=10, row=6, column=0, stick="w")

# TABWIEW
tabwiew = ctk.CTkScrollableFrame(app, width=350, height=290)
tabwiew.grid(padx=10, pady=10, row=5, columnspan=2)

# MOSTRAR OS EXISTENTES
add_tafs(tabwiew)




app.mainloop()