from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.index, name='index'),
    path('bio', views.bio, name='bio'),
    path('techtips', views.techtips, name='techtips'),
    path('biohome', views.BiohomeView.as_view(), name = 'biohome'),
]


