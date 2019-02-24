from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.index, name='index'),
    #path('detail', views.DetailView.as_view(), name = 'detail'),
    path('bio', views.bio, name='bio'),
    path('techtips', views.techtips, name='techtips'),
    path('biohome', views.BiohomeView.as_view(), name = 'biohome'),
    path('archive', views.ArchiveView.as_view(), name = 'archive'),
    path('biohome/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
]

urlpatterns += [
    path('comments/create/', views.CommentsCreate.as_view(), name='comments_create'),
    path('comments/<int:pk>/update/', views.CommentsUpdate.as_view(), name='comments_update'),
    path('comments/<int:pk>/delete/', views.CommentsDelete.as_view(), name='comments_delete'),
]


