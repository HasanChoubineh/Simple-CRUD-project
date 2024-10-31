from django.urls import path 
from . import views 

urlpatterns = [

    path('posts/', views.posts_list_view, name='posts_list'),
    path('posts/<int:pk>/', views.post_detail_view, name= 'post_detail'),
    path('posts/add/', views.create_post_view, name='post_create'),
    path('posts/<int:pk>/update/', views.update_post_view, name='post_update')
]
