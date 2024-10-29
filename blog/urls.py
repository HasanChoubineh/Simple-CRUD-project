from django.urls import path 
from . import views 

urlpatterns = [

    path('posts/', views.posts_list_view, name='posts_list'),
    path('posts/<int:pk>/', views.post_detail_view, name= 'post_detail'),
]
