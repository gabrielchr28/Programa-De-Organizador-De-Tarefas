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
    import sqlite3

    db = sqlite3.connect("tarefas.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM tarefas")
    dados = cur.fetchall()
    for i in dados:
        if tit == i[0]:
            return True
    return False
        