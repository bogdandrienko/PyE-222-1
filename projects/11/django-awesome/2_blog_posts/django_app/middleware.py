import datetime
from django.http import HttpRequest


class CustomLogsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)
        # response["Access-Control-Allow-Origin"] = "*"
        # response["Access-Control-Allow-Headers"] = "*"
        with open("logs.txt", "a") as file:
            file.write(f"{request.user.username} {request.path} {datetime.datetime.now()}\n")

        return response
