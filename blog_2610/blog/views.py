from django.shortcuts import render
from django.http import HttpResponse

from time import strftime

def index(request):
    return render(request, 'blog/index.html', {'now': strftime('%c')})


def bio(request):
    return render(request, 'blog/bio.html')


def techtips(request):
    return render(request, 'blog/techtips.html')


highFives = 0
def highFive(request):
    # Bear with me, I don't have a database yet... :(
    global highFives
    highFives += 1
    return render(request, 'hello/highFive.html', { 'highFives': highFives })
