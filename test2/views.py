from django.http import HttpResponse
from django.shortcuts import render
from .tasks import create_number

def home(request):
    return render(request,"index.html",context=None)

def new(request):
    if request.method == 'POST':
        total= request.POST.get('total')
        create_number.delay(int (total) )
    return render(request,"add.html",context=None)