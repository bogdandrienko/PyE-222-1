########################################################################################################################
# TODO базы данных

import psycopg2  # postgres
from psycopg2 import Error

# https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
# pandas
# pyodbc (mysql, mssql ...)
# py_ora (oracle)

# SQL - 1950-60 релятивистка (связи) - 1992 г.  - 98%

# CRUD

# Read - чтение(сортировка и фильтрация) из базы
# Create - вставка новых данных
# Delete - удаление строк (по условиям)
# Update - обновление из базы

query1 = """
CREATE TABLE public.buhgalteria
(
    id bigserial NOT NULL,
    name character varying(255) NOT NULL UNIQUE ,
    count bigint DEFAULT 0,
    price double precision DEFAULT 0.0,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.buhgalteria
    OWNER to postgres;
"""

query2 = """
SELECT * FROM public.buhgalteria
ORDER BY id ASC, name DESC;
"""

# чтение всех строк в таблице
"""
SELECT * FROM public.buhgalteria;
"""

# чтение всех строк в таблице с определёнными колонками
"""
SELECT name, price FROM public.buhgalteria;
"""

"""
SELECT * FROM public.buhgalteria
/*

wgerwrgwgrwrgwrgwrg
wgfwgrfwrgfwrgwerg

*/
--where count < 500
;
"""

"""
SELECT count(*) FROM public.buhgalteria
--order by price DESC
where price > 1000
;
"""

"""
SELECT sum(count) -- 2

FROM public.buhgalteria
--order by price DESC
where price > 0 -- 1
;
"""

"""
SELECT name, sum(count), avg(price) FROM public.buhgalteria group by name
"""

# запись 1 строки в таблицу
"""
INSERT INTO public.buhgalteria (name, count, price) VALUES ('бананы', '10', '18000.0');
"""

# запись строк в таблицу
"""
INSERT INTO public.buhgalteria (name, count, price) VALUES ('бананы 1', '10', '18000.0'), ('бананы 2', '10', '18000.0');
"""

# запись строк в таблицу
"""
DELETE FROM public.buhgalteria WHERE name='бананы' and count='10';
"""

# запись строк в таблицу
"""
UPDATE public.buhgalteria SET count = '99', price = price - 500 WHERE name='бананы' and count='0';
"""

"""
INSERT INTO public.buhgalteria_history --2

SELECT * FROM public.buhgalteria where count > 500; --1
"""

def select_all():
    with psycopg2.connect(
            user="postgres",
            password="31284bogdan",
            host="127.0.0.1",
            port="5432",
            database="magazine_by_river"
    ) as connection:
        with connection.cursor() as cursor:
            # cursor.execute("SELECT version();")
            # record = cursor.fetchone()
            cursor.execute("SELECT * FROM public.buhgalteria_history;")
            records = cursor.fetchall()
            print(records)
            for i in records:
                print(i)


select_all()

def insert_one():
    name = "картошка"
    count = 600
    price = 150.5

    list1 = ["картошка", 600, 150.5]

    with psycopg2.connect(
            user="postgres",
            password="31284bogdan",
            host="127.0.0.1",
            port="5432",
            database="magazine_by_river"
    ) as connection:
        with connection.cursor() as cursor:
            # cursor.execute("SELECT version();")
            # record = cursor.fetchone()

            # todo DROP TABLE;
            # cursor.execute("INSERT INTO public.buhgalteria (name) VALUES (:t);", "картошка")  # todo NOT SQL injection
            cursor.execute(f"INSERT INTO public.buhgalteria (name, count, price) VALUES "
                           f"('{name}', '{count}', '{price}');")


# insert_one()


def exc():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                      password="pynative@#29",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
