from peewee import Model, PostgresqlDatabase
from peewee import PrimaryKeyField, CharField, IntegerField
import os

DB_HOST = os.getenv('DB_HOST')
DB_HOST = '172.21.0.3'
if DB_HOST is None:
    raise ValueError('Cant work with out db_host')
DB_PORT = os.getenv('DB_HOST')
DB_PORT = 5432
if DB_PORT is None:
    raise ValueError('Cant work with out db_port')

database = PostgresqlDatabase(host=DB_HOST, port=5432, user='postgres', password='password', database='postgres')


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
