from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Blog
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from time import strftime

#def index(request):
 #   return render(request, 'blog/index.html', {'now': strftime('%c')})


def bio(request):
    return render(request, 'blog/bio.html')


def techtips(request):
    return render(request, 'blog/techtips.html')

visitors = 0
def index(request):
    global visitors
    visitors += 1
    return render(request, 'blog/index.html', {'visitors': visitors})

class BiohomeView(generic.ListView):
    model = Blog
    template_name = 'blog/biohome.html'
    context_object_name = 'latest_post_list'



    def get_queryset(self):
        return Blog.objects.order_by('-date_posted')[:5]

