from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.


def home(request):
    return render(request, 'index.html')


def passgen(request):
    char = list('abcdefghijklmnopqrstuvwxyz')
    password = ""

    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('digits'):
        char.extend(list('0123456789'))

    if request.GET.get('symbol'):
        char.extend(list('!@#$%^&*()_+-=[]{}<>,./?'))

    length = int(request.GET.get('length', 10))

    for x in range(length):
        password += random.choice(char)
    pas = {'password': password}
    return render(request, 'password.html', pas)
