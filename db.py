# db.py
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("HOST_DB"),
        user=os.getenv("USER_DB"),
        password=os.getenv("PASSWORD_DB"),
        database=os.getenv("DATABASE_DB")
    )
