from sanic import Sanic, Request
from sanic_ext import render
import aiofiles
from sanic import json

# sanic main:app --host=0.0.0.0 --port=8001 --fast

app = Sanic("MyHelloWorldApp")


@app.get("/api/data/")  # URL
async def f_data(request: Request):  # VIEW

    # todo SYNC
    # with open("data.txt", mode="r", encoding="utf-8") as file:
    #     data = [x.strip() for x in file.readlines()]
    # todo SYNC

    # todo ASYNC
    async with aiofiles.open('data.txt', mode='r', encoding="utf-8") as file:
        data = [x.strip() for x in await file.readlines()]
    # todo ASYNC

    return json(data, status=200)


@app.get("/")  # URL
async def handler(request: Request):  # VIEW
    names = ["Инна", "Ольа", "Юля"]  # MODEL (база данных)
    return await render("index.html", context={"names": names}, status=200)  # TEMPLATE


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8001,
        debug=True,
        auto_reload=True
    )
