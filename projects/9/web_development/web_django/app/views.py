from django.http import HttpResponse, JsonResponse
import requests


def get_data(request):  # VIEW
    # DB  #   MODEL
    data = requests.get("http://127.0.0.1:8001/api/data/")
    # print(data.json())

    return JsonResponse(data=data.json(), safe=False)  # TEMPLATE
