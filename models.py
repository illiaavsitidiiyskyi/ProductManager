from peewee import *

db = SqliteDatabase('db.sqlite')


class BaseModel(Model):
    class Meta:
        database = db


class Product(BaseModel):
    name = TextField()
    price = FloatField()
    category = TextField()


class Company(BaseModel):
    name = TextField()
    password = TextField()


def init_db():
    db.connect()
    # db.drop_tables([Company])
    db.create_tables([Product, Company])