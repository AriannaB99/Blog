from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
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

    #def get_queryset(self):
     #   return Comments.objects.filter('blog_id' = )
def add_comment(request):
    # Get the context from the request.
    context = RequestContext(request)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():

            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return BlogDetailView(request)
        else:
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = CommentForm()

    return render_to_response('blog/add_comment.html', {'form': form}, context)

