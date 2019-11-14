from peewee import Model, CharField

from config import DB


class BaseModel(Model):
    class Meta:
        database = DB


class User(BaseModel):
    username = CharField()


def debug_create_tables():
    DB.create_tables([
        User,
    ])
