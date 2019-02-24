from django.urls import path
from . import views
from django import urls

app_name = 'blog'

urlpatterns = [

    path('', views.index, name='index'),
    #path('detail', views.DetailView.as_view(), name = 'detail'),
    path('bio', views.bio, name='bio'),
    path('techtips', views.techtips, name='techtips'),
    path('biohome', views.BiohomeView.as_view(), name = 'biohome'),
    path('archive', views.ArchiveView.as_view(), name = 'archive'),
    path('biohome/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('biohome/add_comment', views.add_comment, name='add_comment'),  # NEW MAPPING!
]



