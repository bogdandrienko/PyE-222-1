import datetime

from django.http import HttpResponse
from django.shortcuts import render
from app import service


def index(request):
    # источники данных: excel, json|api, txt, csv, xml, SQL | NOSQL

    data = service.read_excel(filename='data.xlsx', is_have_titles=True)
    vips = []
    for idx, vip in enumerate(data, 1):
        item = {
            "id": idx,
            "title": '' if vip[0] is None else vip[0],
            "description": '' if vip[1] is None else vip[1],
            "price": '' if vip[2] is None else vip[2],
            "count": '' if vip[3] is None else vip[3],
            "date": '' if vip[4] is None else vip[4],
        }
        vips.append(item)

    data2 = service.read_json('data.json')

    return render(request, 'index.html', context={"vips": vips, "basics": data2})
