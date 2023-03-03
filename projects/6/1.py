#Прочитать файл и создать папки из внетреннего массива внутри папки temp

#Прочитать файл
import json
import os
  
with open("new.json", "r") as f:
    data = json.load(f)
    print(data)


try:
    os.mkdir("temp")
except:
    pass

print(data["dirs"])

for i in data["dirs"]:
    print(i, type(i))
    print(i["name"])
    os.mkdir("temp/" + i["name"])


