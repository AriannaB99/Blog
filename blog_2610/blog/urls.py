from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('bio', views.bio, name='bio'),
    path('techtips', views.techtips, name='techtips'),
]
