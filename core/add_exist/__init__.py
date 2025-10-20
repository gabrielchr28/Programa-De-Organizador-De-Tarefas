from core.classes import TarefasClas
import sqlite3
def add_tafs(tabwiew):
    
    db = sqlite3.connect("tarefas.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM tarefas")
    dados = cur.fetchall()
    db.close()

    try:
        for i in dados:
            TarefasClas(desc=i[1], titulo=i[0], tabview=tabwiew)
    except IndexError:
        return