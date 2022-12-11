import requests

url3 = "https://picsum.photos/600/600/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def get3(name: str | int):
    response = requests.get(url=url3, headers=headers)
    content1 = response.content  # bytes

    with open(f"images/new{name}.jpg", "wb") as image_file:
        image_file.write(content1)


for i in range(1, 10+1):
    get3(i)
