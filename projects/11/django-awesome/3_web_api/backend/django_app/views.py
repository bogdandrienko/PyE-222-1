from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view


def home(request):
    return HttpResponse("OK")


@api_view(http_method_names=["GET", "POST"])
def api(request):
    print(request.GET)
    print(request.POST)
    print(request.data)

    return JsonResponse(data={"name": "DRF"}, safe=True)
