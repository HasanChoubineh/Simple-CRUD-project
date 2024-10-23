from django.shortcuts import render
from .models import *

def posts_list_view(request):
    
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', context={'posts' : posts})
