# Программа сохраняющая пользователей в БД.
# Сохраняя БД в Volume она сохранится после работы контейнера

from peewee import Model, IntegerField, TextField, SqliteDatabase, PrimaryKeyField
from time import time
database = SqliteDatabase('users.db')


class User(Model):
    id = PrimaryKeyField()
    name = TextField()
    time = IntegerField()

    class Meta:
        database = database
        db_table = 'users'


with database:
    database.create_tables([User])

User.create(name='Gleb', time=time())
User.create(name='Lev', time=time())
for i in range(User.select().count() * 2):
    User.create(name='Peter', time=time())
    
for i in User.select().dicts():
    print(i)

