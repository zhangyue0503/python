import sqlite3

def convert(value):
    if value.startswith('-'):
        return value.strip('-')
    if not value:
        value = 0
    return float(value)

conn = sqlite3.connect('food.db')
curs = conn.cursor()

# curs.execute('''
# CREATE TABLE food(
# id  TEXT  PRIMARY KEY,
# desc  TEXT,
# water FLOAT,
# kcal  FLOAT
# )
# ''')

# query = "INSERT INTO food values(1,'aaa','bbb','ccc')"
# curs.execute(query)

query = 'select * from food'
print query

curs.execute(query)
for row in curs.fetchall():
    print row[1]

conn.commit()

conn.close()