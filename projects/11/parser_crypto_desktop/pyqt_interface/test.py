import concurrent.futures
import time


def get_data(vals):
    # results = []
    # for i in vals:
    #     results.append(calculate(i))
    # return results

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for i in vals:
            futures.append(executor.submit(calculate, i))
        results = []
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
        return results


def calculate(val):
    time.sleep(0.15)  # НАГРУЗКА
    return float(val)


if __name__ == "__main__":
    start = time.perf_counter()
    _vals = ["1", "2", "3", "4", "5", "6", "7"] * 5
    print(_vals)  # ['1', '2', '3', '4', '5', '6', '7', '1', '2', '3', '4', '5', '6', '7', '
    print(get_data(_vals))  # 6 секунд, а нужно 2  # 0.91
    print("Elapsed time: ", round(time.perf_counter() - start, 2))
