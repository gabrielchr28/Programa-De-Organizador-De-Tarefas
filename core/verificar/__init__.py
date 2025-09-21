def verificar_digitados(pagina):
    import customtkinter as ctk # type: ignore

    for w in pagina.winfo_children():
        
        if isinstance(w, ctk.CTkEntry):

            if len(w.get()) == 0:
                return False
            
            continue
            
        elif isinstance(w, ctk.CTkTextbox):

            if len(w.get('0.0', 'end')) == 1:
                return False
            
            continue
    return True

def veri_igu(tit):

    abrt = open("tarefas.txt", "r", encoding="UTF-8")

    for l in abrt:
        taf = l.rstrip().split(";")
        
        if taf[0] == tit:
            return True
    return False
