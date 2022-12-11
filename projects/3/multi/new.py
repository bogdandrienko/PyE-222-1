import random

import requests  # sync
import time
import threading
import multiprocessing
import asyncio  # встроена в Python
import aiohttp  # async

# последовательно sync =                1 процесс: 1 поток
# многопоточно threading =              1 процесс: N поток
# мультипроцессорно multiprocessing =   N процесс: N поток
# асинхронно (параллельно) async =      1 процесс: 1 поток

# мы поставили чайник, и не жарим яйца, пока чайник не закипит
# мы одновременно следим то за чайником, то за яйцами на плите
# мы зовём ещё человека, жарить яйца
# мы одновременно следим то за чайником, то за яйцами на плите

url3 = "https://picsum.photos/600/600/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def sync_download_image():
    time.sleep(0.5)

    response = requests.get(url=url3, headers=headers)
    with open(f"images/new{random.randint(1, 100000000)}.jpg", "wb") as f:
        f.write(response.content)


async def async_download_image():
    async with aiohttp.ClientSession() as session:  # разговора
        async with session.get(url=url3, headers=headers) as response_obj:  # вопросы
            data = await response_obj.read()
            with open(f"images/new{random.randint(1, 100000000)}.jpg", "wb") as f:
                f.write(data)


def sync_mass_download_images():
    start = time.perf_counter()

    # sync_download_image(1)
    # sync_download_image(2)
    # sync_download_image(3)

    for i in range(1, 10 + 1):
        sync_download_image()

    print(f"elapsed: {round(time.perf_counter() - start, 5)}")  # 15.4 (10) * 1000


def threading_mass_download_images():
    start = time.perf_counter()

    # thread_1 = threading.Thread(target=sync_download_image, args=(1, ))
    # thread_1.start()
    #
    # thread_2 = threading.Thread(target=sync_download_image, args=(2, ))
    # thread_2.start()
    #
    # thread_3 = threading.Thread(target=sync_download_image, args=(3, ))
    # thread_3.start()
    #
    # thread_1.join()  # заставить главный поток ждать дополнительный
    # thread_2.join()  # заставить главный поток ждать дополнительный
    # thread_3.join()  # заставить главный поток ждать дополнительный

    thread_list = []

    for i in range(1, 10 + 1):
        thread_list.append(threading.Thread(target=sync_download_image, args=()))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print(f"elapsed: {round(time.perf_counter() - start, 5)}")  # 1.4 (10) * 1000


def processing_mass_download_images():
    start = time.perf_counter()

    # process_1 = multiprocessing.Process(target=sync_download_image, args=())
    # process_1.start()
    #
    # process_1.join()  # заставить главный поток ждать дополнительный

    process_list = []

    for i in range(1, 10 + 1):
        process_list.append(multiprocessing.Process(target=sync_download_image, args=()))

    for process in process_list:
        process.start()

    for process in process_list:
        process.join()

    print(f"elapsed: {round(time.perf_counter() - start, 5)}")  # 2.48807 (0.1)


def async_mass_download_images():
    start = time.perf_counter()

    async def start_download():  # корутина - promise (обещание - future)
        await asyncio.gather(*[async_download_image() for _ in range(1, 10+1)])

    asyncio.run(start_download())

    print(f"elapsed: {round(time.perf_counter() - start, 5)}")  # 1.28807 (10) 0.12


if __name__ == "__main__":
    # sync_mass_download_images()        # 5.0  0199  - 0.5 * 10
    # threading_mass_download_images()   # 0.5  0146  - 0.5 * 10 / 10
    # processing_mass_download_images()  # 0.5  42573  - 0.5 * 10 / 10
    async_mass_download_images()         # 1.0
