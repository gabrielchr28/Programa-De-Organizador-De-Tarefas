import customtkinter as ctk
import sqlite3
def add(page: ctk.CTk):
    for wid in page.winfo_children():

        if isinstance(wid, ctk.CTkEntry):

            titulo = wid.get()

        elif isinstance(wid, ctk.CTkTextbox):

            texto = wid.get("0.0", "end")
    else:
        db = sqlite3.connect("tarefas.db")
        cur = db.cursor()
        cur.execute(f"INSERT INTO tarefas VALUES('{titulo}', '{texto}')")
        db.commit()
        db.close