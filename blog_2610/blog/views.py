from django.shortcuts import render
from django.http import HttpResponse
import datetime

from time import strftime

def index(request):
    return render(request, 'blog/index.html', {'now': strftime('%c')})


def bio(request):
    return render(request, 'blog/bio.html')


def techtips(request):
    return render(request, 'blog/techtips.html')

visitors = 0
def visitors(request):
    global visitors
    visitors += 1
    return render(request, 'blog/index.html', {'visitors': visitors})
