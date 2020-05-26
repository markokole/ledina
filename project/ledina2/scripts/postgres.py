import psycopg2
import os
host = os.getenv('POSTGRES_HOST')
database = os.getenv('POSTGRES_DB')
password = os.getenv('POSTGRES_PASSWORD')
conn = psycopg2.connect(host=host,database=database, user="postgres", password=password)
cur = conn.cursor()
cur.execute('SELECT version()')
db_version = cur.fetchone()
print(db_version)