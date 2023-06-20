import aiohttp
import asyncio


def test_create_new_post():
    async def test():
        async with aiohttp.ClientSession() as session:
            data = {"title": "TEST", "description": "TEST"}
            async with session.post("http://127.0.0.1:8000/create", data=data) as response:
                print(response)

    asyncio.run(test())


if __name__ == "__main__":
    test_create_new_post()
    pass
