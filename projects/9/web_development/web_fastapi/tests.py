import sqlite3

import aiohttp
import asyncio


def test_create_new_post():
    async def test():
        async with aiohttp.ClientSession() as session:
            data = {"title": "TEST", "description": "TEST"}
            async with session.post("http://127.0.0.1:8000/create", data=data) as response:
                print(response)

    asyncio.run(test())


def test_comments():
    with sqlite3.connect('database/database.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM post_comments""")
        data = cursor.fetchall()
        print(len(data), data)


if __name__ == "__main__":
    # test_create_new_post()
    test_comments()
    pass
