import sqlite3

con = sqlite3.connect("CoddyCoinKepeer.db")
cursor = con.cursor()
# Создать таблицу
# cursor.execute("""CREATE TABLE admins
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 pass TEXT)
#             """)
# Ввести учетные данные
# cursor.execute("INSERT INTO admins (name, pass) VALUES ('admin', 'admin')")
# con.commit()