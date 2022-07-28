from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):

    select_line = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        select_line.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        select_line.extend(list('0123456789'))

    if request.GET.get('specials'):
        select_line.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length'))

    thepassword =''

    for i in range(length):
        thepassword += random.choice(select_line)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):

    return render(request, 'generator/about.html')







