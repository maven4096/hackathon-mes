import sqlite3
def create_table():
    conn = sqlite3.connect('main/database.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username str, password str)")
    conn.commit()
    conn.close()
def conn_exec(query):
    conn = sqlite3.connect('main/database.db')
    cursor = conn.cursor()
    x = cursor.execute(query)
    y = x.fetchall()
    conn.commit()
    conn.close()
    return y
create_table()