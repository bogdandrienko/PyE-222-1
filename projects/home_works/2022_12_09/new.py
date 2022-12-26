import requests
import json

########################################################################################################################
# TODO 1

# url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(url=url)
# result = response.json()  # JSON -> dict(Python)
# with open(f"data/new.json", mode="w") as file_object:
#     json.dump(result, file_object)

########################################################################################################################
# TODO 2



# def download(num):
#     url = f"https://jsonplaceholder.typicode.com/todos/{num}"
#     response = requests.get(url=url)
#     result = response.json()  # JSON -> dict(Python)
#     with open(f"data/new{num}.json", mode="w") as file_object:
#         json.dump(result, file_object)
#
#
# for num in range(1, 50 + 1):
#     download(num=num)

########################################################################################################################
# TODO 3

# import threading
#
#
# def download(num):
#     url = f"https://jsonplaceholder.typicode.com/todos/{num}"
#     response = requests.get(url=url)
#     result = response.json()  # JSON -> dict(Python)
#     with open(f"data/new{num}.json", mode="w") as file_object:
#         json.dump(result, file_object)
#
#
# thread_list = []
# for num in range(1, 50 + 1):
#     thread_list.append(threading.Thread(target=download, args=(num,)))
#
# for i in thread_list:
#     i.start()

########################################################################################################################
# TODO 4

# import multiprocessing
#
#
# def download(num):
#     url = f"https://jsonplaceholder.typicode.com/todos/{num}"
#     response = requests.get(url=url)
#     result = response.json()  # JSON -> dict(Python)
#     with open(f"data/new{num}.json", mode="w") as file_object:
#         json.dump(result, file_object)
#
#
# if __name__ == '__main__':
#     process_list = []
#     for num in range(1, 50 + 1):
#         process_list.append(multiprocessing.Process(target=download, args=(num,)))
#
#     for i in process_list:
#         i.start()

########################################################################################################################
# TODO 5

# import asyncio  # асинхронность
# import aiohttp  # TODO асинхронные веб-запросы
#
#
# async def async_download(num: int) -> None:
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url=f"https://jsonplaceholder.typicode.com/todos/{num}") as response_instance:
#             response = await response_instance.json()
#             with open(f"data/new{num}.json", mode="w") as file_object:
#                 json.dump(response, file_object)
#
#
# if __name__ == '__main__':
#     async def start():
#         return await asyncio.gather(*[async_download(num) for num in range(1, 50 + 1)])
#
#     asyncio.run(start())

########################################################################################################################
