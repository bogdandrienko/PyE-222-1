from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import openpyxl


def get_string(request):
    return HttpResponse("я просто строка")


def get_json(request):
    dict1 = {"id": 1, "author": "Лев Толстой", "name": "Война и Мир"}
    return JsonResponse(data=dict1, safe=False)


def get_data(request):
    workbook = openpyxl.load_workbook('data.xlsx')
    worksheet = workbook.active
    matrix = []
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        new_dict = {"id": int(row[0]), "name": str(row[1]), "count": float(row[2]), "rating": int(row[3])}
        matrix.append(new_dict)
    # print(matrix)
    return render(request, "index.html", context={"data": matrix})
