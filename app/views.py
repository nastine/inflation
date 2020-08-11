from django.shortcuts import render
import csv

def inflation_view(request):
    template_name = 'inflation.html'
    # чтение csv-файла и заполнение контекста
    with open('./inflation_russia.csv', encoding='utf-8') as f:
        data = list(csv.reader(f, delimiter=';'))

    context = {
        'header': data[0],
        'body': data[1:],
    }

    return render(request, template_name, context)