import sqlite3


def create_sqlite_db_users():
    with sqlite3.connect('database/db.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
CREATE TABLE users (id INTEGER PRIMARY KEY, username UNIQUE TEXT, email TEXT, password TEXT, sex TEXT, datetime TEXT)
''')


def example_sqlite_db_users():
    with sqlite3.connect('database/db.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
SELECT * from users;
''')
        rows = cursor.fetchall()
        print(rows)


if __name__ == "__main__":
    # create_sqlite_db_users()
    example_sqlite_db_users()
    pass
