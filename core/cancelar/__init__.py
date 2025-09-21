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
        with open("tarefas.txt", "w") as arq:
            pass

def apa_unic(tit, tab):
    for w in tab.winfo_children():
        for wid in w.winfo_children():
            try:
                if wid.cget("text") == tit:
                    w.destroy()

                    tarefas = list()
                    abrt = open("tarefas.txt", "r", encoding="UTF-8")
                    for l in abrt:
                        tarefas.append(l.rstrip().split(";"))

                    for n, _ in enumerate(tarefas):
                        if tarefas[n][0] == wid.cget("text"):
                            tarefas.remove(tarefas[n])
                            break
                    
                    abrt2 = open("tarefas.txt", "w", encoding="UTF-8")
                    for _, i in enumerate(tarefas):
                        abrt2.write(f"{i[0]};{i[1]}\n")

                    return
                else:
                    continue
            except:
                continue


