from django.urls import path
from . import views
from django import urls

app_name = 'blog'

urlpatterns = [

    #path('', views.index, name='index'),
    #path('detail', views.DetailView.as_view(), name = 'detail'),
    path('index', views.bio, name='index'),
    path('techtips', views.techtips, name='techtips'),
    path('', views.BiohomeView, name = 'biohome'),
    path('archive', views.ArchiveView, name = 'archive'),
    path('biohome/<int:question_id>', views.BlogDetailView, name='blog_detail'),
    path('<int:question_id>/add_comment/', views.add_comment, name='add_comment'),
    path('init', views.init, name='init'),
    #path('biohome/add_comment', views.add_comment, name='add_comment'),  # NEW MAPPING!
]



