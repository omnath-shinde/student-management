from django.http import HttpResponse
from django.shortcuts import render
import datetime
# def home(request):
#     return HttpResponse("Hello World")


def home(request):
    return render(request, 'index.html', {})


def student_info(request):
    date = datetime.datetime.now()
    name = 'Omnath'
    rollno = 3
    city = 'Ambajogai'

    data = {
        'date': date,
        'name': name,
        'rollno': rollno,
        'city': city
    }
    return render(request, 'omnath.html', data)
