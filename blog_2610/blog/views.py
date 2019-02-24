from django.shortcuts import render, render_to_response
from django.http import HttpResponse
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

class BiohomeView(generic.ListView):
    model = Blog
    template_name = 'blog/biohome.html'
    context_object_name = 'latest_post_list'
    def get_queryset(self):
        return Blog.objects.order_by('-date_posted')[:2]

class ArchiveView(generic.ListView):
    model = Blog
    template_name = 'blog/archive.html'
    context_object_name = 'all_posts'
    def get_queryset(self):
        return Blog.objects.order_by('-date_posted')

class BlogDetailView(generic.DetailView):
    model =  Blog
    template_name = "blog/blog_detail.html"
    #template_name = "blog/detail.html"

    '''class BookDetailView(generic.DetailView):
    model = Book'''
    #def get_queryset(self):
     #   return Comments.objects.filter('blog_id' = )
def add_comment(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = CommentForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = CommentForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('blog/add_comment.html', {'form': form}, context)

