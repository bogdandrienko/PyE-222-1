########################################################################################################################
# TODO потоки исполнения
import random
import requests  # todo синхронная (последовательная)
import aiohttp  # todo асинхронная (параллельная)
import time
import threading
import multiprocessing
import asyncio
import concurrent.futures

# print(1)
# print(2)
# todo блокирующая
# for i in range(1, 5 + 1):
#     p = requests.get('https://upload.wikimedia.org/wikipedia/commons/a/a2/Python_royal_35.JPG', headers={
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
#                       'Chrome/102.0.0.0 Safari/537.36'
#     })
#     with open(f"temp/img{i}.jpg", "wb") as f:
#         # time.sleep(3.0)
#         f.write(p.content)
# todo блокирующая
# print(3)

# sync VS async VS threading VS multiprocessing

# sync =                1 процесс: 1 поток
# threading =           1 процесс: N поток
# multiprocessing =     N процесс: N поток
# async =               1 процесс: 1 поток


def time_measuring(func):
    def wrapper(*args, **kwargs):
        time_start = time.perf_counter()
        result = func(*args, **kwargs)
        time_stop = time.perf_counter()

        print("elapsed time: ", round(time_stop - time_start, 5))
        return result

    return wrapper


def sync_download_one_image():
    time.sleep(1.0)
    return None

    response = requests.get(url=url, headers=headers)
    with open(f"temp/image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
        opened_file.write(response.content)


@time_measuring
def sync_download_mass_image():
    # загрузка 10 картинок в этом потоке
    for i in range(1, 10 + 1):
        sync_download_one_image()


@time_measuring
def threading_download_mass_image():
    # new_thread = threading.Thread(target=sync_download_one_image, args=(), kwargs={})
    # new_thread.start()
    # new_thread.join()  # todo ТОЛЬКО ДЛЯ ТОГО, ЧТОБЫ ГЛАВНЫЙ ПОТОК НЕ ЗАВЕРШИЛСЯ РАНЬШЕ ОСТАЛЬНЫХ

    new_thread_list = []
    for i in range(1, 10 + 1):
        new_thread_list.append(threading.Thread(target=sync_download_one_image, args=(), kwargs={}))
    for i in new_thread_list:
        i.start()
    for i in new_thread_list:
        i.join()

    # # # todo чтобы не перенагрузить систему и выбрать "оптимальное количество потоков"
    # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #     for i in range(1, 10 + 1):
    #         executor.submit(sync_download_one_image)


@time_measuring
def processing_download_mass_image():
    # new_process = multiprocessing.Process(target=sync_download_one_image, args=(), kwargs={})
    # new_process.start()
    # new_process.join()  # todo ТОЛЬКО ДЛЯ ТОГО, ЧТОБЫ ГЛАВНЫЙ ПОТОК НЕ ЗАВЕРШИЛСЯ РАНЬШЕ ОСТАЛЬНЫХ

    new_process_list = []
    for i in range(1, 50 + 1):
        new_process_list.append(multiprocessing.Process(target=sync_download_one_image, args=(), kwargs={}))
    for i in new_process_list:
        i.start()
    for i in new_process_list:
        i.join()

    # # todo чтобы не перенагрузить систему и выбрать "оптимальное количество потоков"
    # with concurrent.futures.ProcessPoolExecutor(max_workers=8*2+1) as executor:
    #     for i in range(1, 10 + 1):
    #         executor.submit(sync_download_one_image)


async def async_download_one_image():
    # await asyncio.sleep(1.0)
    # return None
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as response_obj:
            data = await response_obj.read()
            with open(f"temp/image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
                opened_file.write(data)


@time_measuring
def async_download_mass_image():
    async def create_tasks():  # coroutines
        await asyncio.gather(*[async_download_one_image() for _ in range(1, 10 + 1)])

    asyncio.run(create_tasks())


if __name__ == "__main__":  #
    url = "https://picsum.photos/320/240/"  # todo global
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

    # sync_download_mass_image()            # elapsed time:  10.05191
    # threading_download_mass_image()       # elapsed time:  1.0152
    # processing_download_mass_image()      # elapsed time:  1.31037
    async_download_mass_image()  # elapsed time:  1.0141
    pass
