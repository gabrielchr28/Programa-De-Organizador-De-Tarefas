import sqlite3

db = sqlite3.connect("tarefas.db")

cur = db.cursor()

cur.execute("CREATE TABLE tarefas (titulo TEXT NOT NULL, descricao TEXT NOT NULL)")

db.close()