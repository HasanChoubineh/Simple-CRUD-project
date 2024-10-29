from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def posts_list_view(request):
    
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/posts_list.html', context={'posts' : posts})


def post_detail_view(request,pk):

    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', context={'post' : post})