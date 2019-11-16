from peewee import Model, CharField, IntegerField

from config import DB


class BaseModel(Model):
    class Meta:
        database = DB


class User(BaseModel):
    tg_id = IntegerField()
    username = CharField()


def debug_create_tables():
    DB.create_tables([
        User,
    ])
