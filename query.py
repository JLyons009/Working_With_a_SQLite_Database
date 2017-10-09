import sqlite3


conn = sqlite3.connect('factbook.db')
print(conn.execute('SELECT name, population FROM facts WHERE population != \'None\' ORDER BY population ASC;').fetchmany(10))
conn.close()