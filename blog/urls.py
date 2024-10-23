from django.urls import path 
from . import views 

urlpatterns = [

    path('posts/', views.posts_list_view, name='posts_list')
]
