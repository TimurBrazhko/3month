import sqlite3 as sq
from db import queries

db = sq.connect('db/db.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print("BAZA DANNIH SQLITE3 PODKL")
    cursor.execute(queries.CREATE_TABLE_REGISTRATION)
    db.commit()


async def sql_insert_registration(telegram_id, firstname):
    cursor.execute(queries.INSERT_INTO_TABLE_REGISTRATION, (
        telegram_id, firstname)
                   )
    db.commit()
