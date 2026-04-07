from peewee import *

db = SqliteDatabase('db.sqlite')


class BaseModel(Model):
    class Meta:
        database = db


class Product(BaseModel):
    name = TextField()
    price = FloatField()
    category = TextField()


def init_db():
    db.connect()
    db.create_tables([Product])

db.connect()