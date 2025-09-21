def add(page):
    import customtkinter as ctk
    from tkinter import messagebox
    erro = False
    for wid in page.winfo_children():

        if isinstance(wid, ctk.CTkEntry):

            titulo = wid.get()

        elif isinstance(wid, ctk.CTkTextbox):

            texto = wid.get("0.0", "end")
    else:
        with open("tarefas.txt", "a", encoding="UTF-8") as taf:

            taf.write(f"{titulo};{texto}")