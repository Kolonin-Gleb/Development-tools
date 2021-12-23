import sqlite3 # Драйвер для работы с БД

# conn = sqlite3.connect('example.db')

conn = sqlite3.connect(':memory:') #Для сохранения в оперативную 

cursor = conn.cursor() #Доступ к БД для выполнения команд

# Выполняем SQL команды
cursor.execute('CREATE TABLE users (id int, first_name text)')
cursor.execute('INSERT INTO users VALUES (1, "Ivan")')
cursor.execute('INSERT INTO users VALUES (2, "John")')

cursor.execute('SELECT * FROM users') #Выкидываем данные
print(cursor.fetchall()) # Ловим все данные и чистим данные
print("")

cursor.execute('SELECT * FROM users')
print(cursor.fetchone()) #Ловим 1вые данные
print("")

cursor.executescript("""
    INSERT INTO users VALUES (3, "Bob");
    UPDATE users SET first_name = "Anton" WHERE id = 1;
""")

cursor.execute('SELECT * FROM users') #Выкидываем данные
print(cursor.fetchall()) # Ловим все данные и чистим данные
print("")

name = ''

# Защита от SQL инъекции = экранирование

# cursor.execute('SELECT * FROM users WHERE first_name = ?', (name,))
# cursor.execute('SELECT * FROM users WHERE first_name = :name', (name,))


