from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from .models import Blog, Comments
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from blog.forms import CommentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

def  BiohomeView(request):
    latest_post_list = Blog.objects.order_by("-date_posted")[:5]
    template = loader.get_template('blog/biohome.html')
    context = {'latest_post_list': latest_post_list,}
    return HttpResponse(template.render(context, request))

def ArchiveView(request):
    latest_post_list = Blog.objects.order_by("-date_posted")
    template = loader.get_template('blog/archive.html')
    context = {'latest_post_list': latest_post_list, }
    return HttpResponse(template.render(context, request))

def BlogDetailView(request, question_id):
    try:
        blog = Blog.objects.get(pk = question_id)
    except Blog.DoesNotExist:
        raise Http404("Blog post does not exist")
    return render(request, 'blog/blog_detail.html', {'blog': blog})


def add_comment(request, question_id):
    if request.method == 'POST':
        try:
            blog = get_object_or_404(Blog, pk=question_id)
        except (KeyError, Blog.DoesNotExist):
            return render(request, 'blog/blog_detail.html', {'blog': blog})
        else:
            c = blog.comments_set.create(blog_id=question_id,
                                     content='Comment', commenter="Commenter",
                                     email_address="EmailAddress")
            c.save()

            return render(request, 'blog/blog_detail.html', {'blog': blog})

