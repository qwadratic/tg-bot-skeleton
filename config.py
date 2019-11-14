import os
import dotenv
from peewee import SqliteDatabase, PostgresqlDatabase

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

dotenv.load_dotenv(
    os.path.join(BASE_DIR, '.env')
)

IS_DEBUG = True if os.environ.get('DEBUG') == '1' else False

TG_TOKEN = os.environ.get('TG_TOKEN_DEV') if IS_DEBUG else os.environ.get('TG_TOKEN')

SQLITE_NAME = 'test.db'
POSTGRES_CONFIG = {
    'host': 'localhost',
    'database': 'bot',
    'user': 'bot'
}
DB = SqliteDatabase(SQLITE_NAME) if IS_DEBUG else PostgresqlDatabase(**POSTGRES_CONFIG)
