def canc(page):
    import customtkinter as ctk # type: ignore

    for wid in page.winfo_children():

        if isinstance(wid, ctk.CTkEntry):
            wid.delete(0, "end")

        if isinstance(wid, ctk.CTkTextbox):
            wid.delete("0.0", "end")

def apa_td(tabview):
    for i in tabview.winfo_children():
        i.destroy()
    import sqlite3
    db = sqlite3.connect("tarefas.db")
    cur = db.cursor()
    cur.execute("DELETE FROM tarefas")
    db.commit()
    db.close()

def apa_unic(tit, tab):
    for w in tab.winfo_children():
        for wid in w.winfo_children():
            try:
                if wid.cget("text") == tit:
                    w.destroy()

                    import sqlite3
                    db = sqlite3.connect("tarefas.db")
                    cur = db.cursor()
                    cur.execute(f"DELETE FROM tarefas WHERE titulo = ?;", (tit,))
                    db.commit()
                    db.close()

                    return
                else:
                    continue
            except:
                continue


