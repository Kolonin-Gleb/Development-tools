from peewee import Model, PostgresqlDatabase
from peewee import PrimaryKeyField, CharField, IntegerField
import os

DB_HOST = os.getenv('DB_HOST')
if DB_HOST is None:
    raise ValueError('Cant work with out db_host')
DB_PORT = os.getenv('DB_PORT')
if DB_PORT is None:
    raise ValueError('Cant work with out db_port')
DB_PASSWORD = os.getenv('DB_PASSWORD')
if DB_PASSWORD is None:
    raise ValueError('Cant work with out db_password')
DATABASE = os.getenv('DATABASE')
if DATABASE is None:
    raise ValueError('Cant work with out database')
DB_USER = os.getenv('DB_USER')
if DB_USER is None:
    raise ValueError('Cant work with out db_user')
while 1:
    try:
        database = PostgresqlDatabase(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DATABASE)
        break
    except:
        pass

class User(Model):
    id = PrimaryKeyField()
    name = CharField(max_length=64)
    count = IntegerField(default=1)

    class Meta:
        database = database
        db_table = 'users'


with database:
    database.create_tables([User])

HOST = os.getenv('HOST')
if HOST is None:
    raise ValueError('Cant work without host')
PORT = os.getenv('PORT')
if PORT is None:
    raise ValueError('Cant work without port')
