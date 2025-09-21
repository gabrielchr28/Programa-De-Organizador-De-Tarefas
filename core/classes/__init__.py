import customtkinter as ctk # type: ignore
from PIL import Image # type: ignore
from core.cancelar import apa_unic

seta_d = ctk.CTkImage(light_image=Image.open("core\\imgs\\seta-direita.png"), size=(15,15))
seta_b = ctk.CTkImage(light_image=Image.open("core\\imgs\\seta-baixo.png"), size=(15,15))

class TarefasClas:
    def __init__(self, titulo, desc, tabview):

        self.clicado = False
        def btao_event():
            if self.clicado:
                self.desc.pack_forget()
                self.apa.pack_forget()
                self.titulo.configure(image=seta_d)
                self.clicado = False
            else:
                self.desc.pack(padx=10, pady=(1, 10), anchor="w")
                self.apa.pack(padx=10, pady=(0, 3), anchor="w")
                self.titulo.configure(image=seta_b)
                self.clicado = True
        
        def apa():
            from tkinter import messagebox
            if messagebox.askyesno("Confirmação", "Você tem certeza que deseja apagar a sua tarefa?"):
                apa_unic(titulo, tabview)
                messagebox.showinfo("Sucesso", "Tarefa apagada com sucesso.")
            else:
                return

        frame = ctk.CTkFrame(tabview, width=340, fg_color="gray")
        self.titulo = ctk.CTkButton(frame, text=titulo, fg_color="transparent", hover_color="gray", anchor="w", font=(None, 20), image=seta_d, compound="right", command=btao_event)
        self.apa = ctk.CTkButton(frame, width=30, height=25, text="Apagar 🗑", fg_color="red", hover_color="#b40000", command=apa)
        self.desc = ctk.CTkLabel(frame, text=desc, wraplength=330)

        frame.pack(padx=10, pady=10, anchor="center", fill="both")
        self.titulo.pack(padx=10, pady=10, anchor="w", fill="x")

    

