import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

query = """
    CREATE TABLE IF NOT EXISTS board(
        'idx' INTEGER PRIMARY KEY AUTOINCREMENT,
        'writer' VARCHAR(100),
        'title' VARCHAR(250),
        'contents' TEXT
    )
"""

cur.execute(query)


#query = "INSERT INTO board ('writer' , 'title' , 'contents') values('홍길동' , '제목' , '작성중')"
#conn.commit()
query = "SELECT 'writer' , 'title' , 'contents' from board"

cur.execute(query)

rows = cur.fetchall()

for row in rows :
    print(row)

conn.close()
