from peewee import Model, SqliteDatabase
from peewee import PrimaryKeyField, CharField, IntegerField

database = SqliteDatabase('/etc/db/web_site.db')


class User(Model):
    id = PrimaryKeyField()
    name = CharField(max_length=64)
    count = IntegerField(default=1)

    class Meta:
        database = database
        db_table = 'users'


with database:
    database.create_tables([User])
