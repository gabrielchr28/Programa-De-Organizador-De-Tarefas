from core.classes import TarefasClas
def add_tafs(tabwiew):
    
    abrt = open("tarefas.txt", "rt", encoding="UTF-8")

    try:
        for n, i in enumerate(abrt):
            sep = i.rstrip()
            sep = sep.split(";")
            
            TarefasClas(desc=sep[1], titulo=sep[0], tabview=tabwiew)
    except IndexError:
        return