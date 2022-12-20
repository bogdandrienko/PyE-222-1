import threading
import requests
import json
import threading


def get_all_data(count: int) -> list:
    response = requests.get(url="https://jsonplaceholder.typicode.com/todos/")
    print(response.json())
    data = response.json()[0:count:1]
    print(data)
    return data


def write_data(dict1: dict) -> None:
    with open(f"dicts/new{dict1['id']}.json", "w") as file:
        json.dump(dict1, file)


data1 = get_all_data(50)  # [{'userId': 1, 'id': 1, 'title': 'delectus aut auid': ... 50

# TODO sync
for i in data1:
    write_data(i)

# TODO threading
# thread_list = []
# for i in data1:
#     thread_list.append(threading.Thread(target=write_data, args=(i,)))
# for i in thread_list:
#     i.start()
# for i in thread_list:
#     i.join()


