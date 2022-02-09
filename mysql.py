from dotenv import load_dotenv
from os import getenv
import pymysql

load_dotenv()

def create_db_connection():
    return pymysql.connect(
        host=getenv('DB_HOST'),
        user=getenv('DB_USER'),
        passwd=getenv('DB_PASSWORD'),
        port=int(getenv('DB_PORT')),
        db=getenv('DB_NAME'),
        charset=getenv('DB_CHARSET'))
