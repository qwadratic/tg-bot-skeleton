import os
import dotenv
from peewee import SqliteDatabase, PostgresqlDatabase

dotenv.load_dotenv()

IS_DEBUG = True if os.environ.get('DEBUG') == '1' else False

TG_TOKEN = os.environ.get('TG_TOKEN_DEV') if IS_DEBUG else os.environ.get('TG_TOKEN')

SQLITE_NAME = 'test.db'
POSTGRES_CONFIG = {
    'host': 'localhost',
    'database': 'bot',
    'user': 'bot'
}
DB = SqliteDatabase(SQLITE_NAME) if IS_DEBUG else PostgresqlDatabase(**POSTGRES_CONFIG)

MINTER_NODE_API_URL = 'https://mnt.funfasy.dev/v0/'
MINTER_NODE_API_HEADERS = {
    'X-Project-Id': 'af76c7ba-1631-4810-b677-79b4317324db',
    'X-Project-Secret': os.environ.get('FUNFASY_PROJECT_SECRET')
}
