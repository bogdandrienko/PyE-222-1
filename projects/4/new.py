import requests


class Todo:
    def __init__(self, title: str):
        self.title = title

    def get_name(self):
        print("Моё имя: ", self.title)

    def serialize(self):
        # json.dumn
        pass


response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = response.json()
print(todos)
arr_todo = []
for todo in todos:
    arr_todo.append(Todo(todo["title"]))

for todo in arr_todo:
    todo.get_name()
