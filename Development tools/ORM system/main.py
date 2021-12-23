# ORM система - позволяет удобно взаимодействовать с БД
# pip intall peewee

# peewee - ORM система. Не поддерживает ассинхронное программирование.

from peewee import * # Импорт всех модулей без отдельного пространства имен

db = SqliteDatabase('example.db')

class User(Model): #Наследуем таблицу от Модели
    id = PrimaryKeyField()
    name = CharField(max_length=20)
    age = IntegerField()
    bio = TextField(null=True)
    gender = BooleanField(null=True)

    class Meta: # Вложенный класс
        database = db # В какой БД работаем
        db_table = 'users' # Название таблицы


with db:
    db.create_tables([User]) # Создаем таблицу согласно описанной модели

    
# DB browser (SQLite only) и Data Grip - программы для работы с БД

# 1ый способ добавления данных в таблицу

user = User(name = 'Ivan', age = 17, bio='Bio', gender = True)
user.save()

# 2ой способ добавления данных в таблицу

User.create(name = 'Gleb', age = 16, bio='Bio', gender = True)

# Для вывода данных в консоль

# response = User.select() # Читаем все данные
# print(response)
# # Работаем, как со списком, чтобы получить данные
# for i in response:
#     print(i.name)

response = User.select().where(User.name == "Ivan").dicts() #Вывод из файла БД
for i in response:
    print(i)


# Удобное взаимодействие с данными

user = User.get(name='Ivan')
print(user.name, user.age)
user.age = 24
user.save()
print(user, type(user))

