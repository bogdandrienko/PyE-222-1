import psycopg2
import sqlite3


def db_query_postgres(query: str, args=(), many=True) -> tuple | list[tuple] | None:
    """
    Универсальная функция для запросов в базу данных

    :param query: SQL-запрос
    :param args: Аргументы, которые можно "пробросить" в запрос (!= sql injection)
    :param many: Много ли строк возвращается?
    :return: Если надо, возвращаются данные из запроса
    """

    with psycopg2.connect("dbname='flask_db' user='postgres' host='127.0.0.1' password='31284bogdan'") as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        try:
            if many:
                # todo Read many
                return cursor.fetchall()
            # todo Read one
            return cursor.fetchone()
        except Exception as error:
            # todo Create
            # todo Update
            # todo Delete
            return None


def db_query_sqlite(query: str, args=(), many=True) -> tuple | list[tuple] | None:
    """
    Универсальная функция для запросов в базу данных

    :param query: SQL-запрос
    :param args: Аргументы, которые можно "пробросить" в запрос (!= sql injection)
    :param many: Много ли строк возвращается?
    :return: Если надо, возвращаются данные из запроса
    """
    with sqlite3.connect('database/database.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        try:
            if many:
                # todo Read many
                return cursor.fetchall()
            # todo Read one
            return cursor.fetchone()
        except Exception as error:
            # todo Create
            # todo Update
            # todo Delete
            return None


def sqlite_create_posts_db():
    with sqlite3.connect('database/database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
CREATE TABLE IF NOT EXISTS posts
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
author TEXT,
title TEXT,
description TEXT,
datetime TEXT DEFAULT CURRENT_TIMESTAMP
)
''')
