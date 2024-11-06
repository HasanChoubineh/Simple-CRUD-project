from django.urls import path 
from . import views 

urlpatterns = [

    path('posts/', views.PostListView.as_view(), name='posts_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name= 'post_detail'),
    path('posts/add/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete')
]
