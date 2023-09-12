from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random
import datetime
def home(request):
    return render(request, 'generator/home.html')
def password(request):

    Characters=list('abcdefhijklmnopqrstuvwxyz')
    length=int(request.GET.get('length',12))
    if request.GET.get('uppercase'):
        Characters.extend('ABCDEFGHIJKLMNOPQRSTUWXYZ')
    if request.GET.get('numbers'):
        Characters.extend('0123456789')
    if request.GET.get('special'):
        Characters.extend('!@#$%^&*(_-=+')
    thepassword=''
    for x in range(length):
        thepassword +=random.choice(Characters)
    return render(request, 'generator/password.html',{'password':thepassword})

def info(request):
    date=datetime.datetime.now()
    return render(request, 'generator/info.html',{'time':date})
