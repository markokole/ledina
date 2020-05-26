import os
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.errors import DuplicateDatabase

host = os.getenv('POSTGRES_HOST')
database = os.getenv('POSTGRES_DB')
password = os.getenv('POSTGRES_PASSWORD')

def run():
    con = psycopg2.connect(dbname='postgres',
        user='postgres', host=host,
        password=password)

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()

    # Use the psycopg2.sql module instead of string concatenation
    # in order to avoid sql injection attacs.
    try:
        cur.execute(sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(database))
            )
    except DuplicateDatabase:
        print("{} already exists!".format(database))
