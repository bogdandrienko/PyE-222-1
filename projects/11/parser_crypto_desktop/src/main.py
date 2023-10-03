import asyncio
import json
import time
import concurrent.futures
import requests
import aiohttp
from bs4 import BeautifulSoup


class Valute:
    def __init__(self, name: str, symbol: str, priceUSD: str, capitalize: float):
        self.name = name
        self.symbol = symbol
        self.priceUSD = float(str(priceUSD)[1:].replace(',', ''))
        self.capitalize = capitalize

    def __repr__(self):
        return f"<Valute {self.name} {self.priceUSD}>"

    def to_json(self):
        return json.dumps({"name": self.name, "symbol": self.symbol, "price": self.priceUSD, "active": True})


async def async_request(url: str, headers: dict) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as response:
            data = await response.read()
            return data.decode('utf-8')


class View:
    @staticmethod
    def calculate_o(mat: list) -> Valute:
        val = Valute(name=mat[1], symbol=mat[2], priceUSD=mat[3], capitalize=mat[8])
        time.sleep(2.0)
        # print(val)
        return val

    @staticmethod
    def calculate_m(matrix: list[list], workers: int = (8 * 2 + 1) * 2) -> list[Valute]:
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            # future = executor.submit(View.calculate_o, 10)  # обещание
            # result = future.result()  # требуем результат

            futures = []
            for i in matrix:
                futures.append(executor.submit(View.calculate_o, i))
            # futures = [executor.submit(View.calculate_o, i) for i in matrix]

            results = []
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())
            # results = [i.result() for i in concurrent.futures.as_completed(futures)]

            return results


async def get_valutes() -> list[Valute]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    url = "https://www.coingecko.com/"

    # получение ответа в формате str
    response = await async_request(url=url, headers=headers)
    # парсинг ответа в объект BeautifulSoup
    soup = BeautifulSoup(response, 'html.parser')
    # взятие первого тэга "tbody",
    tbody = soup.find('tbody')
    # разделение всего текста на блоки
    lines = tbody.text.split("\n")
    clear_lines = []
    for i in lines:
        if str(i).strip() != "" and str(i).strip() != "Buy":
            clear_lines.append(i)

    matrix = []  # чужая песочница
    local_elems = []  # ведёрко
    index = 0  # количество лопаток(счётчик)
    for i in clear_lines:  # наша песочница
        # опускаем лопатку с песком в ведёрко
        local_elems.append(i)
        index += 1
        # проверям наполнено ли ведёрко
        if index >= 11:
            # тащим ведёрко в чужую песочницу
            matrix.append(local_elems)
            # обнуляем ведёрко
            local_elems = []
            index = 0
    # for i in matrix:
    #     print(i)
    valutes: list[Valute] = View.calculate_m(matrix=matrix, workers=50)
    print(valutes)

    # simple filtration
    # new_valutes = []
    # for i in valutes:
    #     if i.priceUSD > 1000:
    #         new_valutes.append(i)
    # print(len(new_valutes), new_valutes)

    # complex filtration
    new_valutes = list(filter(lambda x: x.priceUSD > 1000, valutes))
    new_valutes = sorted(new_valutes, key=lambda x: x.priceUSD, reverse=True)
    print(new_valutes)



if __name__ == '__main__':
    asyncio.run(get_valutes())
